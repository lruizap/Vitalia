import settings
import discord
from cogs.greetings import Greetings
from discord.ext import commands


logger = settings.logging.getLogger("Vitalia")


Vitalia = commands.Bot(command_prefix='V-', intents=discord.Intents.all(),
                       status=discord.Status.dnd,
                       activity=discord.Game(name="Programando BOT de DISCORD"))


""" //- EVENTOS -// """


@Vitalia.event
#! Crearemos un evento para indicar cuando el BOT está online
async def on_ready():
    logger.info(f"BOT: {Vitalia.user} (ID: {Vitalia.user.id})")
    print(f"\033[32m\n 🦉 ► {Vitalia.user} ha cobrado vida\n\033[39m")

    for commands_file in settings.COMMANDS_DIR.glob("*.py"):
        if commands_file.name != "__init__.py":
            await Vitalia.load_extension(f"commands.{commands_file.name[:-3]}")

    await Vitalia.load_extension('cogs.greetings')


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


@Vitalia.command(
    aliases=['p'],
    description='Vitalia contesta con un "pong!"',
    help='Esta es la ayuda para el comando "V-ping"',
    brief='Vitalia contesta con un "pong!"'
)
#! Contesta al usuario con un "pong!"
async def ping(ctx):
    # ctx es el canal donde se ha enviado el mensaje
    await ctx.send("pong!")


""" //- ERRORES -// """


""" //- FIN -// """

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(settings.DISCORD_TOKEN, root_logger=True)
