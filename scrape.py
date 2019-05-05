import requests
from bs4 import BeautifulSoup as BeautifulSoup
from csv import writer
response = requests.get("https://www.newegg.com/Network-Print-Servers/SubCategory/ID-387?Tid=158135")
soup = BeautifulSoup(response.text, "html.parser")
containers = soup.findAll(class_="item-container")
print(containers)
