import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild, COLOR_BOT
import asyncio
import json

with open("./data/birthdays.json", "r", encoding="utf-8") as f:
    data = json.load(f)

months = []

for month in data:
    months.append(month)


class Birthdays(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="birthdays", description="Show the list of birthdays of SRBB's members"
    )
    async def birthdays(self, interaction):
        embed = discord.Embed(
            title="Birthdays of SRBB's members", colour=discord.Colour(COLOR_BOT)
        )
        for month in months:
            value = ""
            for hb in data[month]:
                value += hb["name"] + "\t" + hb["birthday"] + "\n"
            if value == "":
                continue
            embed.add_field(name=f"{month}:", value=value, inline=False)
        file = discord.File("./img/icon-srbb.png", filename="icon-srbb.png")
        embed.set_thumbnail(url="attachment://icon-srbb.png")
        await interaction.response.send_message(file=file, embed=embed)


async def setup(bot):
    await bot.add_cog(Birthdays(bot), guilds=[guild])
