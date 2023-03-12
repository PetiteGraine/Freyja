import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild
import asyncio


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show the list of commands")
    async def help(self, interaction):
        value = (
            "/ping : the bot say UwU\n"
            + "/rename <member> : rename the member randomly\n"
            + "/roll <man=100> <min=1> : give a random number between min and max\n"
        )
        embed = discord.Embed(title="Better_Shyn3ss - help menu")
        embed.add_field(name="Commands:", value=value, inline=False)
        file = discord.File("./img/icon_bot.png", filename="icon_bot.png")
        embed.set_thumbnail(url="attachment://icon_bot.png")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Help(bot), guilds=[guild])
