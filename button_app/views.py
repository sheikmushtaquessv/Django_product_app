from django.http import HttpResponse
import csv
from django.shortcuts import render
from .scraper import scrape_data 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

def home(request):
    return render(request, 'button.html')

def scrape_data(request):
    # Write your web scraping code here
    # Return scraped data as a list of lists (each list representing a row)
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Names or Titles
    names = soup.find_all("a", class_="title")
    product_name = [i.text for i in names]

    # Prices
    prices = soup.find_all("h4", class_="price")
    prices_list = [i.text for i in prices]

    # Description
    desc = soup.find_all("p", class_="description")
    desc_list = [i.text for i in desc]

    # Reviews
    reviews = soup.find_all("p", class_="review-count")
    reviews_list = [i.text for i in reviews]

    # Add serial numbers
    serial_numbers = list(range(1, len(product_name) + 1))

    # Saving data in CSV
    df = pd.DataFrame({"SL.No": serial_numbers, "Product Name": product_name, "Prices": prices_list, "Description": desc_list, "Number of Reviews": reviews_list})
    csv_output = io.StringIO()
    df.to_csv(csv_output, index=False)
    csv_output.seek(0)

    # Return CSV as HttpResponse for download
    response = HttpResponse(csv_output, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products_details.csv'
    return response
 