---
name: local-deep-research
description: Hybrid semantic + lexical retrieval over a local markdown knowledge base. Ask questions about your document collection — Claude retrieves relevant candidates, reads full text, and synthesizes grounded answers with citations. Embeddings for routing, not evidence.
argument-hint: "query about your documents"
---

# Local Deep Research

A skill for reasoning over large local document collections. You have 50+ papers, notes, or docs as markdown files — this skill lets you ask conceptual questions across all of them.

**Core philosophy: Embeddings for routing, not evidence.** Embeddings find which documents are relevant. Claude then reads the actual full text and synthesizes answers from the source material. No chunk-based RAG, no hallucinated summaries.

## Prerequisites

1. A `lit-retrieval.yaml` config file in your project root (copy from `config.example.yaml`)
2. A built retrieval index (run `build_index.py` after setting up your config)
3. `GOOGLE_API_KEY` or `OPENAI_API_KEY` set in environment or `.env` file

## Trigger

`/local-deep-research "query"`

Examples:
- `/local-deep-research "What do my notes say about error correction performance?"`
- `/local-deep-research "Compare approaches to state preparation"`
- `/local-deep-research "Which papers discuss noise models?"`
- `/local-deep-research "gottesman2001"` (single-document lookup)

---

## Intent Classification

Classify the query into one of two intents:

| Intent | Signals | Route |
|--------|---------|-------|
| **Single-document lookup** | Names a specific document, author, or ID | Direct Lookup |
| **Collection query** | Conceptual question, asks about multiple docs, synthesis, comparison | Retrieval Pipeline |

**Single-document lookup examples**:
- "tell me about gottesman2001_encoding"
- "what does Albert 2017 say about performance?"
- "summarize cai2023_quantum"

**Collection query examples**:
- "what do my notes say about error correction under noise?"
- "compare the approaches discussed across my papers"
- "which documents discuss performance bounds?"
- "summarize what is known about state preparation"

---

## Direct Lookup Flow

For queries about a specific known document:

1. Scan the configured `notes_dir` for files matching the named ID (filename or frontmatter ID field).
2. Read the matching note file.
3. If a full-text source exists in `sources_dir/[id]/[id].md`, read that too.
4. Answer directly from the loaded content.

---

## Collection Query Pipeline

### Step 1: Retrieve candidates

Run the retrieval script:
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/retrieve.py "QUERY_HERE" --config lit-retrieval.yaml --top-k 10 --verbose
```

This performs hybrid retrieval (semantic embeddings + lexical keyword matching) over the local index and returns a ranked list of candidate documents with scores and nomination reasons.

**If the index doesn't exist or is stale**, tell the user:
> "The retrieval index needs to be built. Run: `python3 ${CLAUDE_SKILL_DIR}/scripts/build_index.py --config lit-retrieval.yaml`"

### Step 2: Review candidates

Examine the returned candidate list. Consider:
- Scores and nomination reasons (semantic vs. lexical signals)
- Relevant sections identified for each document
- Document relevance ratings from note frontmatter

### Step 3: Progressive disclosure (optional)

For borderline candidates, read their note summaries to decide whether full-text loading is warranted.

### Step 4: Load full text

Select 3-6 documents for full reading. For each:
- Read the full-text source from `sources_dir/[id]/[id].md` (converted markdown)
- If the source is unavailable, fall back to the note file from `notes_dir/[id].md`
- Cap at 6 documents to stay within context budget

### Step 5: Synthesize grounded answer

Write a response that:
- Directly answers the question from loaded full-text sources
- Uses in-text citations: `(document_id, Section Title)` or `(document_id, lines X-Y)`
- Quotes specific results, equations, or key findings from the documents
- For broad/brainstorming queries: explicitly separates **direct claims from sources** vs. **inferred cross-document connections** vs. **speculative ideas**
- Includes a "**Sources used**" footer listing all cited documents with full titles
- Notes any additional candidates identified but not loaded due to context limits

### Step 6: Handle edge cases

- **Document exists only as a note** (no source markdown): answer from note, state limitation
- **Query uses exact notation or technical terms**: the lexical layer should catch these
- **Broad query**: load more candidates' note summaries before selecting for full reading

---

## Index Management

### Build the index (first time or full rebuild)
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_index.py --config lit-retrieval.yaml
```

### Incremental update (after adding new documents)
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_index.py --config lit-retrieval.yaml --incremental
```

### Override embedding backend
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_index.py --config lit-retrieval.yaml --model openai
```

---

## How the Retrieval Works

The retrieval system scores documents using three signals:

1. **Document card semantic similarity** (weight: 0.4) — cosine similarity between the query embedding and each document's card (built from note frontmatter + summary sections)
2. **Section semantic similarity** (weight: 0.3) — cosine similarity between the query embedding and section-level embeddings from the source documents
3. **Lexical keyword matching** (weight: 0.3) — token overlap + bigram phrase proximity bonus

Final score = weighted sum of all three signals. Sections nominate their parent document (paper-centered ranking).

This hybrid approach ensures:
- Semantic search catches conceptually relevant documents even without exact keyword matches
- Lexical search catches exact technical terms that embeddings might miss
- Section-level embeddings find documents where the relevant content is in a specific section, not the abstract
