from dollarapi import blue, official
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hey! Please make a GET request to /official or /blue'

@app.route('/official')
def getOfficial():
    return official().getDollarValue()

@app.route('/blue')
def getBlue():
    return blue().getDollarValue()