#Importants
import discord
import asyncio
import os
import datetime


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

    #Simplification
    channel = message.channel
    author = message.author
    mention_author = message.author.mention
    adminID = '363627385838632961'
    adminName = 'Justice_Lion#1722'
    adminThumbnail = 'https://cdn.discordapp.com/avatars/363627385838632961/1cb72b10d3ab7625521cced6653f9235.png'
    BotName = 'Troll#3030'
    BotID = '561168512425656330'
    BotThumbnail = 'https://cdn.discordapp.com/avatars/561168512425656330/1b7d47e5ae9c643ac2f83b3d66a597a2.png'

    #Help
    if message.content.startswith('/트롤봇'):
        print('{} : /트롤봇'.format(author))
        embed = discord.Embed(color=0xea0000)
        embed.set_author(name='Troll Bot', icon_url=BotThumbnail)
        embed.add_field(name='봇 이름', value=BotName, inline=True)
        embed.add_field(name='가입일', value='2019년 03월 30일', inline=True)
        embed.add_field(name='봇 ID', value=BotID, inline=True)
        embed.add_field(name='사용법', value='채팅창에 /명령어 를 입력해주세요!', inline=False)
        embed.set_thumbnail(url=BotThumbnail)
        embed.set_footer(text='Made by Justice_Lion', icon_url=adminThumbnail)
        await client.send_message(channel, '{}'.format(mention_author))
        await client.send_message(channel, embed=embed)
        print(BotName + ' : {}, '.format(author) + '트롤봇 embed')

    #Admin
    if message.content.startswith('/관리자'):
        print('{} : /관리자'.format(author))
        if message.author.id == adminID:
            embed = discord.Embed(color=0xea0000)
            embed.set_author(name='Troll Bot',
                             icon_url=BotThumbnail)
            embed.add_field(name=':information_source: [관리자 명령어 목록]',
                            value='아래는 트롤봇의 관리자 전용 명령어 목록입니다.\n```\n/말해 <메시지>\n```',
                            inline=False)
            embed.set_footer(text='Made by Justice_Lion',
                             icon_url=adminThumbnail)
            await client.send_message(channel, '{}'.format(mention_author))
            await client.send_message(channel, embed=embed)
            print(BotName + ' : {}, 관리자 명령어 embed'.format(author))
        else:
            date = datetime.datetime.utcfromtimestamp(((int(adminID) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0xc354f7)
            embed.add_field(name='닉네임', value=adminName, inline=True)
            embed.add_field(name='가입일', value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일', inline=True)
            embed.add_field(name='아이디', value=adminID, inline=True)
            embed.set_thumbnail(url=adminThumbnail)
            await client.send_message(channel, '{}, 관리자 정보입니다.'.format(mention_author))
            await client.send_message(channel, embed=embed)
            print(BotName + ' : {}, 관리자 embed'.format(author))


#Background Task
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)