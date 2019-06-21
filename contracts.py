import requests
import json


def get_Contracts():
    page = 30
    response_contracts = requests.get('https://esi.evetech.net/latest/contracts/public/10000002/?datasource=tranquility&page=' + str(page))
    if response_contracts == '[]':
        --page
    else:
        break
        return response_contracts



data_contracts = response_contracts.json()

print(data_contracts)
