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


@Vitalia.group(
    aliases=['m'],
    description='Vitalia tiene comandos para operaciones matemáticas',
    help='Esta es la ayuda para el comando "V-math"',
    brief='Vitalia te ayuda con las mates'
)
async def math(ctx):
    usuario = ctx.message.author.mention
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Por favor {usuario}, Introduzca un comando perteneciente al grupo')


# ? Simple


@math.group(
    aliases=['s'],
    description='Vitalia tiene comandos para operaciones matemáticas simples',
    help='Esta es la ayuda para el comando "V-math simple"',
    brief='Vitalia te ayuda con las mates'
)
async def simple(ctx):
    usuario = ctx.message.author.mention
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Por favor {usuario}, Introduzca un comando perteneciente al grupo')


@simple.command(
    aliases=['+'],
    description='Vitalia suma dos numeros',
    help='Esta es la ayuda para el comando "V-math simple sum"',
    brief='Vitalia suma dos numeros'
)
#! Suma dos números
async def sum(ctx, one: int, two: int):
    usuario = ctx.message.author.mention
    await ctx.send(f"{usuario}, el resultado es: {one + two}")


@simple.command(
    aliases=['-'],
    description='Vitalia resta dos numeros',
    help='Esta es la ayuda para el comando "V-math simple subtract"',
    brief='Vitalia resta dos numeros'
)
#! Resta dos números
async def subtract(ctx, one: int, two: int):
    usuario = ctx.message.author.mention
    await ctx.send(f"{usuario}, el resultado es: {one - two}")


# ? Avanzado


@math.group(
    aliases=['a'],
    description='Vitalia tiene comandos para operaciones matemáticas avanzadas',
    help='Esta es la ayuda para el comando "V-math advanced"',
    brief='Vitalia te ayuda con las mates'
)
async def advanced(ctx):
    usuario = ctx.message.author.mention
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Por favor {usuario}, Introduzca un comando perteneciente al grupo')


@advanced.command(
    aliases=['*'],
    description='Vitalia multiplica dos numeros',
    help='Esta es la ayuda para el comando "V-math avanced multiply"',
    brief='Vitalia multiplica dos numeros'
)
#! Multiplica dos números
async def multiply(ctx, one: int, two: int):
    usuario = ctx.message.author.mention
    await ctx.send(f"{usuario}, el resultado es: {one * two}")


@advanced.command(
    aliases=['/'],
    description='Vitalia divide dos numeros',
    help='Esta es la ayuda para el comando "V-math avanced divide"',
    brief='Vitalia divide dos numeros'
)
#! Divide dos números
async def divide(ctx, one: int, two: int):
    usuario = ctx.message.author.mention
    await ctx.send(f"{usuario}, el resultado es: {one / two}")


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


@sum.error
#! Manejo de errores del comando "sum"
async def sum_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


@subtract.error
#! Manejo de errores del comando "subtract"
async def subtract_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


@multiply.error
#! Manejo de errores del comando "multiply"
async def multiply_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


@divide.error
#! Manejo de errores del comando "divide"
async def divide_error(ctx, error):
    usuario = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Por favor, {usuario}, comprueba los valores introducidos")


""" //- FIN -// """

# Ahora activamos el bot con los comandos creados
# Para que el bot lea los comandos debemos introducir la token
# Esta debe ser la última línea del código

Vitalia.run(settings.DISCORD_TOKEN, root_logger=True)
