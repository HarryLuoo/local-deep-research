# Local Deep Research

**A Claude Code skill for reasoning over large local document collections.**

You have 50+ papers, notes, or docs as markdown files. You want to ask questions across them — not one at a time, but conceptually: *"What do my sources say about X?"*

This skill builds a hybrid retrieval index (semantic embeddings + lexical keyword matching), finds the most relevant documents, then has Claude read the actual full text and synthesize a grounded answer with precise citations.

**Embeddings for routing, not evidence.** Unlike chunk-based RAG, this system uses embeddings only to find *which* documents are relevant. The actual answer comes from Claude reading the complete source text — no hallucinated summaries, no lost context, no chunk boundary artifacts.

---

## Example

The repo ships with 3 real quantum computing papers as a test knowledge base. Here's what retrieval looks like:

```
$ python scripts/retrieve.py "bosonic codes under photon loss" \
    --config example/config.yaml --verbose

Index: 3 documents, 75 sections
Model: models/gemini-embedding-2-preview
Query tokens: ['bosonic', 'codes', 'photon', 'loss']

Top 3 candidates:
--------------------------------------------------------------------------------
  1. [albert2017_performance] score=0.859
     title: Performance and structure of single-mode bosonic codes
     sem_doc=0.83 sem_sec=0.76 lex=1.0
     reasons: semantic: document card (0.83); lexical: 'codes', 'loss', 'bosonic', 'photon'

  2. [gottesman2001_encoding] score=0.848
     title: Encoding a qubit in an oscillator
     sem_doc=0.80 sem_sec=0.76 lex=1.0
     reasons: semantic: document card (0.80); lexical: 'codes', 'loss', 'bosonic', 'photon'

  3. [cai2023_quantum] score=0.819
     title: Quantum error mitigation
     sem_doc=0.71 sem_sec=0.78 lex=1.0
     reasons: semantic: document card (0.71); lexical: 'codes', 'loss', 'bosonic', 'photon'
```

Claude then reads the full text of the top candidates and synthesizes a grounded answer with `(document_id, Section Title)` citations.

**Try it yourself:**
```bash
python scripts/retrieve.py "error correction performance" --config example/config.yaml --verbose
```

---

## How It Works

```
Your query
    |
    v
+-------------------------------------+
|  Hybrid Retrieval Engine             |
|                                      |
|  1. Embed query (Gemini/OpenAI)      |
|                                      |
|  2. Semantic search:                 |
|     - cosine sim vs document cards   |
|     - cosine sim vs section summaries|
|                                      |
|  3. Lexical search:                  |
|     - keyword overlap + phrase bonus |
|                                      |
|  4. Merge & rank:                    |
|     score = 0.4 * doc_semantic       |
|           + 0.3 * section_semantic   |
|           + 0.3 * lexical            |
+------------------+------------------+
                   |
            Top 10 candidates
            with scores + reasons
                   |
                   v
         Claude reads full text
         of top 3-6 documents
                   |
                   v
         Grounded answer with
         precise citations
```

**Document cards** — one per note, built from YAML frontmatter + configurable summary sections. Captures what each document is *about*.

**Section summaries** — one per `##`/`###` heading in source documents. Finds documents where the relevant content is in a specific section, not just the abstract.

**Lexical layer** — catches exact technical terms (like "Petz map" or "CNOT gate") that embeddings alone might miss.

**Full-text reading** — Claude reads the actual complete source, not chunks. This is what prevents hallucination.

---

## Quick Start: Give This URL to Your Agent

The easiest way to install is to give your AI coding agent (Claude Code, etc.) this repo URL and ask it to set it up:

```
https://github.com/YOUR_USERNAME/local-deep-research
```

Tell your agent: *"Install this skill for my project and help me configure it for my documents."*

The agent will:
1. Clone the repo
2. Read this README
3. Set up the skill in your project
4. Guide you through configuration

---

## Manual Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/local-deep-research.git
```

### 2. Install the skill into your project

Copy the skill files into your project's `.claude/skills/` directory:

```bash
mkdir -p your-project/.claude/skills/local-deep-research
cp local-deep-research/SKILL.md your-project/.claude/skills/local-deep-research/
cp -r local-deep-research/scripts your-project/.claude/skills/local-deep-research/
```

### 3. Install Python dependencies

You need one of these (not both):

```bash
pip install google-generativeai   # Primary: Gemini embedding-2-preview (free tier)
# OR
pip install openai                # Fallback: text-embedding-3-large ($0.13/M tokens)
```

### 4. Set your API key

Create a `.env` file in your project root:

```bash
# Primary (recommended — free tier is sufficient)
GOOGLE_API_KEY=your-gemini-api-key

# OR fallback
OPENAI_API_KEY=your-openai-api-key
```

### 5. Create your configuration

```bash
cp local-deep-research/config.example.yaml your-project/lit-retrieval.yaml
```

Edit `lit-retrieval.yaml` to point to your documents:

```yaml
notes_dir: "my-notes/"           # Your markdown notes with YAML frontmatter
sources_dir: "my-sources/"       # Full-text source documents (optional)
index_path: "index/retrieval_index.json"
id_field: "citekey"              # Frontmatter field for document ID
card_sections: ["Summary", "Key Findings"]  # Sections to embed from notes
```

### 6. Build the index

```bash
python .claude/skills/local-deep-research/scripts/build_index.py --config lit-retrieval.yaml
```

### 7. Test it

```bash
python .claude/skills/local-deep-research/scripts/retrieve.py "your test query" --config lit-retrieval.yaml --verbose
```

---

## Configuration Reference

All settings live in a single YAML file (default: `lit-retrieval.yaml` in your project root).

| Field | Default | Description |
|-------|---------|-------------|
| `notes_dir` | `"notes/"` | Directory with your markdown notes (YAML frontmatter required) |
| `sources_dir` | `"sources/"` | Directory with full-text source documents. Each source is `sources_dir/[id]/[id].md` |
| `index_path` | `"index/retrieval_index.json"` | Where to store the retrieval index |
| `id_field` | `"citekey"` | YAML frontmatter field used as document identifier |
| `card_metadata_fields` | `["title", "authors", "year", "topics"]` | Frontmatter fields included in card text for embedding |
| `card_sections` | `["Summary", "Key Findings"]` | `##` sections to extract from notes for embedding |
| `skip_statuses` | `["unread"]` | Notes with these `status` values are excluded from the index |
| `embedding_backend` | `"gemini"` | `"gemini"` or `"openai"` |
| `embedding_dims` | `768` | Output embedding dimensions |
| `weight_paper_semantic` | `0.4` | Weight for document card semantic similarity |
| `weight_section_semantic` | `0.3` | Weight for section summary semantic similarity |
| `weight_lexical` | `0.3` | Weight for lexical keyword matching |

Paths are resolved relative to the config file's location.

---

## Prerequisites

- **Python 3.10+**
- **One embedding API key**: `GOOGLE_API_KEY` (Gemini, free tier) or `OPENAI_API_KEY`
- **Markdown notes** with YAML frontmatter (at minimum: an ID field and a `status` field)
- **No other dependencies** — YAML parsing, tokenization, cosine similarity are all stdlib

---

## Architecture

### Two types of retrieval objects

**Document cards** (one per note):
- Built from YAML frontmatter fields + configurable `##` sections from the note body
- Captures what each document is about at a high level

**Section summaries** (one per `##`/`###` heading in source documents):
- First 500 characters embedded for semantic search
- Full text stored for lexical keyword search
- Enables finding documents where the relevant content is in a specific section

### Embedding backends

**Primary**: Google Gemini `embedding-2-preview` — multimodal, 8192 token input, free tier sufficient for hundreds of documents.

**Fallback**: OpenAI `text-embedding-3-large` — 3072 dims reducible to 768. Used automatically if Gemini fails, with an explicit warning printed to stderr. The system never silently switches backends.

### Index format

A single JSON file — transparent, debuggable, no database dependency. Contains document cards with embeddings, section summaries with embeddings, and full section text for lexical search.

---

## FAQ

**Why not chunk-based RAG?**
Chunk-based RAG loses context at chunk boundaries, can hallucinate by combining chunks from different contexts, and provides no way to verify the source. This system uses embeddings only for *routing* — finding which documents to read. Claude then reads the complete source text, preserving full context.

**Why two embedding backends?**
Gemini `embedding-2-preview` is free and excellent. OpenAI is the fallback for users who already have an OpenAI key or when Gemini is unavailable. The system warns explicitly on fallback — it never silently switches.

**How do I add new documents?**
1. Create a markdown note in your `notes_dir/` with YAML frontmatter
2. Optionally add the full-text source in `sources_dir/[id]/[id].md`
3. Run `build_index.py --config lit-retrieval.yaml --incremental`

**How big can my collection be?**
Tested with 40 papers (~450 sections). The free Gemini tier handles this easily. For larger collections (1000+ documents), the index build takes longer but retrieval stays fast (it's just cosine similarity over vectors in memory).

**Does this work with Obsidian notes?**
Yes — as long as your notes have YAML frontmatter and `##` section headings. Obsidian-specific features like `[[wikilinks]]` are ignored by the retrieval system.

---

## License

MIT
