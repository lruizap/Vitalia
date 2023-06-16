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

    for commands_file in settings.COMMANDS_DIR.glob("*.py"):
        if commands_file.name != "__init__.py":
            await Vitalia.load_extension(f"commands.{commands_file.name[:-3]}")


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
    description='Vitalia saluda al usuario mencionandolo',
    help='Esta es la ayuda para el comando "V-hola"',
    brief='Vitalia saluda al usuario mencionandolo'
)
#! Saluda al usuario que ha enviado el comando
async def hola(ctx):
    usuario = ctx.message.author.mention
    await ctx.send(f"¡Hola {usuario}! ¡Soy Vitalia, tu bot de Discord!")


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


@Vitalia.command(
    aliases=['hc'],
    description='A continuación se muestran todos los comandos del bot',
    help='Embed informativo para utilizar los comandos del bot',
    brief='Embed informativo para utilizar los comandos del bot'
)
#! Embed informativo para utilizar los comandos del bot
async def helpCommands(ctx):
    usuario = ctx.message.author.mention
    embed = discord.Embed(
        title="Comandos de Vitalia",
        description=f"A continuación, {usuario} se muestran todos los comandos del bot",
        color=discord.Color.green()
    )

    embed.set_thumbnail(
        url="https://icones.pro/wp-content/uploads/2021/05/icone-d-information-vert.png")

    # Ordenar en orden alfabético
    embed.add_field(
        name="`V-helpCommands`", value="Vitalia nos dará una guia de sus comandos para que los usemos", inline=False)
    embed.add_field(
        name="`V-hola`", value="Vitalia saluda al usuario que envió el comando", inline=False)
    embed.add_field(
        name="`V-math`", value="Vitalia tiene operaciones matemáticas\nConsultar con el comando `V-help math`", inline=False)
    embed.add_field(
        name="`V-ping`", value="Vitalia contesta con un 'pong!'", inline=False)

    embed.set_footer(text="Espero que te haya ayudado")

    await ctx.send(embed=embed)


""" //- ERRORES -// """


""" //- FIN -// """

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(settings.DISCORD_TOKEN, root_logger=True)
