from discord.ext import commands
from discord import app_commands
from bot_utils import guild
from random import randint

class PileOuFace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="pile_ou_face", description="Renvoie au hasard soit pile soit face")
    async def pileOuFace(self, interaction):
        if randint(0, 1) == 0:
            await interaction.response.send_message(
                "Pile"
            )
            return
        await interaction.response.send_message(
                "Face"
            )

async def setup(bot):
    await bot.add_cog(PileOuFace(bot), guilds=[guild])
