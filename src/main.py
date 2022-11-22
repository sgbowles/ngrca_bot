import discord
import os
import asyncio
import datetime

guild_ID = 927937712072310815

discord.http.API_VERSION = 9

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "!task":
        respStr = "Current: Get a suggestion box for wanted features working and a way for users to print other suggestions to read.\nFuture: TBD."
        await message.channel.send(respStr)

    elif message.content == "!status":
        respStr = "Currently in the infant stages of development."
        await message.channel.send(respStr)
        
    elif message.content == "!help":
        respStr = "Type !status for up to date information or type !task for info on the current task being developed."
        await message.channel.send(respStr)
        
    #elif message.content.startswith('!'):
        #await message.channel.send('Invalid command. Type !help for list of commands.')

client.run('MTA0MTg1NTk5MjY1MDAwNjU1OA.GyiPua.jDPuQH9vlV0frfyW6CuSUOu3hZ8Vs0SS0RQXnQ')
