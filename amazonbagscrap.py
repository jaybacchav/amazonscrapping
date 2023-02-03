import csv
import requests
from bs4 import BeautifulSoup

name = []
price = []
rating = []
urls = []
reviews = []
asin = []
description = []

pages = list(range(1, 21))
for page in pages:
    url = requests.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%252&page={}'.format(page)).text
    sp = BeautifulSoup(url, 'html.parser')

    for i in sp.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}):
        string = i.text
        name.append(string.strip())
    for each in name:
        print(each)

    for i in sp.find_all('span', 'a-price-whole'):
        price.append(i.text)
    for each1 in price:
        print(each1)

    for i in sp.find_all('span', 'a-icon-alt'):
        rating.append(i.text)
    for each2 in rating:
        print(each2)

    for i in sp.find_all('a'):
        urls.append(i.text)
        # print(i.get('href'))

    for i in sp.find_all('span','a-size-base s-underline-text'):
        reviews.append(i.text)
    for each3 in reviews:
        print(each3)

    for i in sp.find_all('div','data-asin'):
        asin.append(i.text)
    for each4 in asin:
        print(each4)

    for i in sp.find_all('div',{'id':'productDescription'}):
        description.append(i.text)
    for each4 in description:
        print(each4)

    with open('bag.csv','w',encoding="utf=8") as f:
        writer = csv.writer(f)
        writer.writerow(['Names','description','prices','rating','reviews','ASIN'])
        writer.writerow([name,description,price,rating,reviews,asin])