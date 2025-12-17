import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OpenAI_API_KEY = os.environ.get("")

# EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")
#
# LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
# FAISS_INDEX_PATH = os.environ.get("FAISS_INDEX_PATH", "app/vector_store/faiss_index.bin")
# DOCS_STORE_PATH = os.environ.get("DOCS_STORE_PATH", "app/vector_store/docs_store.pickle")

if not OpenAI_API_KEY:
    raise RuntimeError("OpenAI_API_KEY environment variable is required. Set it before running")