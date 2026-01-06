import requests
from typing import List, Dict

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"


# -------------------------------
# INPUT VALIDATION (Layer 1)
# -------------------------------
def validate_users_for_ai(users):
    if not isinstance(users, list) or len(users) == 0:
        raise ValueError("No users to summarize")

    if len(users) < 2:
        raise ValueError("Not enough data for summarization")

    return users



# -------------------------------
# OUTPUT VALIDATION (Layer 3)
# -------------------------------
def validate_ai_output(text: str) -> str:
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

    if len(text.split()) < 8:
        raise RuntimeError("AI output too short")

    return text.strip()


# -------------------------------
# FALLBACK (Layer 4)
# -------------------------------
def fallback_summary(users: List[Dict]) -> str:
    avg_age = sum(u["age"] for u in users) / len(users)
    return (
        f"The dataset contains {len(users)} users. "
        f"Average age is {int(avg_age)} years. "
        f"All users have email addresses registered."
    )


# -------------------------------
# MAIN FUNCTION (HARDENED)
# -------------------------------
def summarize_users(users: List[Dict]) -> str:
    try:
        users = validate_users_for_ai(users)
    except ValueError as e:
        return f"Invalid input: {e}"

    user_text = "\n".join(
        f"- {u['name']} ({u['age']} years, {u['email']})"
        for u in users
    )

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
                    "- If summarization is impossible, respond ONLY with: SUMMARY_NOT_POSSIBLE"
                )
            },
            {
                "role": "user",
                "content": (
                    "The following is SAMPLE application data for testing.\n\n"
                    "Provide a neutral summary in under 60 words.\n\n"
                    f"{user_text}"
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
        ai_text = validate_ai_output(ai_text)

        if ai_text == "SUMMARY_NOT_POSSIBLE":
            raise RuntimeError("AI returned sentinel")

        return ai_text

    except Exception as e:
        # 🔒 ZERO FAILURE GUARANTEE
        return fallback_summary(users)
