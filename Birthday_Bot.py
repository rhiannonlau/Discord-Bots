import os
import discord
import datetime
import asyncio

# from dotenv import load_dotenv
from discord.ext import commands, tasks

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

DISCORD_TOKEN = ""
CHANNEL_ID = 1233862600421539861

# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print("Hello! Study bot is ready!")
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send("Hello! Study bot is ready!")

# @bot.command()
# async def addbday(ctx, bday):
#     await ctx.send("Hello!")

# bot.run(DISCORD_TOKEN)


bday_list = []


client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def send_bday_message(user):
    channel = client.get_channel(CHANNEL_ID)  # Replace CHANNEL_ID with your channel ID
    await channel.send(f"Happy bday, {user}!", user)

async def bday_scheduler():
    # figure out what the closest bday is to start checking from so that only
    # one bday has to be checked every iteration of the while loop
    for i in range(len(bday_list)):
            m = bday_list[i][1].month
            d = bday_list[i][1].day
            if now.month <= m and now.day <= d:
                next = bday_list[i] # the closest bday
                next_i = i

    while True:
        now = datetime.datetime.now() # check curr date/time
        
        # if it matches the closest bday, send a message
        if now.month == next[1].month and now.day == next[1].day:
            await send_bday_message(next[0])

        next_i += 1
        next = bday_list[next_i]
        await asyncio.sleep(86400)

@client.event
async def on_ready():
    print("Bot is ready!")
    client.loop.create_task(bday_scheduler())

@bot.command
async def addbday(ctx, user, month, day):
    new_bday = [user, datetime.datetime(2025, month, day, 0, 0, 0)]

    # insert the bday into the list in ascending order
    for i in range(len(bday_list)):
        m1 = bday_list[i][1].month
        d1 = bday_list[i][1].day
        m2 = bday_list[i+1][1].month
        d2 = bday_list[i+1][1].day
        if m1 <= month and m2 >= month:
            if d1 <= day and d2 > day:
                bday_list.insert(i + 1, new_bday)

    await ctx.send(f"{user}'s birthday was added!", user)


client.run(DISCORD_TOKEN)
bot.run(DISCORD_TOKEN)





# from discord.ext import commands



# birthdays = []

# client = discord.Client(intents=discord.Intents.default())

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#         )

# client.run(TOKEN)

#################################################

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
