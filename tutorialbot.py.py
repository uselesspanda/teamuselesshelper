import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welome to Team Usless! Please wait for a Tryout or request fan.')
    print('Sent message to ' + member.name)
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welome to Team Usless! Please wait for a Tryout or request fan.')
    print('Sent message to ' + member.name)
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welome to Team Usless! Please wait for a Tryout or request fan.')
    print('Sent message to ' + member.name)
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welome to Team Usless! Please wait for a Tryout or request fan.')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='with Nobody'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!logo':
        em = discord.Embed(description='Team useless Logo')
        em.set_image(url='https://cdn.discordapp.com/attachments/554832401445027841/554845218101264427/Free_Sample_By_Wix_1.jpg')
        await client.send_message(message.channel, embed=em)
    if ('Nigga') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!random'):
        randomlist = ["1","2","3"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!getpinged'):
        await client.send_message(message.channel,'Here you go <@%s>'  %(message.author.id))
    if message.content.startswith('!getpinged'):
        await client.send_message(message.channel,'Here you go <@%s>'  %(message.author.id))
client.run('NTU0ODM2NjQyODg0NjE2MTky.D2ih8Q.qdsuY9MMQ9F3fWaRzJAESp9E8YM')
