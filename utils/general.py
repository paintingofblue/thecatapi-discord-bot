import discord
import json
from utils.cat import cat

async def breed_autocomplete(interaction: discord.Interaction, current: str):
	breeds = await cat.breeds()
	current = current.strip()

	# Only return 25 options (Discord limitation with dropdowns)
	return [
		discord.app_commands.Choice(name=breed["name"], value=json.dumps({
			"name": breed["name"],
			"id": breed["id"]
		}))
		for breed in breeds
		if not current or current.lower() in breed["name"].lower()
	][:25]

def setup_user_dict(user):
	if not user.get('favorites'):
		user['favorites'] = []

	if not user.get('likes'):
		user['likes'] = []

	if not user.get('dislikes'):
		user['dislikes'] = []

	return user