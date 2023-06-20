import settings
import discord
from cogs.greetings import Greetings
from discord.ext import commands


logger = settings.logging.getLogger("Vitalia")


intents = discord.Intents.all()
intents.message_content = True
intents.members = True

Vitalia = commands.Bot(command_prefix='V-', intents=intents,
                       status=discord.Status.dnd,
                       activity=discord.Game(name="Programando BOT de DISCORD"))


""" //- EVENTOS -// """


@Vitalia.event
#! Crearemos un evento para indicar cuando el BOT está online
async def on_ready():
    logger.info(f"BOT: {Vitalia.user} (ID: {Vitalia.user.id})")

    await Vitalia.tree.sync()

    for commands_file in settings.COMMANDS_DIR.glob("*.py"):
        if commands_file.name != "__init__.py":
            await Vitalia.load_extension(f"commands.{commands_file.name[:-3]}")

    for cogs_file in settings.COGS_DIR.glob("*.py"):
        if cogs_file.name != "__init__.py":
            await Vitalia.load_extension(f"cogs.{cogs_file.name[:-3]}")

    print(f"\033[32m\n 🦉 ► {Vitalia.user} ha cobrado vida\n\033[39m")


@Vitalia.event
#! Evento para enviar un mensaje a usuarios nuevos del servidor
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hola, {member.mention}, Bienvenido a nuestro servidor de pruebas.\nMuchas gracias por ayudar')


@Vitalia.event
#! Evento para que imprime los mensajes enviados por pantalla
async def on_message(message):
    # Verificar que el mensaje no sea del propio bot
    if message.author == Vitalia.user:
        return

    # Replica al mensaje privado
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != Vitalia.user:
        await message.reply('Lo siento, no estoy programado para ayudarte con lo que me pides')

    print(
        f"\033[34m\n 🧑 ► {message.author} ha dicho: {message.content}\n\033[39m")

    # Pasar el mensaje a la funcionalidad de comandos
    await Vitalia.process_commands(message)


""" //- COMANDOS -// """


@Vitalia.hybrid_command(
    aliases=['p'],
    description='Vitalia contesta con un "pong!"',
    help='Esta es la ayuda para el comando "V-ping"',
    brief='Vitalia contesta con un "pong!"'
)
#! Contesta al usuario con un "pong!"
async def ping(ctx):
    # ctx es el canal donde se ha enviado el mensaje

    # con ctx.message.author.send() podemos hacer que el mensaje de respuesta lo de por privado
    # await ctx.message.author.send("pong!")

    await ctx.send("pong!")


@Vitalia.tree.command(
    description='Vitalia contesta con un "ciao!"'
)
#! Contesta al usuario con un "ciao!"
async def ciao(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)


""" //- ERRORES -// """


""" //- FIN -// """

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(settings.DISCORD_TOKEN, root_logger=True)
