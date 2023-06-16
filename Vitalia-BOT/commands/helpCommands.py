from discord.ext import commands
import discord

""" //- COMANDOS -// """


@commands.command(
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
