import discord
from discord.ext import commands
from discord import app_commands
from bot_utils import guild, COLOR_BOT


class Aide(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="aide", description="Affiche la liste de commandes disponible")
    async def aide(self, interaction):
        value = (
            "/anniversaires : affiche la liste des anniversaires des membre de SRBB\n"
            + "/roll <max=2^63-1> <min=1> : renvoie un nombre entier au hasard entre min et max\n"
            + "/pileOuFace : renvoie au hasard soit pile soit face\n"
            + "/tirage_au_sort <options>: tire au sort parmi plusieurs options\n"
            + "/rappel : définit un rappel\n"
        )
        embed = discord.Embed(
            title="Freyja", colour=discord.Colour(COLOR_BOT)
        )
        embed.add_field(name="Commandes:", value=value, inline=False)
        file = discord.File("./img/icon-bot.png", filename="icon-bot.png")
        embed.set_thumbnail(url="attachment://icon-bot.png")
        await interaction.response.send_message(file=file, embed=embed)


async def setup(bot):
    await bot.add_cog(Aide(bot), guilds=[guild])
