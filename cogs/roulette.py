from discord.ext import commands
from discord import app_commands
from bot_utils import guild
from random import randint

class Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roulette", description="Renvoie un nombre entier au hasard entre min et max")
    @app_commands.describe(min="Nombre minimal")
    @app_commands.describe(max="Nombre maximal")
    async def roulette(self, interaction, max: int = 100, min: int = 1):
        if max < min:
            await interaction.response.send_message(
                "max doit être supérieur à min", ephemeral=True)
            return
        await interaction.response.send_message(
            f"[{min}, {max}] -> {randint(min, max)}")

async def setup(bot):
    await bot.add_cog(Roulette(bot), guilds=[guild])
