"""
build_index.py
--------------
Build a retrieval index over local markdown documents.

Creates two types of retrieval objects:
  1. Document cards — one per note, built from frontmatter + configurable sections
  2. Section summaries — one per heading in source documents

Embeddings are for ROUTING only (finding relevant documents).
Final answers come from full-text reading by the AI agent.

Usage:
  python scripts/build_index.py --config lit-retrieval.yaml              # full build
  python scripts/build_index.py --config lit-retrieval.yaml --incremental # only new/modified
  python scripts/build_index.py --config lit-retrieval.yaml --model openai
  python scripts/build_index.py --config lit-retrieval.yaml --dims 768
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Script directory — for importing embedding_provider
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
from embedding_provider import get_provider


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "notes_dir": "notes/",
    "sources_dir": "sources/",
    "index_path": "index/retrieval_index.json",
    "id_field": "citekey",
    "card_metadata_fields": ["title", "authors", "year", "topics"],
    "card_sections": ["Summary", "Key Findings"],
    "skip_statuses": ["unread"],
    "embedding_backend": "gemini",
    "embedding_dims": 768,
    "weight_paper_semantic": 0.4,
    "weight_section_semantic": 0.3,
    "weight_lexical": 0.3,
}


def load_config(config_path: str = None) -> dict:
    """Load configuration from a YAML file. Falls back to defaults."""
    config = dict(DEFAULT_CONFIG)

    # Find config file
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

    # Store config file location for resolving relative paths
    config["_config_dir"] = str(path.resolve().parent)

    # Simple YAML parser (stdlib only — no pyyaml dependency)
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

        # Strip quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]

        # Inline list: [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
            config[key] = items
        # Integer
        elif val.isdigit():
            config[key] = int(val)
        # Float
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
# YAML frontmatter parsing (stdlib only — no pyyaml dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown. Returns (frontmatter_dict, body)."""
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    yaml_block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    fm = {}

    current_key = None
    current_list = None

    for line in yaml_block.split("\n"):
        # List item under a key
        if line.strip().startswith("- ") and current_key:
            val = line.strip()[2:].strip().strip('"').strip("'")
            if current_list is None:
                current_list = []
            current_list.append(val)
            fm[current_key] = current_list
            continue

        # Key: value pair
        if current_list is not None:
            current_list = None

        match = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip().strip('"').strip("'")
            current_key = key

            # Inline list: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                items = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
                fm[key] = items
                current_list = None
            elif val:
                fm[key] = val
                current_list = None
            else:
                # Key with no inline value — next lines might be list items
                current_list = []
                fm[key] = current_list

    # Convert relevance to int if present
    if "relevance" in fm:
        try:
            fm["relevance"] = int(fm["relevance"])
        except (ValueError, TypeError):
            fm["relevance"] = 3

    # Convert year to int if present
    if "year" in fm:
        try:
            fm["year"] = int(fm["year"])
        except (ValueError, TypeError):
            pass

    return fm, body


def extract_section(body: str, heading: str) -> str:
    """Extract text under a specific ## heading from markdown body."""
    pattern = rf'^##\s+{re.escape(heading)}\s*$'
    match = re.search(pattern, body, re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    # Find next ## heading
    next_heading = re.search(r'^##\s+', body[start:], re.MULTILINE)
    if next_heading:
        end = start + next_heading.start()
    else:
        end = len(body)
    return body[start:end].strip()


# ---------------------------------------------------------------------------
# Document card extraction
# ---------------------------------------------------------------------------

def build_document_cards(config: dict) -> list[dict]:
    """Build document cards from all notes in the configured directory."""
    cards = []
    notes_dir = Path(config["notes_dir"])
    if not notes_dir.exists():
        print(f"Warning: {notes_dir} does not exist", file=sys.stderr)
        return cards

    id_field = config["id_field"]
    skip_statuses = config.get("skip_statuses", ["unread"])
    card_sections = config.get("card_sections", ["Summary", "Key Findings"])
    card_metadata_fields = config.get("card_metadata_fields", ["title", "authors", "year", "topics"])

    for note_path in sorted(notes_dir.glob("*.md")):
        if note_path.name == "README.md":
            continue

        content = note_path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(content)

        doc_id = fm.get(id_field, note_path.stem)
        status = fm.get("status", "unread")

        # Skip documents with excluded statuses
        if status in skip_statuses:
            continue

        # Extract metadata fields
        title = fm.get("title", "")
        authors = fm.get("authors", [])
        if isinstance(authors, str):
            authors = [authors]
        year = fm.get("year", "")
        topics = fm.get("topics", [])
        if isinstance(topics, str):
            topics = [topics]
        relevance = fm.get("relevance", 0)
        if not isinstance(relevance, int):
            try:
                relevance = int(relevance)
            except (ValueError, TypeError):
                relevance = 0

        # Build embedding text from configurable metadata and sections
        parts = []
        for field in card_metadata_fields:
            val = fm.get(field, "")
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val[:5])
            if val:
                parts.append(f"{field.title()}: {val}")

        for section_name in card_sections:
            section_text = extract_section(body, section_name)
            if section_text:
                parts.append(f"{section_name}: {section_text}")

        embed_text = "\n".join(parts)

        if not embed_text.strip():
            continue

        cards.append({
            "id": doc_id,
            "title": title,
            "authors": authors,
            "year": year,
            "topics": topics,
            "relevance": relevance,
            "status": status,
            "text": embed_text,
            "embedding": None,  # filled later
            "source": str(note_path),
        })

    return cards


# ---------------------------------------------------------------------------
# Section summary extraction
# ---------------------------------------------------------------------------

def split_sections(markdown: str) -> list[dict]:
    """Split markdown into sections at ## and ### headings."""
    sections = []
    lines = markdown.split("\n")

    current_heading = None
    current_start = 0
    current_lines = []

    for i, line in enumerate(lines):
        # Match ## or ### headings (not # which is typically the title)
        heading_match = re.match(r'^(#{2,3})\s+(.+)', line)
        if heading_match:
            # Save previous section
            if current_heading is not None and current_lines:
                text = "\n".join(current_lines).strip()
                if len(text) >= 50:  # skip very short sections
                    sections.append({
                        "heading": current_heading,
                        "text": text,
                        "lines": [current_start + 1, i],  # 1-indexed
                    })
            current_heading = heading_match.group(2).strip()
            current_start = i
            current_lines = []
        else:
            current_lines.append(line)

    # Last section
    if current_heading is not None and current_lines:
        text = "\n".join(current_lines).strip()
        if len(text) >= 50:
            sections.append({
                "heading": current_heading,
                "text": text,
                "lines": [current_start + 1, len(lines)],
            })

    return sections


def build_section_summaries(config: dict) -> list[dict]:
    """Build section summaries from all source documents."""
    summaries = []
    sources_dir = Path(config["sources_dir"])
    id_field = config["id_field"]

    if not sources_dir.exists():
        print(f"Warning: {sources_dir} does not exist", file=sys.stderr)
        return summaries

    for doc_dir in sorted(sources_dir.iterdir()):
        if not doc_dir.is_dir():
            continue

        doc_id = doc_dir.name
        md_file = doc_dir / f"{doc_id}.md"
        if not md_file.exists():
            continue

        content = md_file.read_text(encoding="utf-8", errors="replace")
        sections = split_sections(content)

        for sec in sections:
            # Embedding text: doc_id + heading + truncated section content
            embed_text = f"{doc_id}: {sec['heading']}\n{sec['text'][:500]}"

            summaries.append({
                "id": doc_id,
                "heading": sec["heading"],
                "text": sec["text"][:500],  # truncated for embedding
                "full_text": sec["text"],    # full text for lexical search
                "embedding": None,           # filled later
                "source": str(md_file),
                "lines": sec["lines"],
            })

    return summaries


# ---------------------------------------------------------------------------
# Index building
# ---------------------------------------------------------------------------

def load_existing_index(index_path: Path) -> dict | None:
    """Load existing index for incremental builds."""
    if not index_path.exists():
        return None
    try:
        return json.loads(index_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def build_index(args):
    """Main index building function."""
    config = load_config(args.config)

    # CLI overrides
    if args.model:
        config["embedding_backend"] = args.model
    if args.dims:
        config["embedding_dims"] = args.dims

    notes_dir = Path(config["notes_dir"])
    sources_dir = Path(config["sources_dir"])
    index_path = Path(config["index_path"])

    print(f"Building retrieval index...")
    print(f"  Notes dir:   {notes_dir}")
    print(f"  Sources dir: {sources_dir}")
    print(f"  Output:      {index_path}")
    print()

    # Extract retrieval objects
    print("Extracting document cards from notes...")
    doc_cards = build_document_cards(config)
    print(f"  -> {len(doc_cards)} document cards")

    print("Extracting section summaries from source documents...")
    section_summaries = build_section_summaries(config)
    print(f"  -> {len(section_summaries)} section summaries")
    print()

    if not doc_cards and not section_summaries:
        print("No content to index. Exiting.", file=sys.stderr)
        sys.exit(1)

    # Incremental mode: skip documents already in the index
    existing_index = load_existing_index(index_path) if args.incremental else None
    if existing_index and args.incremental:
        existing_ids = {c["id"] for c in existing_index.get("document_cards", [])}
        new_cards = [c for c in doc_cards if c["id"] not in existing_ids]
        # For existing cards, reuse their embeddings
        reused_cards = []
        for ec in existing_index.get("document_cards", []):
            matching = [c for c in doc_cards if c["id"] == ec["id"]]
            if matching:
                matching[0]["embedding"] = ec.get("embedding")
                reused_cards.append(matching[0])

        existing_section_keys = {
            (s["id"], s["heading"]) for s in existing_index.get("section_summaries", [])
        }
        new_sections = [
            s for s in section_summaries
            if (s["id"], s["heading"]) not in existing_section_keys
        ]
        reused_sections = []
        for es in existing_index.get("section_summaries", []):
            matching = [
                s for s in section_summaries
                if s["id"] == es["id"] and s["heading"] == es["heading"]
            ]
            if matching:
                matching[0]["embedding"] = es.get("embedding")
                reused_sections.append(matching[0])

        print(f"Incremental mode: {len(new_cards)} new cards, {len(new_sections)} new sections")
        print(f"  Reusing {len(reused_cards)} card embeddings, {len(reused_sections)} section embeddings")

        cards_to_embed = new_cards
        sections_to_embed = new_sections
        all_cards = reused_cards + new_cards
        all_sections = reused_sections + new_sections
    else:
        cards_to_embed = doc_cards
        sections_to_embed = section_summaries
        all_cards = doc_cards
        all_sections = section_summaries

    # Initialize embedding provider
    backend = config.get("embedding_backend", "gemini")
    dims = int(config.get("embedding_dims", 768))
    print(f"Initializing embedding provider (backend={backend})...")
    provider = get_provider(backend=backend, dims=dims)
    print(f"  Model: {provider.model_name()}")
    print(f"  Dimensions: {dims}")
    print()

    # Embed document cards
    if cards_to_embed:
        print(f"Embedding {len(cards_to_embed)} document cards...")
        card_texts = [c["text"] for c in cards_to_embed]
        card_embeddings = provider.embed(card_texts, task_type="RETRIEVAL_DOCUMENT")
        for card, emb in zip(cards_to_embed, card_embeddings):
            card["embedding"] = emb
        print(f"  Done.")
    else:
        print("No new document cards to embed.")

    # Embed section summaries
    if sections_to_embed:
        print(f"Embedding {len(sections_to_embed)} section summaries...")
        sec_texts = [f"{s['id']}: {s['heading']}\n{s['text']}" for s in sections_to_embed]
        sec_embeddings = provider.embed(sec_texts, task_type="RETRIEVAL_DOCUMENT")
        for sec, emb in zip(sections_to_embed, sec_embeddings):
            sec["embedding"] = emb
        print(f"  Done.")
    else:
        print("No new section summaries to embed.")

    print()

    # Build final index
    index = {
        "metadata": {
            "version": 1,
            "embedding_model": provider.model_name(),
            "dims": dims,
            "built": datetime.now(timezone.utc).isoformat(),
            "document_count": len(all_cards),
            "section_count": len(all_sections),
        },
        "document_cards": all_cards,
        "section_summaries": [
            {k: v for k, v in s.items() if k != "full_text"}
            for s in all_sections
        ],
        # Store full_text separately to keep main index scannable
        "section_full_texts": {
            f"{s['id']}::{s['heading']}": s["full_text"]
            for s in all_sections
        },
    }

    # Write index
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=None), encoding="utf-8")
    index_size_mb = index_path.stat().st_size / (1024 * 1024)

    print(f"Index written to {index_path}")
    print(f"  Size: {index_size_mb:.1f} MB")
    print(f"  Document cards: {len(all_cards)}")
    print(f"  Section summaries: {len(all_sections)}")
    print(f"  Model: {provider.model_name()}")


def main():
    parser = argparse.ArgumentParser(description="Build local document retrieval index")
    parser.add_argument("--config", default=None, help="Path to config YAML file (default: lit-retrieval.yaml in CWD)")
    parser.add_argument("--model", default=None, help="Embedding backend override: gemini or openai")
    parser.add_argument("--dims", type=int, default=None, help="Output embedding dimensions override")
    parser.add_argument("--incremental", action="store_true", help="Only embed new/modified documents")
    args = parser.parse_args()
    build_index(args)


if __name__ == "__main__":
    main()
