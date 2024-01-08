import discord
from utils.config import cfg
from utils.general import setup_user_dict

#	thecatapi has endpoints for upvoting and downvoting, don't use this shit lol
# need to do some shit with user id hashing tho for sure

class Voting(discord.ui.View):
	def __init__(self, img: dict):
		super().__init__(timeout=None)
		self.image = img

	@discord.ui.button(emoji='👍', style=discord.ButtonStyle.blurple)
	async def upvote(self, interaction: discord.Interaction, _button: discord.ui.Button):
		key = f'users.{interaction.user.id}'
		user = setup_user_dict(cfg.get(key))

		if self.image not in user['likes']:
			while len(user['likes']) >= 50:
				user['likes'].pop(0)

			user['likes'].append(self.image)
			cfg.set(key, user)
			return await interaction.response.send_message('Liked!', ephemeral=True)
		else:
			return await interaction.response.send_message('You have already liked this image!', ephemeral=True)

	@discord.ui.button(emoji='👎', style=discord.ButtonStyle.blurple)
	async def downvote(self, interaction: discord.Interaction, _button: discord.ui.Button):
		key = f'users.{interaction.user.id}'
		user = setup_user_dict(cfg.get(key))

		if self.image not in user['dislikes']:
			while len(user['dislikes']) >= 50:
				user['dislikes'].pop(0)

			user['dislikes'].append(self.image)
			cfg.set(key, user)
			return await interaction.response.send_message('Disliked!', ephemeral=True)
		else:
			return await interaction.response.send_message('You have already disliked! this image!', ephemeral=True)

	@discord.ui.button(emoji='♥', style=discord.ButtonStyle.blurple)
	async def favorite(self, interaction: discord.Interaction, _button: discord.ui.Button):
		key = f'users.{interaction.user.id}'
		user = setup_user_dict(cfg.get(key))

		if self.image not in user['favorites']:
			while len(user['favorites']) >= 50:
				user['favorites'].pop(0)

			user['favorites'].append(self.image)
			cfg.set(key, user)
			return await interaction.response.send_message('Favorited!', ephemeral=True)
		else:
			return await interaction.response.send_message('You have already favorited this image!', ephemeral=True)