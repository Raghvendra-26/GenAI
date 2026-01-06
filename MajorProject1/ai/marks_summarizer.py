import requests
from typing import List, Dict
from core.marks_ops import calculate_marks_summary

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"


def validate_marks_for_ai(marks):
    if not isinstance(marks, list) or len(marks) == 0:
        raise ValueError("No marks to summarize")

    if len(marks) < 2:
        raise ValueError("Not enough data for summarization")

    return marks


def validate_marks_ai_output(text: str) -> str:
    if not text or not text.strip():
        raise RuntimeError("Empty AI response")
    
    refusal_markers = [
        "i can't",
        "i cannot",
        "i'm unable",
        "as an ai",
        "i can’t"
    ]
    
    for marker in refusal_markers:
        if marker in text.lower():
            raise RuntimeError("AI refusal detected")
        
    cleaned = text.strip()

    if cleaned.startswith("{") or cleaned.startswith("["):
        raise RuntimeError("JSON output not allowed")

    if len(text.split()) < 8:
        raise RuntimeError("AI output too short")

    return text.strip()


def fallback_summary(marks: List[Dict]) -> str:
    total,avg = calculate_marks_summary(marks)
    return (
        f"The dataset contains {len(marks)} records. "
        f"Average marks is {int(avg)} marks. "
        f"Total marks is {int(total)} marks"
    )
    

def summarize_marks(marks: List[Dict]) -> str:
    try:
        marks = validate_marks_for_ai(marks)
    except ValueError as e:
        return f"Invalid input: {e}"

    mark_text = "\n".join(
        f"- {u['name']} ({u['score']} marks)"
        for u in marks
    )
    
    total,avg = calculate_marks_summary(marks)

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a strict summarization engine.\n"
                    "Rules:\n"
                    "- Do NOT refuse\n"
                    "- Do NOT mention policies\n"
                    "- Do NOT add explanations\n"
                    "- Respond in a single short paragraph\n"
                    "- Do NOT use line breaks or headings\n"
                    "- DO NOT calculate or derive numbers\n"
                    "- Use ONLY the statistics explicitly provided\n"
                    "- If statistics are missing, respond with: SUMMARY_NOT_POSSIBLE\n"
                    "- If summarization is impossible, respond ONLY with: SUMMARY_NOT_POSSIBLE"
                )
            },
            {
                "role": "user",
                "content": (
                    f"""This is SAMPLE application data for testing.

                    Pre-calculated statistics (do NOT modify or recompute):
                    - Total marks: {total}
                    - Average marks: {avg}

                    Using ONLY the statistics above, write a neutral single-paragraph summary
                    under 60 words. Do not explain calculations.
                    Context:
                    <mark_text>"""
                )
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=15
        )
        response.raise_for_status()
        data = response.json()

        ai_text = data.get("message", {}).get("content", "")
        ai_text = validate_marks_ai_output(ai_text)
        
        if "\n" in ai_text:
            raise RuntimeError("Multi-line output not allowed")


        if ai_text == "SUMMARY_NOT_POSSIBLE":
            raise RuntimeError("AI returned sentinel")

        return ai_text

    except Exception as e:
        # 🔒 ZERO FAILURE GUARANTEE
        return fallback_summary(marks)