import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
Vitalia = commands.Bot(command_prefix='V-', intents=intents)


@Vitalia.command()
async def ping(ctx):
    await ctx.send('pong')


Vitalia.run(DISCORD_TOKEN)
