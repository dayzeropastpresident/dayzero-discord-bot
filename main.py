import os
import discord
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hello {member.name}, welcome to the DayZero Discord Server!'
            )

@bot.command(name='quote')
async def quote(ctx):
    quotes = [
            "Biscuit: They have a party for two days and then get to meet the kids they fucked",
            "Biscuit: There's always a furry in the backend",
            "Creel: They replaced my bash shell with nyan cat",
            "MacDaddy: I was using Linux while you were still doodooing in diapers!",
            "MacDaddy: How hard is it to pull out a pistol and shoot someone?",
            "Dylan: I have to turn my security onion off during the summer - too hot",
            "Tristen: He's got an insurance policy - these hands",
            "Tristen: All the girls were like sploosh",
            "Tristen: According to company policy, we don't negotiate with cyberterrorists",
            "Thanh: I'm a nice guy, I didn't pee on him",
            "Chris: Category? MILF.",
            "Chris: That trophy has nice birthing hips.",
            "Nathan: Weird DeMarcus, I thought you were circumcised!",
            "Nathan: How about I not shit on the floor?",
            "Ryan: Does anyone want my English degree? I have no use for it."
    ]
    response = random.choice(quotes)
    await ctx.send(response)


bot.run(TOKEN)

