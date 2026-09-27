from logger import logging
from config import EMAIL ,RECEIVER_EMAIL , PASSWORD,OUTPUT_FILE
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

def send_email(file_name, data):
    try:
        sender=EMAIL
        receiver=RECEIVER_EMAIL
        password=PASSWORD

        msg=MIMEMultipart()
        msg["FROM"]=sender
        msg["TO"]=receiver
        msg["Subject"]="Scraped Books Using Bot"

        body=f"Scraped {len(data)} Books.\n\n"
        body += "=" * 40 + "\n"
        for book in data[:5]:
            body+=f"{book['Name']} - {book['Rating']} - ({book['Price']})\n"
            body += "-" * 40 + "\n"
        body += "=" * 40 + "\n"
        body += "\nFull report attached.\n\nRegards,\nBook Scraper Bot 🤖"
        msg.attach(MIMEText(body,"plain"))

        with open(file_name,"rb") as f:
            part=MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_name}",
        )

        msg.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender,password)
            server.send_message(msg)
        logging.info("Email sent with attachment!")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def save_to_csv(data):
    if not data:
        logging.info(f"No Data to save.")
        return
    df=pd.DataFrame(data)
    try:
        df.to_csv(OUTPUT_FILE,index=False)
        logging.info(f"Data saved to {OUTPUT_FILE} Successfully.")
    except Exception as e:
        logging.info(f"Error occured while saving File: {e}")