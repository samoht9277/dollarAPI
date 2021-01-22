import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.dolarhoy.com/').text
soup = BeautifulSoup(url, 'html.parser')

def getSellingValue():
    sell = soup.find('div', {"class": "venta"})
    sell = sell.find('div', {"class": "val"}).text
    return int(sell.strip('$'))

def getPurchasingValue():
    purchase = soup.find('div', {"class": "compra"})
    purchase = purchase.find('div', {"class": "val"}).text
    return int(purchase.strip('$'))
