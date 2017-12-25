import requests
from bs4 import BeautifulSoup
import lxml

productlist = ['https://geizhals.at/apple-iphone-se-32gb-rosegold-a1597483.html?plz=&t=v&va=b&vl=at&hloc=at&v=e#filterform']
products = []

def transform_price(price):
     price = price.replace("€ ", "")
     price = price.replace("--", "00")
     price = price.replace(",", ".")
     price = float(price) * 100
     price = int(price)
     return price

for product in productlist:
    response = requests.get(product)
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.find_all('div', class_='offer offer--available')
    for row in rows:
        info = {}
        info['link'] = row.find('a', class_='gh_offerlist__offerurl ntd merchant').get('href')
        info['name']= row.find('span', class_='merchant__logo-caption').find('span', class_='notrans').text
        price = (row.find('div', class_='offer__price').find('span', class_='gh_price').text)
        info['price'] = transform_price(price)
        shippingPriceInfo = row.find('div', class_='offer__delivery-costs').find_all('span', class_='gh_price')
        priceNoShipping = shippingPriceInfo[0].text
        info['priceNoShipping'] = transform_price(priceNoShipping)
        shippingCosts = shippingPriceInfo[1].text
        info['shippingCosts'] = transform_price(shippingCosts) 
        #prices = soup.find_all
        products.append(info)
    print(products)

