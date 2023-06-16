from discord.ext import commands


""" //- COMANDOS -// """


@commands.group(
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


async def setup(Vitalia):
    Vitalia.add_command(math)


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
