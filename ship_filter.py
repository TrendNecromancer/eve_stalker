import json

data = ' {"attackers":[{"alliance_id":1900696668,"character_id":1621368138,"corporation_id":98506105,"damage_done":432,"final_blow":true,"security_status":3.8,"ship_type_id":22456,"weapon_type_id":2881},{"alliance_id":1900696668,"character_id":173783471,"corporation_id":98506105,"damage_done":0,"final_blow":false,"security_status":0.4,"ship_type_id":35683,"weapon_type_id":527}],"killmail_id":77341138,"killmail_time":"2019-06-17T17:21:16Z","solar_system_id":30001159,"victim":{"alliance_id":99003214,"character_id":2114501736,"corporation_id":98169165,"damage_taken":432,"items":[],"position":{"x":346511379657.19,"y":27414349625.015,"z":-349607691561.16},"ship_type_id":670},"zkb":{"locationID":50001391,"hash":"5b220949b5c5958359c4b640255fc86e7aebb16f","fittedValue":10000,"totalValue":10000,"points":1,"npc":false,"solo":false,"awox":false,"esi":"https:\/\/esi.evetech.net\/latest\/killmails\/77341138\/5b220949b5c5958359c4b640255fc86e7aebb16f\/","url":"https:\/\/zkillboard.com\/kill\/77341138\/"}}'


conv_data = json.loads(data)
zkill_url = conv_data['zkb']['url']
attackers = conv_data['attackers']
with open('ship_ids.json') as file:
    ship_ids = json.load(file)
print(zkill_url)
print('Number of attackers: ' + str(len(attackers)))
global ship_list
ship_list = []
conv_data_2 = conv_data['attackers']
for item in conv_data_2:
    conv_id = str(item['ship_type_id'])
    print(conv_id)
    if conv_id in ship_ids:
        ship_list.append(ship_ids[conv_id])
    if item['ship_type_id'] == 17738 and item['weapon_type_id'] in [15963, 14190, 14188, 15947]:
        ship_list.append('Smartbombing Machariel')

if len(ship_list) > 0:
    print(', '.join(ship_list) + ' spotted.\n' + zkill_url)
else:
    print(zkill_url)
