import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, Vitalia):
        self.Vitalia = Vitalia

    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     await message.add_reaction('👋')

    @commands.command(
        description='Vitalia saluda al usuario mencionandolo',
        help='Esta es la ayuda para el comando "V-hola"',
        brief='Vitalia saluda al usuario mencionandolo'
    )
    #! Saluda al usuario que ha enviado el comando
    async def hola(self, ctx):
        usuario = ctx.message.author.mention
        await ctx.send(f"¡Hola {usuario}! ¡Soy Vitalia, tu bot de Discord!")


async def setup(Vitalia):
    await Vitalia.add_cog(Greetings(Vitalia))
