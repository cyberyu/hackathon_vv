__author__ = 'shiyu'

import requests


r = requests.post('http://54.173.193.196:5001/clsfy', data = {'textinput': ' want low risk.'})
print type(r)
print r.json()['y']