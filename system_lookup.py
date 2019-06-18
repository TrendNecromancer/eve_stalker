import requests
import json

system_id = 30002718

response_const  = requests.get('http://esi.evetech.net/latest/universe/systems/' + str(system_id))

data_system = response_const.json()
const_id = data_system['constellation_id']

response_const = requests.get('http://esi.evetech.net/latest/universe/constellations/' + str(const_id))

data_const = response_const.json()
region_id = data_const['region_id']

response_region = requests.get('http://esi.evetech.net/latest/universe/regions/' + str(region_id))

data_region = response_region.json()
region_name = data_region['name']

print(region_name)
