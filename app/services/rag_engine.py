import os
import pickle
from typing import List, Tuple
import faiss
import numpy as np
import openai
from app.config import EMBEDDING_MODEL, FAISS_INDEX_PATH, DOCS_STORE_PATH

openai.api_key = os.environ.get("OPENAI_API_KEY")

def _embed_texts(texts: List[str]) -> List[List[float]]:
    # OpenAI embedding API (sync)
    resp = openai.Embedding.create(model=EMBEDDING_MODEL, input=texts)
    embs = [r['embedding'] for r in resp['data']]
    return embs

def build_or_load_index(doc_texts: List[str]) -> None:
    """
    Build FAISS index from a list of document strings, and save it.
    """
    # create embeddings
    embeddings = _embed_texts(doc_texts)
    dim = len(embeddings[0])
    xb = np.array(embeddings).astype('float32')
    index = faiss.IndexFlatL2(dim)
    index.add(xb)

    # save index and docs
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(DOCS_STORE_PATH, "wb") as f:
        pickle.dump(doc_texts, f)

def search(query: str, top_k: int = 3) -> List[Tuple[str, float]]:
    """
    Return top_k (doc_text, score) for the query.
    """
    if not os.path.exists(FAISS_INDEX_PATH) or not os.path.exists(DOCS_STORE_PATH):
        return []

    # embed query
    q_emb = _embed_texts([query])[0]
    xb = np.array([q_emb]).astype('float32')
    index = faiss.read_index(FAISS_INDEX_PATH)
    D, I = index.search(xb, top_k)
    with open(DOCS_STORE_PATH, "rb") as f:
        docs = pickle.load(f)
    results = []
    for idx, dist in zip(I[0], D[0]):
        if idx < len(docs):
            results.append((docs[idx], float(dist)))
    return results
