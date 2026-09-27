import sqlite3
from datetime import datetime
from logger import logging
from config import BOOKS_DB


def save_to_db(data):
    if not data:
        logging.info(f"No Data to save.")
        return
    try:
        conn=sqlite3.connect(BOOKS_DB)
        cursor=conn.cursor()
        cursor.execute("""create table if not exists books_db(         
                    Name text,
                    Price integr,
                    Rating text,
                    Availability text,
                    Date)""")
        # cursor.execute(
        #             "insert into books_db values (?,?,?,?,?)",(data['Name'],data['Price'],data['Rating'],data['Availability'],data['Date'])
        #         )
        cursor.executemany("""
        INSERT INTO books_db (Name, Price, Rating, Availability, Date) 
        VALUES (:Name, :Price, :Rating, :Availability, :Date)
    """, data)
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Error in saving data to Data Base : {e}")
