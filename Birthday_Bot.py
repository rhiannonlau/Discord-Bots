import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

birthdays = []

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        )

client.run(TOKEN)

# bot = commands.Bot(intents=discord.Intents.default(), command_prefix='!')

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to Discord!')

# @bot.command(name='add_bday', help='Add a user\'s birthday.')
# async def add_birthday(ctx, user, birthday):
#     birthdays.append()
#     await ctx.send("Birthday added!")

# @bot.command(name='add_bday_age', help='Add a user\'s birthday and their age.')
# async def add_birthday(ctx, user, birthday, age: int):
#     birthdays.append()
#     await ctx.send("Birthday added!")

# @bot.command(name='add_age', help='Add a user\'s age to a pre-existing birthday.')
# async def add_birthday(ctx, user, age: int):
#     birthdays.append()
#     await ctx.send("Age added!")

# @bot.command(name='edit_bday', help='Edit a user\'s birthday.')
# async def add_birthday(ctx, user, birthday):
#     birthdays.append()
#     await ctx.send("Birthday edited!")

# @bot.command(name='edit_age', help='Edit a user\'s age.')
# async def add_birthday(ctx, user, age: int):
#     birthdays.append()
#     await ctx.send("Age edited!")

# bot.run(TOKEN)
