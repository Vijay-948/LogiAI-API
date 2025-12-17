import re
from typing import Dict, List

STACKTRACE_START = re.compile(r'^\s*Exception|^\s*java\.lang|^\s*Traceback', re.IGNORECASE)

def extract_error_lines(log_text: str) -> List[str]:
    lines = log_text.splitlines()
    errors = [ln for ln in lines if re.search(r'\b(ERROR|FATAL|CRITICAL|Exception|Traceback)\b', ln, re.IGNORECASE)]
    return errors

def extract_stacktraces(log_text: str) -> List[str]:
    lines = log_text.splitlines()
    stacktraces = []
    i = 0
    while i < len(lines):
        if STACKTRACE_START.search(lines[i]):
            block = [lines[i]]
            i += 1
            # gather until blank line or next timestamp-like line
            while i < len(lines) and lines[i].strip() != "":
                block.append(lines[i])
                i += 1
            stacktraces.append("\n".join(block))
        else:
            i += 1
    return stacktraces

def summarize_errors(log_text: str) -> Dict:
    errors = extract_error_lines(log_text)
    traces = extract_stacktraces(log_text)
    # simple frequency of error messages
    freq = {}
    for e in errors:
        key = e.strip()
        freq[key] = freq.get(key, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_errors = [{"message": k, "count": v} for k, v in sorted_freq[:10]]
    return {
        "errors_count": len(errors),
        "top_errors": top_errors,
        "stacktraces_found": len(traces),
        "stacktraces": traces[:5]  # return up to 5 stacktraces for speed
    }
