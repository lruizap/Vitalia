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
#! Crearemos un evento para indicar cuando el BOT está online
async def on_ready():
    print(f"\033[32m\n 🦉 ► {Vitalia.user} ha cobrado vida\n\033[39m")


@Vitalia.event
#! Evento para que imprime los mensajes enviados por pantalla
async def on_message(message):
    # Verificar que el mensaje no sea del propio bot
    if message.author == Vitalia.user:
        return

    print(
        f"\033[34m\n 🧑 ► {message.author} ha dicho: {message.content}\n\033[39m")

    # Pasar el mensaje a la funcionalidad de comandos
    await Vitalia.process_commands(message)


""" //- COMANDOS -// """


@Vitalia.command()
#! Contesta al usuario con un "pong!"
async def ping(ctx):
    # ctx es el canal donde se ha enviado el mensaje
    await ctx.send("pong!")


@Vitalia.command()
#! Saluda al usuario que ha enviado el comando
async def hola(ctx):
    usuario = ctx.message.author.mention
    await ctx.send(f"¡Hola {usuario}! ¡Soy Vitalia, tu bot de Discord!")


@Vitalia.command()
#! Embed informativo para utilizar los comandos del bot
async def helpCommands(ctx):
    embed = discord.Embed(
        title="Comandos de Vitalia",
        description="A continuación se muestran todos los comandos del bot",
        color=discord.Color.green()
    )

    embed.set_thumbnail(
        url="https://icones.pro/wp-content/uploads/2021/05/icone-d-information-vert.png")

    # Ordenar en orden alfabético
    embed.add_field(
        name="V-helpCommands", value="Vitalia nos dará una guia de sus comandos para que los usemos", inline=False)
    embed.add_field(
        name="V-hola", value="Vitalia saluda al usuario que envió el comando", inline=False)
    embed.add_field(
        name="V-ping", value="Vitalia contesta con un 'pong!'", inline=False)

    embed.set_footer(text="Espero que te haya ayudado")

    await ctx.send(embed=embed)


""" //- FIN -// """


# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(DISCORD_TOKEN)
