from dollarapi import blue, official
from flask import Flask, request
from flask_caching import Cache 

app = Flask(__name__)

CONFIG = {
    "CACHE_TYPE": "SimpleCache"
}

app.config.from_mapping(CONFIG)
cache = Cache(app)

class dollar():
    def valueOf(currency): # Polimorphism :D
        dollarJSON = {}
        dollarJSON['compra'] = currency.getDollarValue('compra')
        dollarJSON['venta'] = currency.getDollarValue('venta')
        return dollarJSON

@app.route('/')
def main():
    return 'Hey! Please make a GET request to /official or /blue'

@app.route('/official')
@cache.cached(timeout=300)
def getOfficial():
    return dollar.valueOf(official())

@app.route('/blue')
@cache.cached(timeout=300)
def getBlue():
    return dollar.valueOf(blue())
 
if __name__ == '__name__':
    app.run("0.0.0.0")