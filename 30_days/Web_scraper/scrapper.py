from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

#adding csv functions
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

#set columns in csv
writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " . " + author.text)
    #to write in cvs
    writer.writerow([quote.text, author.text])
    
#remember to close csv file
file.close()
    

#we combines the loop above using zip
#for author in authors:
#    print(author.text)