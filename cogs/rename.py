import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from bot_utils import guild, SHYN3SS_ID
import random
import asyncio

f = open("./data/noms.txt", "r", encoding="utf-8")
names = sorted(f.read().split("\n"))
names.remove("")
f.close()
f = open("./data/noms.txt", "w", encoding="utf-8")
for name in names:
    if name != "":
        f.write(name + "\n")
f.close()

shyn3ss = 0


class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global shyn3ss
        g = self.bot.guilds[0]
        shyn3ss = await g.fetch_member(1084328393484533790)

    @app_commands.command(name="rename", description="Rename someone")
    async def rename(self, interaction):
        global shyn3ss
        new_nickname = names[random.randint(0, len(names))]
        await shyn3ss.edit(nick=new_nickname)
        await interaction.response.send_message(new_nickname, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Rename(bot), guilds=[guild])
