import requests
from bs4 import BeautifulSoup
import pandas as pd
from json import loads, dumps

#Website
web = "https://www.bcv.org.ve/"
result = requests.get(web)  #Obtaining HTML page
content = result.text #Extracting text content from response "web"

#Arrays where the products, prices and ratings about the items in the page will we stored
names = []
prices = []

#Object "soup" able to analyse HTML docs
soup = BeautifulSoup(content, features="html.parser") 

#This page have "a" elements, which inside have the information that we want to list (name, price and rating)
for div in soup.findAll('div', attrs={'row recuadrotsmc'}):
  #We want to obtain the div element that contains the class attribute with the value that indicates the information we want to extract
  name=div.find('span')
  price=div.find('strong')
  
  #The text content extracted from each variable "name, price, rating" will be stored in their respective arrays
  names.append(name.text)
  prices.append(price.text)

#Now, create a data frame with the data of the arrays
df = pd.DataFrame({'Name':names, 'Price':prices})

#Export the data frame to a .csv doc
result = df.to_json('coins.json',orient = 'records', lines=True) 
parsed =loads(result)
dumps(parsed, indent=4)