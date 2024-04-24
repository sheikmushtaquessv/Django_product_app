#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mushtaque.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


from django.http import HttpResponse
from django.shortcuts import render
import csv
from .scraper import scrape_data  # Assuming you have a scraper function in scraper.py

def scrape_and_download(request):
    data = scrape_data()  # Call your web scraping function
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prouducts_details.csv"'

    # writer = csv.writer(response)
    # for row in data:
    #     writer.writerow(row)

    return response