import json

data = '{"attackers":[{"alliance_id":99004901,"character_id":92242536,"corporation_id":98589200,"damage_done":16142,"final_blow":true,"security_status":4.4,"ship_type_id":23757,"weapon_type_id":23061},{"alliance_id":99004901,"character_id":92372597,"corporation_id":573400667,"damage_done":2186,"final_blow":false,"security_status":-9.9,"ship_type_id":33818,"weapon_type_id":1877},{"alliance_id":99004901,"character_id":92277365,"corporation_id":98589200,"damage_done":515,"final_blow":false,"security_status":-9.8,"ship_type_id":17715,"weapon_type_id":27371}],"killmail_id":77284866,"killmail_time":"2019-06-14T18:55:34Z","solar_system_id":30004977,"victim":{"alliance_id":99008879,"character_id":2115101036,"corporation_id":98575483,"damage_taken":18843,"items":[{"flag":87,"item_type_id":15508,"quantity_dropped":3,"singleton":0},{"flag":28,"item_type_id":17482,"quantity_dropped":1,"singleton":0},{"flag":20,"item_type_id":6001,"quantity_dropped":1,"singleton":0},{"flag":5,"item_type_id":25,"quantity_dropped":1,"singleton":0},{"flag":5,"item_type_id":33475,"quantity_destroyed":1,"singleton":0},{"flag":5,"item_type_id":33475,"quantity_dropped":1,"singleton":0},{"flag":5,"item_type_id":33474,"quantity_destroyed":1,"singleton":0},{"flag":12,"item_type_id":8748,"quantity_destroyed":1,"singleton":0},{"flag":94,"item_type_id":32043,"quantity_destroyed":1,"singleton":0},{"flag":19,"item_type_id":444,"quantity_destroyed":1,"singleton":0},{"flag":27,"item_type_id":17482,"quantity_dropped":1,"singleton":0},{"flag":93,"item_type_id":32043,"quantity_destroyed":1,"singleton":0},{"flag":11,"item_type_id":8748,"quantity_destroyed":1,"singleton":0},{"flag":92,"item_type_id":32043,"quantity_destroyed":1,"singleton":0}],"position":{"x":-1661303047065.2,"y":185546956714.25,"z":-448129466296.66},"ship_type_id":17480},"zkb":{"locationID":40315164,"hash":"543b230b790fd9387b1d140e3a6870dd535863d7","fittedValue":15991731.69,"totalValue":36931745.66,"points":1,"npc":false,"solo":false,"awox":false,"esi":"https:\/\/esi.evetech.net\/latest\/killmails\/77284866\/543b230b790fd9387b1d140e3a6870dd535863d7\/","url":"https:\/\/zkillboard.com\/kill\/77284866\/"}}'

conv_data = json.loads(data)
zkill_url = conv_data['zkb']['url']
attackers = conv_data['attackers']
print(zkill_url)
print('Number of attackers: ' + str(len(attackers)))
global ship_list
ship_list = []
for item in conv_data['attackers']:
    if item['ship_type_id'] == 33818:
        ship_list.append('Orthrus')
    if item['ship_type_id'] == 11198:
        ship_list.append('Stiletto')
print(len(ship_list))
if len(ship_list) > 0:
    print(', '.join(ship_list) + ' spotted.\n' + zkill_url)
else:
    print(zkill_url)
add = []
add.append(1)
print(len(add))
value = 15
boole = value in [12, 13, 14, 15]
print(boole)