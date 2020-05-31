import discord
from discord.ext import commands
import asyncio
import random
import re
import requests

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("ログインしました")
    print("bot名:"+client.user.name)
    print("botID:"+str(client.user.id))
    print("discord.pyのver:"+str(discord.__version__))
    print("---------")


@client.event
async def on_message(message):
    # diceBOT
    if message.content.startswith("!dice"):         
        if client.user != message.author:            
            dice_txt = message.content[5:]
            try:
                dice_result_txt = " "
                m = re.match(r' ([0-9]+)d([0-9]+)', dice_txt)
                for i in range(int(m.groups()[0])):
                    dice_result_int = random.randint(1,int(m.groups()[1]))
                    dice_result_txt += ("["+str(dice_result_int)+"] ")
                await message.channel.send(m.groups()[1]+"面サイコロを"+m.groups()[0]+"回振りました。\n"+dice_result_txt)
            except Exception as e:
                dice_result_int = random.randint(1,100)
                await message.channel.send(dice_result_int)

    await client.process_commands(message)


TOKEN = 'NzE2NDY1NzYzMjA0MDcxNDM4.XtMLfQ.bSwt1bKIVBaGseJeKJ7RVLx3tEU'
client.run(TOKEN)
