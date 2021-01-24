from dollarapi import blue, official
from flask import Flask, request
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
    
if __name__ == '__name__':
    app.run()