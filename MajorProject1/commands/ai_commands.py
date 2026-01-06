from storage.json_store import load_json
from ai.user_summarizer import summarize_users
from ai.marks_summarizer import summarize_marks
from utils.logger import logger

file_path1 = "data/users.json"
file_path2 = "data/marks.json"


def summarize_users_command():
    users = load_json(file_path1)

    try:
        summary = summarize_users(users)
    except Exception as e:
        logger.error(f"AI summarization failed: {e}")
        return

    logger.info("User Summary generated")
    print(summary)
    
    
def summarize_marks_command():
    marks = load_json(file_path2)

    try:
        summary = summarize_marks(marks)
    except Exception as e:
        logger.error(f"AI summarization failed: {e}")
        return
    
    logger.info("Marks summary generated")
    print(summary)