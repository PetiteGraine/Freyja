import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild, COLOR_BOT
import asyncio


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show the list of commands")
    async def help(self, interaction):
        value = (
            "/birthdays : show the list of birthdays of SRBB's members\n"
            + "/ping : mention the user\n"
            + "/rename <member> : rename Shyn3ss#4125 randomly\n"
            + "/roll <max=100> <min=1> : give a random integer between min and max\n"
        )
        embed = discord.Embed(
            title="Freyja - help menu", colour=discord.Colour(COLOR_BOT)
        )
        embed.add_field(name="Commands:", value=value, inline=False)
        file = discord.File("./img/icon-bot.png", filename="icon-bot.png")
        embed.set_thumbnail(url="attachment://icon-bot.png")
        await interaction.response.send_message(file=file, embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot), guilds=[guild])
