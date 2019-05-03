#Importants
import discord
import asyncio


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


#Background Task
client.run(TOKEN)