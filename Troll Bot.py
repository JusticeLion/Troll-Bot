#Imports
import discord
import asyncio
import openpyxl
import random
import datetime
import bs4
import urllib
import urllib.request
import logging
import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from discord import Member
from itertools import cycle
if not discord.opus.is_loaded():
     discord.opus.load_opus('opus')


#Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


#Simplification
client = discord.Client()


#Login
@client.event
async def on_ready():
    print('[Login]')
    print('Bot Name :', client.user.name)
    print('Bot ID :', client.user.id)
    print("==============================")


#Bot Status
status = ['트롤봇 온라인!', '채팅창에 /트롤봇 입력하여 사용']
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(4)


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

    #Command List
    if message.content.startswith('/명령어'):
        print('{} : /명령어'.format(author))
        embed = discord.Embed(color=0xea0000)
        embed.set_author(name='Troll Bot', icon_url=BotThumbnail)
        embed.add_field(name=':information_source: [트롤봇 명령어 목록]',
                        value='아래는 트롤봇의 명령어 목록입니다. 띄어쓰기를 꼭 맞춰주세요!\n```\n/골라 <단어1> <단어2> …\n/주사위\n/현재시간\n/날씨 <지역명>\n/실시간검색어 또는 /실검\n/나무위키 <검색어>\n/관심\n/시공조아 또는 /시공\n```',
                        inline=False)
        embed.set_footer(text='Made by Justice_Lion', icon_url=adminThumbnail)
        await client.send_message(channel, '{}'.format(mention_author))
        await client.send_message(channel, embed=embed)
        print(BotName + ' : {}, '.format(author) + '명령어 embed')

    #Choose One
    if message.content.startswith('/골라'):
        choice = message.content.split(' ')
        print('{} : /골라'.format(author) + str(choice))
        if len(choice)-1<2:
            await client.send_message(channel, '{}, 두 가지 이상의 단어를 입력해 주세요.'.format(mention_author))
            print(BotName + ' : {}, 두 가지 이상의 단어를 입력해 주세요.'.format(author))
        else:
            choicetext = random.randint(1, len(choice) - 1)
            choiceresult = choice[choicetext]
            await client.send_message(channel, '{}, '.format(mention_author) + str(choiceresult))
            print(BotName + ' : {}, '.format(author) + str(choiceresult))

    #Dice
    if message.content.startswith('/주사위'):
        print('{} : /주사위'.format(author))
        dice = random.randint(1,6)
        if dice==1:
            await client.send_message(channel, '{}, :one:'.format(mention_author))
            print(BotName + ' : {}, 1'.format(author))
        if dice==2:
            await client.send_message(channel, '{}, :two:'.format(mention_author))
            print(BotName + ' : {}, 2'.format(author))
        if dice==3:
            await client.send_message(channel, '{}, :three:'.format(mention_author))
            print(BotName + ' : {}, 3'.format(author))
        if dice==4:
            await client.send_message(channel, '{}, :four:'.format(mention_author))
            print(BotName + ' : {}, 4'.format(author))
        if dice==5:
            await client.send_message(channel, '{}, :five:'.format(mention_author))
            print(BotName + ' : {}, 5'.format(author))
        if dice==6:
            await client.send_message(channel, '{}, :six:'.format(mention_author))
            print(BotName + ' : {}, 6'.format(author))

    #Current Time
    if message.content.startswith('/현재시간'):
        print('{} : /현재시간'.format(author))
        t = datetime.datetime.today()
        y = t.year
        m = t.month
        d = t.day
        h = t.hour
        mi = t.minute
        await client.send_message(channel, '{}, '.format(mention_author) + str(y) + '년 ' + str(m) + '월 ' + str(d) + '일 ' + str(h) + '시 ' + str(mi) + '분 입니다.')
        print(BotName + ' : {}, '.format(mention_author) + str(y) + '년 ' + str(m) + '월 ' + str(d) + '일 ' + str(h) + '시 ' + str(mi) + '분 입니다.')

    #Weather
    if message.content.startswith('/날씨'):
        loc = message.content.split(' ')[1]
        print('{} : /날씨'.format(author) + loc)
        sch = urllib.parse.quote(loc + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+sch
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, 'html.parser')
        todayBase = bsObj.find('div', {'class': 'main_info'})
        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()
        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()
        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp2 = todayFeelingTemp1.find('span', {'class': 'num'})
        todayFeelingTemp = todayFeelingTemp2.text.strip()
        todayDust1 = bsObj.find('div', {'class': 'sub_info'})
        todayDust2 = todayDust1.find('div', {'class': 'detail_box'})
        todayDust3 = todayDust2.find('dd')
        todayDust = todayDust3.text.strip()
        tomorrowBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()
        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()
        tomorrowAllFind = tomorrowBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfter = tomorrowAfter3.text.strip()
        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()
        embed = discord.Embed(color=0x03cf5d)
        embed.set_author(name='Troll Bot', icon_url=BotThumbnail)
        embed.add_field(name='현재 온도', value=todayTemp + '˚', inline=True)
        embed.add_field(name='체감 온도', value=todayFeelingTemp + '˚', inline=True)
        embed.add_field(name='현재 상태', value=todayValue, inline=False)
        embed.add_field(name='미세먼지', value=todayDust, inline=False)
        embed.add_field(name='내일 오전', value=tomorrowMoring + '˚, ' +  tomorrowValue, inline=False)
        embed.add_field(name='내일 오후', value=tomorrowAfter + '˚, ' +  tomorrowAfterValue, inline=False)
        embed.set_footer(text='NAVER 제공',
                         icon_url='https://lh3.googleusercontent.com/DjUgn0hqwzO0hw4NchiE4r66I5vutBFZQWsL0nct8gFTkzRhBIAZmyXPdtyzD4-hKGM=s180-rw')
        await client.send_message(channel, '{}, '.format(mention_author) + loc + '의 날씨정보입니다.')
        await client.send_message(channel, embed=embed)
        print(BotName + ' : {}, '.format(author) + loc + ' 날씨 embed')

    #Trending Topics
    if message.content.startswith('/실시간검색어') or message.content.startswith('/실검'):
        print('{} : /실시간검색어 or /실검'.format(author))
        url = 'https://www.naver.com/'
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, 'html.parser')
        Search1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        Search2 = Search1.find('ul', {'class': 'ah_l'})
        Search3 = Search2.find_all('li')
        embed = discord.Embed(color=0x03cf5d)
        embed.set_author(name='Troll Bot', icon_url=BotThumbnail)
        embed.set_footer(text='NAVER 제공',
                         icon_url='https://lh3.googleusercontent.com/DjUgn0hqwzO0hw4NchiE4r66I5vutBFZQWsL0nct8gFTkzRhBIAZmyXPdtyzD4-hKGM=s180-rw')
        for i in range(0, 5):
            Search4 = Search3[i]
            Search5 = Search4.find('span', {'class': 'ah_k'})
            Search = Search5.text.replace(' ','')
            sch = urllib.parse.quote(Search)
            SearchURL = 'https://search.naver.com/search.naver?ie=utf8&query='+sch
            embed.add_field(name=str(i+1) + '위', value='\n' + '[%s](<%s>)' % (Search, SearchURL), inline=False)
        await client.send_message(channel, '{}, 네이버 실시간 검색어 1~5위 목록입니다.'.format(mention_author))
        await client.send_message(channel, embed=embed)
        print(BotName + ' : {}, 실시간검색어 embed'.format(author))

    #NamuWiki
    if message.content.startswith('/나무위키'):
        txt = message.content[6:]
        print('{} : /나무위키 '.format(author) + txt)
        sch = urllib.parse.quote(txt)
        url = 'https://namu.wiki/w/'+sch
        embed = discord.Embed(color=0x13ad65)
        embed.set_author(name='Troll Bot', icon_url=BotThumbnail)
        embed.add_field(name='↓아래의 링크를 눌러주세요↓', value='[%s](<%s>)' % (txt, url), inline=False)
        embed.set_footer(text='나무위키 제공',
                         icon_url='http://mystartpage.kr/namu.png')
        await client.send_message(channel, '{}'.format(mention_author))
        await client.send_message(channel, embed=embed)
        print(BotName + ' : {}, '.format(author) + txt + ' 나무위키 링크 embed')

    #Reaction 1 (Attention Seeker)
    if message.content.startswith('/관심'):
        print('{} : /관심'.format(author))
        await client.send_message(channel, '{}'.format(mention_author))
        await client.send_file(channel, "image\Reaction\grandstander.jpg")
        print(BotName + ' : {}, image\Reaction\grandstander.jpg'.format(author))

    #Reaction 2 (HOS)
    if message.content.startswith('/시공') or message.content.startswith('/시공조아'):
        print('{} : /시공 or /시공조아'.format(author))
        i = random.randint(1,25)
        await client.send_message(channel, '{}'.format(mention_author))
        await client.send_file(channel, "image\Reaction\HOS\HOS (" + str(i) + ").gif")
        print(BotName + ' : {}, image\Reaction\HOS\HOS ('.format(author) + str(i) + ').gif')

    #Test
    if message.content.startswith('/테스트'):
        print('{} : '.format(author) + '/테스트')
        if message.author.id == adminID:
            await client.send_message(channel, '{}, :ballot_box_with_check: 어드민 테스트!'.format(mention_author))
            print(BotName + ' : {}, :ballot_box_with_check: 어드민 테스트!'.format(author))
        else:
            await client.send_message(channel, '{}, :ballot_box_with_check: 테스트!'.format(mention_author))
            print(BotName + ' : {}, :ballot_box_with_check: 테스트!'.format(author))

    #Say(Repeat)
    if message.content.startswith('/말해'):
        print('{} : '.format(author) + '/말해')
        if message.author.id == adminID:
            msg = message.content.split()
            output = ''
            for word in msg[1:]:
                output += word
                output += ' '
            await client.send_message(channel, output)
            print(BotName + ' : ' + output)
        else:
            await client.send_message(channel, '{}, :warning: 명령어를 사용할 권한이 없습니다.'.format(mention_author))
            print(BotName + ' : {}, :warning: 명령어를 사용할 권한이 없습니다.'.format(author))

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
client.loop.create_task(change_status())
client.run(str(os.environ.get('BOT_TOKEN')))
