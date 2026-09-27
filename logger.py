# logger.py
import os
import logging

base_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(base_dir, "data/Final_project.log")
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
