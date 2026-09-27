import json
from config import PROGRESS_FILE
from logger import logging
def load_progress():
    try:
        with open(PROGRESS_FILE) as f:
            data = json.load(f)
            return data["last_page"]

    except:
        return 0

def save_progress(page):
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump({"last_page": page}, f)
            logging.info(f"Last Page Scraped = {page}")
    except Exception as e:
        logging.error(f"Error in Saving Page progress : {e}")

