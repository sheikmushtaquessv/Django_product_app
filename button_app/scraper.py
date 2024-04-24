# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    # Write your web scraping code here
    # Return scraped data as a list of lists (each list representing a row)
    url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r=requests.get(url)

    soup=BeautifulSoup(r.text,"html.parser")
    
    #Names or Titles
    names=soup.find_all("a",class_="title")
    product_name=[]
    
    for i in names:
        name=i.text
        product_name.append(name)
    print(product_name)

    #Prices
    prices=soup.find_all("h4",class_="price")
    prices_list=[]

    for i in prices:
        price=i.text
        prices_list.append(price)
    print(prices_list)

    #Description
    desc=soup.find_all("p",class_="description")
    desc_list=[]

    for i in desc:
        des=i.text
        desc_list.append(des)
    print(desc_list)

    #Reviews
    reviews=soup.find_all("p",class_="review-count")
    reviews_list=[]

    for i in reviews:
        rev=i.text
        reviews_list.append(rev)
    print(reviews_list)

    #saving data in csv
    df=pd.DataFrame({"Product Name":product_name,"Prices":prices_list,"Description":desc_list,"Number of Reviews":reviews_list})
    print(df)
    df.to_csv("products_details.csv")
