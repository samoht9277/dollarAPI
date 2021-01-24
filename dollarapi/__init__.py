'''
dollarAPI
========

Get the value of a USD in Argentine Pesos.
'''

import requests
from bs4 import BeautifulSoup

class dollarAPI():
    def getDollarValue(self, method):
        '''
        Gets Dollar Value

        Pass a 0 to the method parameter to get the purchasing value, pass a 1 to get the selling value.
        '''
        value = self.soup.find('div', {"class": "tile is-parent is-8"})
        value = self.soup.select(".value")[method].text
        return float(value.strip('$'))

class blue(dollarAPI):
    '''
    Dollar Blue Class
    ========
    '''
    req = requests.get('https://www.dolarhoy.com/cotizaciondolarblue').text
    soup = BeautifulSoup(req, 'lxml')

class official(dollarAPI):
    '''
    Dollar Official Class
    ========
    '''
    req = requests.get('https://www.dolarhoy.com/cotizaciondolaroficial').text
    soup = BeautifulSoup(req, 'lxml')