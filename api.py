import blue
from flask import Flask
app = Flask(__name__)

class dollar:

    def blue():
        dollarJSON = {}
        dollarJSON['compra'] = blue.getPurchasingValue()
        dollarJSON['venta'] = blue.getSellingValue()
        return dollarJSON

    def official():
        dollarJSON = {}
        dollarJSON['compra'] = 458
        dollarJSON['venta'] = 8000
        return dollarJSON

@app.route('/')
def main():
    return 'Hey! Please make a GET request to /official or /blue'

@app.route('/official')
def getOfficial():
    return dollar.official()

@app.route('/blue')
def getBlue():
    return dollar.blue()

app.run()