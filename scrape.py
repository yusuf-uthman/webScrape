#import necessary libraries
import requests
from bs4 import BeautifulSoup as soup
from csv import writer
response = requests.get("https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38")
#parsing the html of te page
page_soup = soup(response.text, "html.parser")
#Grabs each product 
containers = page_soup.findAll(class_="item-info")

file_name = "products.csv"
f = open(file_name, "w")

headers = "brand, product_name, shipping \n"
f.write(headers)

for container in containers:
    brand = container.div.a.img["title"] 
    
    container_name = container.findAll("a", class_="item-title")
    product = container_name[0].get_text()
    
    shipping_container = container.findAll("li", class_="price-ship")
    shipping = shipping_container[0].get_text().strip()

    f.write(brand +","+ product.replace(",","|") + "," + shipping + "\n")
f.close()
