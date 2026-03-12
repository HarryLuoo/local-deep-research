"""
embedding_provider.py
---------------------
Thin abstraction over embedding backends for local document retrieval.

Primary: Google Gemini embedding-2-preview (March 2026, multimodal, 8192 token input)
Fallback: OpenAI text-embedding-3-large (3072 dims, reducible)

The embedding provider is ONLY used for routing (finding relevant documents).
It is NOT the evidence source — final answers come from full-text reading.
"""

import os
import sys
import math
from pathlib import Path
from abc import ABC, abstractmethod

# Load .env from current working directory
_env_file = Path.cwd() / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _key, _val = _line.split("=", 1)
            if _val.strip():
                os.environ.setdefault(_key.strip(), _val.strip())


class EmbeddingProvider(ABC):
    """Base class for embedding backends."""

    @abstractmethod
    def embed(self, texts: list[str], task_type: str = "RETRIEVAL_DOCUMENT") -> list[list[float]]:
        """Embed a list of texts. Returns one embedding vector per text."""
        ...

    @abstractmethod
    def model_name(self) -> str:
        """Return the model identifier string."""
        ...


class GeminiProvider(EmbeddingProvider):
    """Google Gemini embedding-2-preview backend."""

    MODEL = "models/gemini-embedding-2-preview"

    def __init__(self, dims: int = 768):
        import google.generativeai as genai

        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("No GOOGLE_API_KEY or GEMINI_API_KEY found in environment")
        genai.configure(api_key=api_key)
        self._genai = genai
        self._dims = dims

    def model_name(self) -> str:
        return self.MODEL

    def embed(self, texts: list[str], task_type: str = "RETRIEVAL_DOCUMENT") -> list[list[float]]:
        # Gemini embed_content accepts a list of texts
        # Batch in groups to stay under 20K token budget per request
        all_embeddings = []
        batch_size = 10  # conservative batch size
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            result = self._genai.embed_content(
                model=self.MODEL,
                content=batch,
                task_type=task_type,
                output_dimensionality=self._dims,
            )
            # embed_content returns {'embedding': [[...], ...]} for batch, {'embedding': [...]} for single
            emb = result["embedding"]
            if emb and isinstance(emb[0], list):
                all_embeddings.extend(emb)
            else:
                all_embeddings.append(emb)
        return all_embeddings


class OpenAIProvider(EmbeddingProvider):
    """OpenAI text-embedding-3-large fallback backend."""

    MODEL = "text-embedding-3-large"

    def __init__(self, dims: int = 768):
        from openai import OpenAI

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("No OPENAI_API_KEY found in environment")
        self._client = OpenAI(api_key=api_key)
        self._dims = dims

    def model_name(self) -> str:
        return self.MODEL

    def embed(self, texts: list[str], task_type: str = "RETRIEVAL_DOCUMENT") -> list[list[float]]:
        # OpenAI doesn't use task_type — it's symmetric
        # Batch in groups of 20 (API limit is 2048 but let's be conservative)
        all_embeddings = []
        batch_size = 20
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            response = self._client.embeddings.create(
                model=self.MODEL,
                input=batch,
                dimensions=self._dims,
            )
            all_embeddings.extend([d.embedding for d in response.data])
        return all_embeddings


def get_provider(backend: str = None, dims: int = 768) -> EmbeddingProvider:
    """
    Get an embedding provider. Tries Gemini first, falls back to OpenAI.

    Args:
        backend: "gemini" or "openai". If None, reads EMBEDDING_BACKEND env var,
                 defaults to "gemini".
        dims: Output embedding dimensions (default 768).

    Returns:
        An EmbeddingProvider instance.

    Raises:
        RuntimeError if no backend can be initialized.
    """
    backend = backend or os.environ.get("EMBEDDING_BACKEND", "gemini").lower()

    if backend == "gemini":
        try:
            return GeminiProvider(dims=dims)
        except Exception as e:
            print(
                f"WARNING:  Gemini embedding-2-preview unavailable: {e}\n"
                f"    Falling back to OpenAI text-embedding-3-large.",
                file=sys.stderr,
            )
            try:
                return OpenAIProvider(dims=dims)
            except Exception as e2:
                raise RuntimeError(
                    f"Both embedding backends failed.\n"
                    f"  Gemini: {e}\n"
                    f"  OpenAI: {e2}\n"
                    f"Set GOOGLE_API_KEY or OPENAI_API_KEY in .env"
                ) from e2

    elif backend == "openai":
        print(
            "WARNING:  Using OpenAI text-embedding-3-large (not Gemini embedding-2-preview).",
            file=sys.stderr,
        )
        return OpenAIProvider(dims=dims)

    else:
        raise ValueError(f"Unknown embedding backend: {backend!r}. Use 'gemini' or 'openai'.")


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


if __name__ == "__main__":
    # Quick smoke test
    provider = get_provider()
    print(f"Backend: {provider.model_name()}")
    embeddings = provider.embed(["test embedding for document retrieval"])
    print(f"Dims: {len(embeddings[0])}")
    print(f"First 5 values: {embeddings[0][:5]}")
