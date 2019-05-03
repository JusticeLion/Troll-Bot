#Importants
import discord
import asyncio
import os


@client.event
async def on_ready():
    print('[Login]')
    print('Bot Name :', client.user.name)
    print('Bot ID :', client.user.id)
    print("==============================")


#Simplification
client = discord.Client()


#Events
@client.event
async def on_message(message):
    
    #Help
    if message.content.startswith('/트롤봇'):
        await client.send_message(channel, '현재 깃허브 테스트 중입니다.')


#Background Task
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
