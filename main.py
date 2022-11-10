import requests
from bs4 import BeautifulSoup
import csv


title_list=[]
price_list=[]

#Put your Url here
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response=requests.get(url)

soup=BeautifulSoup(response.text,"lxml")

# boxes = soup.find_all("div",class_ ="col-sm-4 col-lg-4 col-md-4")
# print(len(boxes))

names=soup.find_all("a",class_="title")

for i in names:
    name=i.text
    title_list.append(name.strip())


prices=soup.find_all("h4",class_="pull-right price")

for i in prices:
    pric=i.text
    price_list.append(pric.strip())


file_name="data.csv"

with open(file_name, "w" , encoding="utf-8") as f:
    f.write=csv.writer(f)
    f.write.writerow(['No','Name','Price ($)'])

    for i in range(len(price_list)):
        f.write.writerow([i+1,title_list[i],price_list[i]])