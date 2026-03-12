"""
retrieve.py
-----------
Query interface for local document retrieval.

Hybrid retrieval: semantic (embedding cosine similarity) + lexical (keyword matching).
Outputs a ranked list of candidate documents with scores and nomination reasons.

Usage:
  python scripts/retrieve.py "your query here" --config lit-retrieval.yaml
  python scripts/retrieve.py "your query" --config lit-retrieval.yaml --top-k 5
  python scripts/retrieve.py "your query" --config lit-retrieval.yaml --verbose
"""

import argparse
import json
import math
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Script directory — for importing embedding_provider
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
from embedding_provider import get_provider, cosine_similarity


# ---------------------------------------------------------------------------
# Configuration (shared with build_index.py)
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "notes_dir": "notes/",
    "sources_dir": "sources/",
    "index_path": "index/retrieval_index.json",
    "id_field": "citekey",
    "embedding_backend": "gemini",
    "embedding_dims": 768,
    "weight_paper_semantic": 0.4,
    "weight_section_semantic": 0.3,
    "weight_lexical": 0.3,
}


def load_config(config_path: str = None) -> dict:
    """Load configuration from a YAML file. Falls back to defaults."""
    config = dict(DEFAULT_CONFIG)

    if config_path:
        path = Path(config_path)
    elif os.environ.get("LIT_RETRIEVAL_CONFIG"):
        path = Path(os.environ["LIT_RETRIEVAL_CONFIG"])
    else:
        path = Path.cwd() / "lit-retrieval.yaml"

    if not path.exists():
        print(f"Config file not found: {path}", file=sys.stderr)
        print(f"Create one from config.example.yaml or specify --config", file=sys.stderr)
        sys.exit(1)

    config["_config_dir"] = str(path.resolve().parent)

    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()

        if not val:
            continue

        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]

        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
            config[key] = items
        elif val.isdigit():
            config[key] = int(val)
        elif re.match(r'^\d+\.\d+$', val):
            config[key] = float(val)
        else:
            config[key] = val

    # Resolve relative paths against config file location
    config_dir = Path(config["_config_dir"])
    for key in ("notes_dir", "sources_dir", "index_path"):
        val = config.get(key, "")
        if val and not Path(val).is_absolute():
            config[key] = str(config_dir / val)

    return config


# ---------------------------------------------------------------------------
# Lexical scoring
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """Simple tokenizer: lowercase, split on non-alphanumeric, remove short tokens."""
    tokens = re.findall(r'[a-zA-Z]{2,}|\d+(?:\.\d+)?', text.lower())
    # Remove very common stopwords
    stops = {"the", "and", "for", "with", "from", "that", "this", "are", "was",
             "were", "been", "have", "has", "had", "not", "but", "can", "all",
             "its", "our", "their", "which", "when", "where", "also", "more",
             "than", "into", "such", "each", "only", "both", "does", "use",
             "used", "using", "based", "between", "under", "over", "through"}
    return [t for t in tokens if t not in stops]


def lexical_score(query_tokens: list[str], text: str) -> float:
    """Score text against query tokens using keyword overlap + phrase bonus."""
    text_lower = text.lower()
    text_tokens = set(tokenize(text))

    if not query_tokens:
        return 0.0

    # Token overlap
    matches = sum(1 for t in query_tokens if t in text_tokens)
    overlap = matches / len(query_tokens)

    # Phrase bonus: check if consecutive query tokens appear near each other
    phrase_bonus = 0.0
    if len(query_tokens) >= 2:
        for i in range(len(query_tokens) - 1):
            if query_tokens[i] in text_lower and query_tokens[i+1] in text_lower:
                # Check proximity: are they within ~100 chars of each other?
                for m in re.finditer(re.escape(query_tokens[i]), text_lower):
                    window = text_lower[m.start():m.start() + 100]
                    if query_tokens[i+1] in window:
                        phrase_bonus += 0.15
                        break

    return min(overlap + phrase_bonus, 1.0)


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------

def load_index(index_path: Path) -> dict:
    """Load the retrieval index."""
    if not index_path.exists():
        print(f"Error: Index not found at {index_path}", file=sys.stderr)
        print(f"Run: python scripts/build_index.py --config <your-config.yaml>", file=sys.stderr)
        sys.exit(1)
    return json.loads(index_path.read_text(encoding="utf-8"))


def retrieve(query: str, config: dict, top_k: int = 10, verbose: bool = False,
             alpha: float = None, beta: float = None, gamma: float = None) -> dict:
    """
    Hybrid retrieval over local documents.

    Args:
        query: Natural language query
        config: Configuration dict
        top_k: Number of candidates to return
        alpha: Weight for document card semantic similarity (overrides config)
        beta: Weight for section summary semantic similarity (overrides config)
        gamma: Weight for lexical matching (overrides config)
        verbose: Print detailed scoring info

    Returns:
        Dict with query, model, and ranked candidates.
    """
    # Resolve weights from args -> config -> defaults
    if alpha is None:
        alpha = float(config.get("weight_paper_semantic", 0.4))
    if beta is None:
        beta = float(config.get("weight_section_semantic", 0.3))
    if gamma is None:
        gamma = float(config.get("weight_lexical", 0.3))

    index_path = Path(config["index_path"])
    notes_dir = config.get("notes_dir", "notes/")
    sources_dir = config.get("sources_dir", "sources/")

    index = load_index(index_path)
    metadata = index["metadata"]
    doc_cards = index.get("document_cards", index.get("paper_cards", []))
    section_summaries = index["section_summaries"]
    section_full_texts = index.get("section_full_texts", {})

    if verbose:
        print(f"Index: {metadata.get('document_count', metadata.get('paper_count', '?'))} documents, {metadata['section_count']} sections")
        print(f"Model: {metadata['embedding_model']}")
        print()

    # Embed query
    provider = get_provider(dims=metadata["dims"])
    query_embedding = provider.embed([query], task_type="RETRIEVAL_QUERY")[0]
    query_tokens = tokenize(query)

    if verbose:
        print(f"Query tokens: {query_tokens}")
        print()

    # Determine ID field name from index (support both "id" and "citekey")
    id_key = "id" if doc_cards and "id" in doc_cards[0] else "citekey"

    # --- Semantic scoring: document cards ---
    doc_semantic = {}
    for card in doc_cards:
        if card.get("embedding"):
            sim = cosine_similarity(query_embedding, card["embedding"])
            doc_semantic[card[id_key]] = sim

    # --- Semantic scoring: section summaries ---
    sec_id_key = "id" if section_summaries and "id" in section_summaries[0] else "citekey"
    doc_section_semantic = defaultdict(float)
    doc_relevant_sections = defaultdict(list)
    for sec in section_summaries:
        if sec.get("embedding"):
            sim = cosine_similarity(query_embedding, sec["embedding"])
            did = sec[sec_id_key]
            if sim > doc_section_semantic[did]:
                doc_section_semantic[did] = sim
            if sim > 0.3:  # threshold for "relevant section"
                doc_relevant_sections[did].append((sec["heading"], sim))

    # Sort relevant sections by score
    for did in doc_relevant_sections:
        doc_relevant_sections[did].sort(key=lambda x: -x[1])
        doc_relevant_sections[did] = doc_relevant_sections[did][:5]  # top 5 sections

    # --- Lexical scoring ---
    doc_lexical = defaultdict(float)
    doc_lexical_terms = defaultdict(list)

    # Score document cards lexically
    for card in doc_cards:
        did = card[id_key]
        score = lexical_score(query_tokens, card["text"])
        if score > doc_lexical[did]:
            doc_lexical[did] = score
        if score > 0:
            matched = [t for t in query_tokens if t in card["text"].lower()]
            doc_lexical_terms[did].extend(matched)

    # Score section full texts lexically
    for sec in section_summaries:
        did = sec[sec_id_key]
        full_key = f"{sec[sec_id_key]}::{sec['heading']}"
        full_text = section_full_texts.get(full_key, sec.get("text", ""))
        score = lexical_score(query_tokens, full_text)
        if score > doc_lexical[did]:
            doc_lexical[did] = score
        if score > 0:
            matched = [t for t in query_tokens if t in full_text.lower()]
            doc_lexical_terms[did].extend(matched)

    # Deduplicate lexical terms
    for did in doc_lexical_terms:
        doc_lexical_terms[did] = list(set(doc_lexical_terms[did]))

    # --- Merge scores ---
    all_ids = set()
    all_ids.update(doc_semantic.keys())
    all_ids.update(doc_section_semantic.keys())
    all_ids.update(k for k, v in doc_lexical.items() if v > 0)

    candidates = []
    for did in all_ids:
        sem_doc = doc_semantic.get(did, 0.0)
        sem_section = doc_section_semantic.get(did, 0.0)
        lex = doc_lexical.get(did, 0.0)

        score = alpha * sem_doc + beta * sem_section + gamma * lex

        # Build nomination reasons
        reasons = []
        if sem_doc > 0.3:
            reasons.append(f"semantic: document card ({sem_doc:.2f})")
        if sem_section > 0.3:
            reasons.append(f"semantic: section match ({sem_section:.2f})")
        if lex > 0:
            terms = doc_lexical_terms.get(did, [])
            if terms:
                reasons.append(f"lexical: {', '.join(repr(t) for t in terms[:5])}")

        # Get metadata from document card if available
        card_match = next((c for c in doc_cards if c[id_key] == did), None)
        title = card_match["title"] if card_match else ""
        relevance = card_match.get("relevance", 0) if card_match else 0

        # Get relevant sections
        rel_sections = [h for h, s in doc_relevant_sections.get(did, [])]

        # Source paths
        source_note = f"{notes_dir}{did}.md"
        source_doc = f"{sources_dir}{did}/{did}.md"

        candidates.append({
            "id": did,
            "title": title,
            "score": round(score, 4),
            "semantic_document": round(sem_doc, 4),
            "semantic_section": round(sem_section, 4),
            "lexical": round(lex, 4),
            "relevance": relevance,
            "reasons": reasons,
            "relevant_sections": rel_sections,
            "source_note": source_note,
            "source_document": source_doc,
        })

    # Sort by score (with relevance as tiebreaker)
    candidates.sort(key=lambda c: (-c["score"], -c["relevance"]))
    candidates = candidates[:top_k]

    if verbose:
        print(f"\nTop {len(candidates)} candidates:")
        print("-" * 80)
        for i, c in enumerate(candidates):
            print(f"  {i+1}. [{c['id']}] score={c['score']}")
            print(f"     title: {c['title'][:70]}")
            print(f"     sem_doc={c['semantic_document']} sem_sec={c['semantic_section']} lex={c['lexical']}")
            print(f"     reasons: {'; '.join(c['reasons'])}")
            if c['relevant_sections']:
                print(f"     sections: {', '.join(c['relevant_sections'][:3])}")
            print()

    return {
        "query": query,
        "model": metadata["embedding_model"],
        "top_k": top_k,
        "weights": {"alpha": alpha, "beta": beta, "gamma": gamma},
        "candidates": candidates,
    }


def main():
    parser = argparse.ArgumentParser(description="Query local document retrieval index")
    parser.add_argument("query", help="Natural language query")
    parser.add_argument("--config", default=None, help="Path to config YAML file")
    parser.add_argument("--top-k", type=int, default=10, help="Number of candidates (default: 10)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed scoring")
    parser.add_argument("--alpha", type=float, default=None, help="Document semantic weight")
    parser.add_argument("--beta", type=float, default=None, help="Section semantic weight")
    parser.add_argument("--gamma", type=float, default=None, help="Lexical weight")
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_config()

    result = retrieve(
        args.query,
        config=config,
        top_k=args.top_k,
        verbose=args.verbose,
        alpha=args.alpha,
        beta=args.beta,
        gamma=args.gamma,
    )

    if not args.verbose:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
