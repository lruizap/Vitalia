# El primer comando de nuestro bot

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Lo primero que debemos introducir es el prefijo para llamar al bot
# dentro de la aplicación

# Después tendremos que indicarle los permisos y privilegios

Vitalia = commands.Bot(command_prefix='V-', intents=discord.Intents.all())

# Crearemos un evento para indicar cuando el BOT está online


@Vitalia.event
async def on_ready():
    print(f"{Vitalia.user} ha cobrado vida")

# Ahora crearemos un comando que utilice el evento anterior


@Vitalia.command()
async def ping(ctx):
    # ctx es el canal donde se ha enviado el mensaje
    await ctx.send("pong!")

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(DISCORD_TOKEN)
