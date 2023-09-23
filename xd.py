import requests
from bs4 import BeautifulSoup
import pandas as pd
from json import loads, dumps

#Website
web = "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
result = requests.get(web)  #Obtaining HTML page
content = result.text #Extracting text content from response "web"

#Arrays where the products, prices and ratings about the items in the page will we stored
dates = []
banks = []
buys = []
sells = []


#Object "soup" able to analyse HTML docs
soup = BeautifulSoup(content, features="html.parser") 

#This page have "a" elements, which inside have the information that we want to list (name, price and rating)
for tr in soup.findAll('tr', attrs={'letra-pequeña'}):
  #We want to obtain the div element that contains the class attribute with the value that indicates the information we want to extract
  date = tr.find('span')
  bank = tr.find('td', attrs={"views-field-views-conditional"})  
  buy = tr.find('td', attrs={"views-field-field-tasa-compra"})
  sell = tr.find('td', attrs={"views-field-field-tasa-venta"})
  
  #The text content extracted from each variable "name, price, rating" will be stored in their respective arrays
  dates.append(date.text.split())
  banks.append(bank.text.split())
  buys.append(buy.text.split())
  sells.append(sell.text.split())
  
#Now, create a data frame with the data of the arrays
df = pd.DataFrame({'Dates':dates,'Banks':banks,'Buys':buys,'Sells':sells})

#Export the data frame to a .csv doc
df.to_json('bank_prices.json', orient="index")
