import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import asyncio


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.synced = True
        self.guild = None
        self.shyn3ss = None


class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rename", description="test")
    async def rename(self, interaction, nick: str):
        await interaction.response.send_message(nick, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Rename(bot), guilds=[guild])
