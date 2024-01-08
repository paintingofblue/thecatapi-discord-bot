import discord
from discord.ext import commands
from utils.cat import cat
from utils.config import cfg


class View(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@discord.app_commands.command(name="view", description="View your upvoted, downvoted, and favorited media.")
	@discord.app_commands.choices(type=[
        discord.app_commands.Choice(name='Likes', value='likes'),
        discord.app_commands.Choice(name='Dislikes', value='dislikes'),
		discord.app_commands.Choice(name='Favorites', value='favorites')
    ])
	async def view(self, interaction: discord.Interaction, type: str):
		if type == 'likes':
			return await self.likes_view(interaction)
		elif type == 'dislikes':
			return await self.dislikes_view(interaction)
		elif type == 'favorites':
			return await self.favorites_view(interaction)

	# Do individual functions for the leaderboards
	async def likes_view(self, interaction: discord.Interaction):
		pass

	async def dislikes_view(self, interaction: discord.Interaction):
		pass

	async def favorites_view(self, interaction: discord.Interaction):
		pass

async def setup(bot: commands.Bot):
	await bot.add_cog(View(bot))