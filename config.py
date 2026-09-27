# config.py
import os
import random
from logger import base_dir
BASE_URL = "https://books.toscrape.com/"
EMAIL = "your_email"
RECEIVER_EMAIL="receiver_email"
PASSWORD = "your_password"
PROGRESS_FILE = os.path.join(base_dir, "data/progress.json")
BOOKS_DB=os.path.join(base_dir, "data/Books.db") 
OUTPUT_FILE =os.path.join(base_dir, "data/Scraped_Books.csv") 

DELAY=3
TIMEOUT=10
ATTEMPTS=3
AGENTS=["Mozilla/5.0 Windows Chrome",
    "Mozilla/5.0 Mac Safari",
    "Mozilla/5.0 Linux Firefox"]
HEADER = {
    "User-Agent": random.choice(AGENTS)
}