import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import asyncio


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Say UwU")
    async def ping(self, interaction):
        await interaction.response.send_message("UwU " + interaction.user.mention)


async def setup(bot):
    await bot.add_cog(Ping(bot), guilds=[guild])
