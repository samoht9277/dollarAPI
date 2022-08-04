from flask import Flask
from requests import get
from bs4 import BeautifulSoup

def getDollarValue(url):
    req = get(url).text
    soup = BeautifulSoup(req, 'lxml')
    purchaseValue = int(float(soup.select(".value")[0].text.strip('$')))
    sellingValue = int(float(soup.select(".value")[1].text.strip('$')))
    return {'compra': purchaseValue, 'venta': sellingValue}

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hey! Please make a GET request to /official or /blue'

@app.route('/official')
def getOfficial():
    return getDollarValue("https://www.dolarhoy.com/cotizaciondolaroficial")

@app.route('/blue')
def getBlue():
    return getDollarValue("https://www.dolarhoy.com/cotizaciondolarblue")