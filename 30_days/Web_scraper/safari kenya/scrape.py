from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.google.com/maps/search/safari+kenya/@-0.9640955,35.9916956,9z/data=!3m1!4b1?entry=ttu")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

