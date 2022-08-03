'''
dollarAPI
=========

Get the value of a USD in Argentine Pesos.
'''

import requests
from bs4 import BeautifulSoup

class dollarAPI():
    def getDollarValue(self):
        '''
        Gets Dollar Value

        Pass a 0 to the method parameter to get the purchasing value, pass a 1 to get the selling value.
        '''
        purchaseValue = int(float(self.soup.select(".value")[0].text.strip('$')))
        sellingValue = int(float(self.soup.select(".value")[1].text.strip('$')))
        return {'compra': purchaseValue, 'venta': sellingValue}


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