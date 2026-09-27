import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time
from logger import logging
from config import BASE_URL,HEADER,TIMEOUT,DELAY,ATTEMPTS
from progress import save_progress
import json

def book_scraper(page):
    max_page=5
    data=[]
    try:
        while page<=max_page:
            if page==1:
                url=BASE_URL 
            else:
                url=f"{BASE_URL}catalogue/page-{page}.html"
            
            session=requests.session()
            for i in range(ATTEMPTS):
                response=session.get(url,headers=HEADER,timeout=TIMEOUT)
                if response.status_code == 200:
                    logging.info("Request Success!!")
                    break
                elif response.status_code == 403:
                    logging.warning("Blocked by website")
                    break
                elif response.status_code == 429:
                    logging.warning("Too many requests")
                    time.sleep(10)
                time.sleep(DELAY)
            soup=BeautifulSoup(response.text,"html.parser")
            products=soup.find_all("article",class_="product_pod")

            if not products:
                print("No more products.")
                break

            for product in products:
                name=product.h3.a["title"]

                price=product.find("p",class_="price_color").text
                price=price.replace("£","")

                star_class=product.find("p",class_="star-rating")["class"][1]
                star=star_class

                stock=product.find("p",class_="instock availability").text.strip()

                data.append({
                    "Name":name,
                    "Price": price,
                    "Rating": star,
                    "Availability": stock,
                    "Date":datetime.now().strftime("%Y-%m-%d")
                    }
                )
            save_progress(page)
            page=page+1
            next_btn=soup.find("li",class_="next")
            if not next_btn:
                print("Last page reached.Stopping")
                break
        
            
        return data
    except Exception as e:
        print(f"Error occured in scrapping:{e}")
        return []