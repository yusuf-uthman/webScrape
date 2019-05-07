#import necessary libraries
import requests
from bs4 import BeautifulSoup as soup
from csv import writer
response = requests.get("https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&IsNodeId=1&bop=And&Depa=1&Category=38&PageSize=96&order")
#parsing the html of te page
page_soup = soup(response.text, "html.parser")
#Grabs each product 
containers = page_soup.findAll(class_="item-info")
#creates a file to write the scraped info
file_name = "products2.csv"
#open the file to write scraped info
f = open(file_name, "w")
#created headers for the dataset
headers = "brand, product_name, price, shipping \n"
f.write(headers)
#creates a loop that iterates through every div with a class of "item-info" to get the data we need 
for container in containers:
    #grabs the brand name
    brand = container.div.a.img["title"] 
    #grabs the product name
    container_name = container.findAll("a", class_="item-title")
    product = container_name[0].get_text()
    #grabs each price
    price_container = container.findAll("li", class_="price-current")
    price = price_container[0].strong.text
    #grabs the shipping amount
    shipping_container = container.findAll("li", class_="price-ship")
    shipping = shipping_container[0].get_text().strip()
    #writes each line of product information in the file
    f.write(brand +","+ product.replace(",","|") + ","+ price + "," + shipping + "\n")
f.close()
