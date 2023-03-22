from yaml import safe_load
import discord

configuration_file = open("configuration.yaml", "r")
configuration = safe_load(configuration_file.read())

TOKEN = configuration["token"]
GUILD_ID = configuration["guild_id"]
SHYN3SS_ID = configuration["shyn3ss_id"]
COLOR_BOT = configuration["color_bot"]

guild = discord.Object(id=GUILD_ID)
