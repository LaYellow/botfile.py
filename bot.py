import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
from itertools import cycle

my_token = 'NTQyNTAyNjIzNjY4OTk0MDY5.DzvCIw.JoOolByOgGw3OqT4pnOMf5Xc5E8'

client = commands.Bot(command_prefix = '/')

client.remove_command('help')
status = ['/help for commands', 'with LaYellow#9207', "LaYellow Bot"]

players = {}


async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name =current_status))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print('The bot is online and is connected to discord')
 
@client.command()
async def ping():
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    await client.say('@everyone')
    
    
client.run('NTQyNTAyNjIzNjY4OTk0MDY5.DzvCIw.JoOolByOgGw3OqT4pnOMf5Xc5E8')
