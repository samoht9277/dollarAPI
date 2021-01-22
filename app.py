from flask import Flask, request
from dollarapi import blue, official

app = Flask(__name__)

class dollar():
    def valueOf(currency): # Polimorphism :D
        dollarJSON = {}
        dollarJSON['compra'] = currency.getDollarValue(0)
        dollarJSON['venta'] = currency.getDollarValue(1)
        return dollarJSON

@app.route('/')
def main():
    return 'Hey! Please make a GET request to /official or /blue'

@app.route('/official')
def getOfficial():
    return dollar.valueOf(official())

@app.route('/blue')
def getBlue():
    return dollar.valueOf(blue())
    
app.run(host='0.0.0.0')