import os
import re
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel(763721598523277332)
    await welcome_channel.send(f"Welcome on the best server, <@{member.id}>")


@client.event
async def on_member_remove(member):
   await client.get_channel(763721598523277332).send(f"<@{member.id}> has left")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.search("Viktor|Áron", message.content) and message.content[-1] == "?":
        await message.channel.send(f"Use should ask him, <@{message.author.id}> !")

    if re.search("Hello|hello", message.content):
        await message.channel.send(":heart:")

    if re.search("!kick|Kick me!|kick me|kick|Kick", message.content):
        await message.author.create_dm()
        await message.author.dm_channel.send(
            "I have changed my mind, come back Human :heart: : https://discord.gg/GPVCTGT"
        )
        await message.author.kick()

    if re.search("Zsolt", message.author.name):
        await message.author.create_dm()
        await message.author.dm_channel.send(
            "Sorry, we don't like you! :heart:"
        )
        await message.author.kick()

    if re.search("Inroduce yourself|tell me something about you|Tell me something about your|!about", message.content):
        await message\
            .channel\
            .send("Well, I am Frankenstein's monster created by Áron and Viktor! Develop me!")
    if re.search("What is the meaning of life?|!life", message.content):
        await message.channel.send("42")

    if re.search("Hajrá Magyarország!", message.content):
        await message.channel.send("Hajrá magyarok!")

    # if "!clear" == message.content:
    #     mgs = []
    #     async for x in


client.run(TOKEN)
