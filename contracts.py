import requests
import json

response_contracts = response_const  = requests.get('https://esi.evetech.net/latest/contracts/public/10000002/?datasource=tranquility&page=1')

data_contracts = response_contracts.json()

print(data_contracts)
