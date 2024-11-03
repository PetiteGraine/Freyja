import discord
import asyncio
from bot_utils import TOKEN, GUILD_ID, guild
from discord.ext import commands
import logging
from discord.utils import _ColourFormatter

log = logging.getLogger("Freyja")
log.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setFormatter(_ColourFormatter())
log.addHandler(stream)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.synced = False  # change to False to sync
        self.guild = None
        self.shyn3ss = None


intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix="Freyja ", help_command=None, intents=intents)


# Load cogs
initial_extensions = [
    "cogs.aide",
    "cogs.anniversaires",
    "cogs.roll",
    "cogs.pileOuFace",
    "cogs.rappel",
    "cogs.tirageAuSort",
]


@bot.event
async def on_ready():
    log.info(f"Logged as {bot.user}")

    if not bot.synced:
        log.info("Syncing...")
        fmt = await bot.tree.sync(guild=guild)
        s = "" if len(fmt) < 2 else "s"
        log.info("Sync complete")
        log.info(f"{len(fmt)} commande{s} synchronisée{s}.")
        bot.synced = True

    bot.guild = bot.get_guild(GUILD_ID)


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
