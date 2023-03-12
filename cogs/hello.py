import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import asyncio


class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Say something")
    async def hello(self, interaction):
        await interaction.response.send_message("UwU")


async def setup(bot):
    await bot.add_cog(Hello(bot), guilds=[guild])
