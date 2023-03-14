import discord
import asyncio
from bot_utils import TOKEN, guild, SHYN3SS_ID
from discord.ext import commands
import logging
from random import choice

from discord.utils import get

from discord.utils import _ColourFormatter
from time import sleep


log = logging.getLogger("UwU")
log.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setFormatter(_ColourFormatter())
log.addHandler(stream)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="UwU ", help_command=None, intents=intents)


# Load cogs
initial_extensions = [
    "cogs.ping",
    "cogs.rename",
    "cogs.roll",
    "cogs.help",
    "cogs.birthday",
]


@bot.event
async def on_ready():
    log.info(f"Logged as {bot.user}")
    await bot.tree.sync(guild=guild)


async def load():
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(extension, " is loaded !")
        except Exception as e:
            log.error(f"Failed to load extension {extension}")
            log.error(e)


async def main():
    await load()
    await bot.start(TOKEN)


asyncio.run(main())
