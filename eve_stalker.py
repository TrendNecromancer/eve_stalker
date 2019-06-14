import discord
import requests
import asyncio
import websockets
import json

client = discord.Client()

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
            while True:
                response = await websocket.recv()
                global data
                data = json.loads(response)
                zkill_url = data['zkb']['url']
                print(zkill_url)
                zkill_channel = client.get_channel(589180865016365066)
                await zkill_channel.send(zkill_url)
                await asyncio.sleep(0)
client.run('NTg5MDY5MDk0NzcxMjI4Njky.XQOTvA.BvSBGpO9KwMSTlu1Zk7oI1J3W5U')


