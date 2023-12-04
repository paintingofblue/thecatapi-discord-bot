import json
import discord
from discord.ext import commands
from utils.cat import cat
from utils.general import breed_autocomplete


class Image(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@discord.app_commands.command(name="image", description="Sends a cat image.")
	@discord.app_commands.autocomplete(breed=breed_autocomplete)
	async def image(self, interaction: discord.Interaction, limit: int = 1, breed: str = '{}'):
		if breed:
			breed = json.loads(breed)

		images = await cat.image(limit = limit, breed=breed.get('id'))
		embeds = []

		# TODO: Add image processing, this doesn't work on mobile
		# as it abuses an undocumented Discord feature for webhooks

		# for image in images:
		# 	embed = discord.Embed(url = 'https://jane.rip', color=discord.Colour.blurple())
		# 	embed.set_image(url=image.get("url"))

		# 	if breed:
		# 		embed.add_field(name="Breed", value=breed["name"])

		# 	embeds.append(embed)

		await interaction.response.send_message(embeds=embeds)

async def setup(bot: commands.Bot):
	await bot.add_cog(Image(bot))