from logger import logging
from progress import load_progress,save_progress
from scraper import book_scraper
from Data_Base import save_to_db
from utils import save_to_csv,send_email
from config import OUTPUT_FILE
def main():
    logging.info("Main Function Started")
    start=load_progress()+1
    data=book_scraper(start)
    save_to_csv(data)
    send_email(OUTPUT_FILE,data)
    try:
        save_to_db(data)
    except Exception as e:
        print(f"Error in database = {e}")
    
if __name__ == "__main__":
    main()

