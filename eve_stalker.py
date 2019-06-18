#!!/usr/bin/python3

import discord
import requests
import asyncio
import websockets
import json

client = discord.Client()

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



with open('ship_ids.json') as file:
    global ship_ids
    ship_ids = json.load(file)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await connect_Zkill_wss()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def connect_Zkill_wss():
        async with websockets.connect(
            'wss://zkillboard.com:2096') as websocket:
            name = ('{"action":"sub","channel":"killstream"}')

            await websocket.send(name)
            print('Requesting zkill stream..')
            zkill_channel = client.get_channel(589180865016365066)
            while True:
                response = await websocket.recv()
                conv_data = json.loads(response)
                ship_list = []
                system_id = conv_data['solar_system_id']
                zkill_url = conv_data['zkb']['url']
                print(zkill_url)
                try:
                    for item in conv_data['attackers']:
                        conv_id = str(item['ship_type_id'])
                        if conv_id in ship_ids:
                            ship_list.append(ship_ids[conv_id])
                        if item['ship_type_id'] == 17738 and item['weapon_type_id'] in [15963, 14190, 14188, 15947] and lookup_Region(system_id) not in {'Aridia','Catch'}:
                            ship_list.append('Smartbombing Machariel')
                except KeyError:
                    pass
                if len(ship_list) > 0:
                    await zkill_channel.send('@everyone\n \n' + ', '.join(ship_list) + ' spotted.\n' + zkill_url)
                await asyncio.sleep(0)
client.run('NTg5MDY5MDk0NzcxMjI4Njky.XQOTvA.BvSBGpO9KwMSTlu1Zk7oI1J3W5U')
