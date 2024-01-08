import json
import discord
from discord.ext import commands
from utils.cat import cat
from utils.general import breed_autocomplete


class Pages(discord.ui.View):
	def __init__(self, interaction: discord.Interaction, pages: list):
		super().__init__(timeout=None)
		self.pages = pages
		self.interaction = interaction
		self.current_page = 0

	@discord.ui.button(label="Previous", style=discord.ButtonStyle.grey, disabled=True)
	async def previous(self, interaction: discord.Interaction, _button: discord.ui.Button):
		self.current_page -= 1

		if self.current_page == 0:
			for i in self.children:
				i.disabled = True if i.label == "Previous" else False
		else:
			for i in self.children:
				i.disabled = False

		await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

	@discord.ui.button(label="Next", style=discord.ButtonStyle.grey)
	async def next(self, interaction: discord.Interaction, _button: discord.ui.Button):
		self.current_page += 1

		if self.current_page == len(self.pages) - 1:
			for i in self.children:
				i.disabled = True if i.label == "Next" else False
		else:
			for i in self.children:
				i.disabled = False

		await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

class Breed(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	group = discord.app_commands.Group(name="breed", description="Commands related to cat breeds.")

	@group.command(name="list", description="Lists all cat breeds.")
	async def list(self, interaction: discord.Interaction):
		# Fetch breeds and sort them alphabetically
		breeds = await cat.breeds()

		embeds = []
		for i in range(0, len(breeds), 5):
			embed = discord.Embed(title="Cat Breeds", description="A list of all cat breeds.", color=discord.Colour.blurple())
			embed.set_footer(text=f"Page {i // 5 + 1} of {len(breeds) // 5 + 1}")

			for breed in breeds[i:i + 5]:
				embed.add_field(name=breed.get("name"), value=breed.get("description"), inline=False)

			embeds.append(embed)

		# Add images to each embed
		images = await cat.image(limit=len(embeds))
		for i, image in enumerate(images):
			embeds[i].set_image(url=image.get("url"))

		view = Pages(interaction, embeds)
		await interaction.response.send_message(embed=embeds[0], view=view)

	@group.command(name="info", description="Sends information about a cat breed.")
	@discord.app_commands.autocomplete(breed=breed_autocomplete)
	async def info(self, interaction: discord.Interaction, breed: str):
		breed = json.loads(breed)


	@group.command(name="stats", description="Sends statistics about a cat breed.")
	@discord.app_commands.autocomplete(breed=breed_autocomplete)
	async def stats(self, interaction: discord.Interaction, breed: str):
		breed = json.loads(breed)

async def setup(bot: commands.Bot):
	await bot.add_cog(Breed(bot))