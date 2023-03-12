import discord
import asyncio
from bot_utils import TOKEN
from bot_utils import guild
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
    "cogs.hello",
    "cogs.rename",
]


@bot.event
async def on_ready():
    log.info(f"Connecté en tant que {bot.user}")
    if not bot.synced:
        log.info("Syncing...")
        fmt = await bot.tree.sync(guild=bot.guild_object)
        s = "" if len(fmt) < 2 else "s"
        log.info("Sync complete")
        log.info(f"{len(fmt)} commande{s} synchronisée{s}.")
        bot.synced = True

    bot.guild = bot.get_guild(guild)
    bot.shyn3ss = await bot.guild.fetch_member(200610609476141057)
    await bot.tree.sync(guild=guild)
    print("Yo")


async def load():
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(extension, " chargé avec succès !")
        except Exception as e:
            log.error(f"Failed to load extension {extension}")
            log.error(e)


async def main():
    await load()
    await bot.start(TOKEN)


asyncio.run(main())
