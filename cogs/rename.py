import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from bot_utils import guild
import random
import asyncio

f = open("./data/names.txt", "r", encoding="utf-8")
names = sorted(f.read().split("\n"))
names.remove("")
f.close()
f = open("./data/names.txt", "w", encoding="utf-8")
for name in names:
    if name != "":
        f.write(name + "\n")
f.close()


class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rename", description="Rename someone")
    async def rename(self, interaction):
        new_nickname = names[random.randint(0, len(names))]
        await self.bot.shyn3ss.edit(nick=new_nickname)
        await interaction.response.send_message(new_nickname)


async def setup(bot):
    await bot.add_cog(Rename(bot), guilds=[guild])
