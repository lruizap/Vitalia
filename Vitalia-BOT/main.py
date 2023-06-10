import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

Vitalia = commands.Bot(command_prefix='V-', intents=discord.Intents.all(),
                       status=discord.Status.dnd,
                       activity=discord.Game(name="Programando BOT de DISCORD"))


""" //- EVENTOS -// """


@Vitalia.event
# Crearemos un evento para indicar cuando el BOT está online
async def on_ready():
    print(f"\033[32m\n 🦉 ► {Vitalia.user} ha cobrado vida\n\033[39m")


@Vitalia.event
# Vamos a crear un evento para que imprima los mensajes enviados por pantalla
async def on_message(message):
    print(
        f"\033[34m\n 🧑 ► {message.author} ha dicho: {message.content}\n\033[39m")


""" //- COMANDOS -// """


@Vitalia.command()
# Contesta al usuario con un "pong!"
async def ping(ctx):
    # ctx es el canal donde se ha enviado el mensaje
    await ctx.send("pong!")


""" //- FIN -// """


# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(DISCORD_TOKEN)
