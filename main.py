import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        msg = message.content
        if msg.startswith('score bro'):
            response = requests.get(
                'https://hs-consumer-api.espncricinfo.com/v1/pages/matches/live?'
            )
            data = dict(response.json())
            count = 0
            for i in data['content']['matches']:
                if i['stage'] == 'RUNNING' and (
                        i['state'] == "LIVE" or i['state']
                        == "RESULT") and i['status'] != "Not covered Live":
                    name_of_league = i['series']['name']
                    formato = i['format']
                    status = i['statusText']
                    teamA = dict(i['teams'][0])
                    teamB = dict(i['teams'][1])
                    str1 = " " + str(name_of_league) + " " + str(formato)
                    str2 = " " + str(teamA['team']['longName']) + " VS " + str(
                        teamB['team']['longName'])
                    str3 = " " + str(
                        teamA['team']['abbreviation']) + " " + str(
                            teamA['score']) + " " + str(
                                teamA['scoreInfo']) + "   VS   " + str(
                                    teamB['team']['abbreviation']) + " " + str(
                                        teamB['score']) + " " + str(
                                            teamA['scoreInfo'])

                    await message.channel.send(str1)
                    await message.channel.send(str2)
                    await message.channel.send(str3)
                    await message.channel.send(str(status))
                    count += 1
            if count == 0:
                await message.channel.send(' Live Match to chalne do vro')
        if msg.startswith('bro meme'):
				
				      response = requests.get('https://meme-api.herokuapp.com/gimme/dankmemes')
				      data = response.json()
				      print(data['url'])
				      await message.channel.send(data['url'])     


keep_alive()
client.run(os.getenv('TOKEN'))
