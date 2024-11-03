from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import asyncio

class Rappel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rappel", description="Définit un rappel")
    @app_commands.describe(time="Temps en minutes avant le rappel", msg="Message à rappeler")
    async def rappel(self, interaction, time: int, *, msg: str):
        await interaction.response.send_message(f"Rappel configuré pour dans {time} minute(s) : \"{msg}\"")

        await asyncio.sleep(time * 60)
        
        await interaction.channel.send(f"⏰ Rappel pour {interaction.user.mention} : {msg}")

async def setup(bot):
    await bot.add_cog(Rappel(bot), guilds=[guild])
