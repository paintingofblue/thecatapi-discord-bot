import discord
import random
from discord.ext import commands
from utils.cat import cat

class Fact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'fact', description = 'Sends a fact about cats.')
    async def fact(self, interaction: discord.Interaction):
        image = await cat.image() if random.randint(1, 2) == 1 else await cat.gif()
        fact = await cat.fact()

        embed=discord.Embed(title="Here's a cat fact:", description=fact, color=discord.Colour.blurple())
        embed.set_image(url=image)

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fact(bot))