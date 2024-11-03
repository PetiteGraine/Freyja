from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import random

class TirageAuSort(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tirage_au_sort", description="Tire au sort parmi plusieurs options")
    @app_commands.describe(options="Options à tirer au sort, séparées par des virgules")
    async def tirageAuSort(self, interaction, options: str):
        options_list = [opt.strip() for opt in options.split(",") if opt.strip()]
        
        if not options_list:
            await interaction.response.send_message("Veuillez fournir au moins une option pour le tirage", ephemeral=True)
            return
        
        tirage_index = random.randint(0, len(options_list) - 1)
        tirage = options_list[tirage_index]

        options_formatted = "\n".join(f"{i + 1}: {opt}" for i, opt in enumerate(options_list))

        await interaction.response.send_message(f"{options_formatted}\n\n-> {tirage}")

async def setup(bot):
    await bot.add_cog(TirageAuSort(bot), guilds=[guild])
