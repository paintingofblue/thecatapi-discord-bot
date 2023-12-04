import discord
import json
import httpx
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