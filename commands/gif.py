import discord
from discord.ext import commands
from utils.cat import cat

class Gif(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'gif', description = 'Sends a cat gif.')
    async def gif(self, interaction: discord.Interaction):
        gif = await cat.gif()

        embed=discord.Embed(title="Here's a cat gif:", color=discord.Colour.blurple())
        embed.set_image(url=gif)

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Gif(bot))