import discord
import aiohttp
import requests
import asyncio
import websocket
import websockets

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

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
            print(name)
            while True:
                response = await websocket.recv()
                print(response)
                await asyncio.sleep(1)
asyncio.run(connect_Zkill_wss())

client.run('NTg5MDY5MDk0NzcxMjI4Njky.XQOTvA.BvSBGpO9KwMSTlu1Zk7oI1J3W5U')
