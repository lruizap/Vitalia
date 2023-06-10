# Este código es para introducir los comandos de barra y para la insignia de desarrollador

from discord import app_commands, Intents, Client, Interaction
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


class CVitalia(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


Vitalia = CVitalia(intents=Intents.all())


@Vitalia.event
async def on_ready():
    print(f"{Vitalia.user} ha cobrado vida")


@Vitalia.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")


# Este es el comando de ping pero para los comandos de barra

@Vitalia.tree.command()
async def ping(interaction: Interaction):
    await interaction.response.send_message('pong')

Vitalia.run(DISCORD_TOKEN)
