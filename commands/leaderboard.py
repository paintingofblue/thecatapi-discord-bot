import discord
from discord.ext import commands
from utils.cat import cat


class Leaderboard(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@discord.app_commands.command(name="leaderboard", description="View the most upvoted, downvoted, or favorited media from a given time period.")
	@discord.app_commands.choices(
		type=[
			discord.app_commands.Choice(name='Likes', value='likes'),
			discord.app_commands.Choice(name='Dislikes', value='dislikes'),
			discord.app_commands.Choice(name='Favorites', value='favorites')
    	],
		time=[
			discord.app_commands.Choice(name='Day', value='day'),
			discord.app_commands.Choice(name='Week', value='week'),
			discord.app_commands.Choice(name='Month', value='month'),
			discord.app_commands.Choice(name='Year', value='year'),
			discord.app_commands.Choice(name='All Time', value='all')
		]
	)
	async def leaderboard(self, interaction: discord.Interaction, type: str, time: str):
		pass

async def setup(bot: commands.Bot):
	await bot.add_cog(Leaderboard(bot))