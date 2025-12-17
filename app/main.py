from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from typing import List
import os
import pickle

from app.utils.file_utils import save_uploaded_file
from app.services import log_parser, rag_engine, ai_engine
from app.schemas.log_request import LogRequest, LogResponse
from app.config import FAISS_INDEX_PATH
from app.config import EMBEDDING_MODEL, LLM_MODEL

app = FastAPI(title="AI Log Analyzer")

# Health
@app.get("/health")
def health():
    return {"status": "healthy"}

# Simple models endpoint
# @app.get("/models")
# def models():
#     return {"embedding_model": os.environ.get("EMBEDDING_MODEL"), "llm_model": os.environ.get("LLM_MODEL")}

@app.get("/models")
def models():
    return {
        "embedding_model": EMBEDDING_MODEL,
        "llm_model": LLM_MODEL,
    }


# Analyze full log: uses parser, rag search, and LLM synthesis
@app.post("/analyze-log")
async def analyze_log(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    parsed = log_parser.summarize_errors(text)

    # get RAG matches for top errors (if index exists)
    rag_matches = []
    if parsed.get("top_errors"):
        # search using the most common error messages
        top_msgs = [e["message"] for e in parsed["top_errors"]][:3]
        for msg in top_msgs:
            matches = rag_engine.search(msg, top_k=2)
            rag_matches.extend(matches)

    ai_result = ai_engine.synthesize_analysis(parsed, text[:8000], rag_matches)

    return {
        "parsed_summary": parsed,
        "rag_matches_count": len(rag_matches),
        "ai_analysis": ai_result
    }

# Extract only errors/warnings
@app.post("/extract-errors")
async def extract_errors(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    parsed = log_parser.summarize_errors(text)
    return parsed

# Generate fix suggestions from an error text (AI-only)
@app.post("/generate-fix")
def generate_fix(req: LogRequest):
    prompt_text = f"Error: {req.error}\nProvide: 1) root cause, 2) step-by-step fix, 3) monitoring suggestions."
    ai_out = ai_engine.synthesize_analysis({"note": "direct_error_input"}, prompt_text, [])
    return ai_out

# Upload KB files (simple: accept list of text files in form)
@app.post("/upload-knowledge-base")
async def upload_kb(files: List[UploadFile] = File(...)):
    saved_texts = []
    for f in files:
        content = await f.read()
        text = content.decode("utf-8", errors="ignore")
        saved_texts.append(text)

    # build FAISS index from these docs
    try:
        rag_engine.build_or_load_index(saved_texts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return LogResponse(uploaded_files=len(saved_texts), status="indexed")

# convenience: serve /docs root -> redirect to swagger UI (FastAPI already does /docs)
@app.get("/")
def root():
    return {"message": "AI Log Analyzer - open /docs for interactive API UI"}
