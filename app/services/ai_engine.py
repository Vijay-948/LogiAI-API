import os
import openai
from app.config import LLM_MODEL

openai.api_key = os.environ.get("OPENAI_API_KEY")

def synthesize_analysis(parsed_summary: dict, log_snippet: str, rag_matches: list) -> dict:
    """
    Send a prompt to OpenAI to produce final structured analysis.
    """
    # Build prompt
    prompt_parts = []
    prompt_parts.append("You are an expert Java backend engineer & SRE. Analyze logs and provide:")
    prompt_parts.append("1) Short list of detected error types (one line each).")
    prompt_parts.append("2) Likely root cause (concise).")
    prompt_parts.append("3) Concrete step-by-step fixes (ordered).")
    prompt_parts.append("4) Optional: Improvements and monitoring suggestions.\n")
    prompt_parts.append("Parsed summary:\n")
    prompt_parts.append(str(parsed_summary))
    prompt_parts.append("\nRelevant RAG documents (if any):\n")
    if rag_matches:
        for idx, (doc, score) in enumerate(rag_matches):
            prompt_parts.append(f"RAG doc {idx+1} (score {score}):\n{doc}\n")
    else:
        prompt_parts.append("No RAG matches found.\n")
    prompt_parts.append("\nLog snippet:\n")
    prompt_parts.append(log_snippet[:4000])  # cut large logs for prompt safety

    full_prompt = "\n".join(prompt_parts)

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for log analysis."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=800,
        temperature=0.0,
    )

    text = response['choices'][0]['message']['content'].strip()
    return {"analysis_text": text}
