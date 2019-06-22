import json
import requests

def lookup_Region(system_id):
    response_const  = requests.get('http://esi.evetech.net/latest/universe/systems/' + str(system_id))

    data_system = response_const.json()
    const_id = data_system['constellation_id']

    response_const = requests.get('http://esi.evetech.net/latest/universe/constellations/' + str(const_id))

    data_const = response_const.json()
    region_id = data_const['region_id']

    response_region = requests.get('http://esi.evetech.net/latest/universe/regions/' + str(region_id))

    data_region = response_region.json()
    region_name = data_region['name']
    return region_name


def check_Hisec(system_id):
    response_system = requests.get('http://esi.evetech.net/latest/universe/systems/' + str(system_id))
    data_system = response_system.json()
    sec_status = data_system['security_status']
    if sec_status >= 0.5:
        return True



data = ' {"attackers":[{"alliance_id":1900696668,"character_id":1621368138,"corporation_id":98506105,"damage_done":432,"final_blow":true,"security_status":3.8,"ship_type_id":17738,"weapon_type_id":15963},{"alliance_id":1900696668,"character_id":173783471,"corporation_id":98506105,"damage_done":0,"final_blow":false,"security_status":0.4,"ship_type_id":35683,"weapon_type_id":527}],"killmail_id":77341138,"killmail_time":"2019-06-17T17:21:16Z","solar_system_id":30000142,"victim":{"alliance_id":99003214,"character_id":2114501736,"corporation_id":98169165,"damage_taken":432,"items":[],"position":{"x":346511379657.19,"y":27414349625.015,"z":-349607691561.16},"ship_type_id":670},"zkb":{"locationID":50001391,"hash":"5b220949b5c5958359c4b640255fc86e7aebb16f","fittedValue":10000,"totalValue":500110000,"points":1,"npc":true,"solo":false,"awox":false,"esi":"https:\/\/esi.evetech.net\/latest\/killmails\/77341138\/5b220949b5c5958359c4b640255fc86e7aebb16f\/","url":"https:\/\/zkillboard.com\/kill\/77341138\/"}}'


conv_data = json.loads(data)
zkill_url = conv_data['zkb']['url']
attackers = conv_data['attackers']
with open('ship_ids.json') as file:
    ship_ids = json.load(file)

print('Number of attackers: ' + str(len(attackers)))
global ship_list
ship_list = []
conv_data_2 = conv_data['attackers']
system_id = conv_data['solar_system_id']
fitted_v = conv_data['zkb']['fittedValue']
total_v = conv_data['zkb']['totalValue']
npc = conv_data['zkb']['npc']
print(npc)
if (total_v - fitted_v >= 500000000) and npc is True and check_Hisec(system_id) is True:
    print('Loot drop')

for item in conv_data['attackers']:
    conv_id = str(item['ship_type_id'])
    print(conv_id)
    if conv_id in ship_ids:
        ship_list.append(ship_ids[conv_id])
    if item['ship_type_id'] == 17738 and item['weapon_type_id'] in [15963, 14190, 14188, 15947] and lookup_Region(system_id) == 'Sinq Laison':
        ship_list.append('Smartbombing Machariel')



if len(ship_list) > 0:
    print(', '.join(ship_list) + ' spotted.\n' + zkill_url)
else:
    print(zkill_url)

print(system_id == 30002718)
print(system_id)


print(check_Hisec(system_id))
