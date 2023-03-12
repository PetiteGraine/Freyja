import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild
from random import randint
import asyncio


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roll", description="Give a random integer")
    async def roll(self, interaction, max: int = 100, min: int = 1):
        if max < min:
            await interaction.response.send_message("max must be superior to min")
            return
        await interaction.response.send_message(randint(min, max))


async def setup(bot):
    await bot.add_cog(Roll(bot), guilds=[guild])
