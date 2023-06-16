import settings
import discord
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
    aliases=['+'],
    description='Vitalia suma dos numeros',
    help='Esta es la ayuda para el comando "V-sum"',
    brief='Vitalia suma dos numeros'
)
#! Suma dos números
async def sum(ctx, one: int, two: int):
    usuario = ctx.message.author.mention
    await ctx.send(f"{usuario}, el resultado es: {one + two}")


""" //- ERRORES -// """


@Vitalia.event
#! Manejo de errores de forma global
async def on_command_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


@sum.error
#! Manejo de errores del comando "sum"
async def sum_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


""" //- FIN -// """

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(settings.DISCORD_TOKEN, root_logger=True)
