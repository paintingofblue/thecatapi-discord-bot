import os
import discord
import traceback
from discord.ext import commands
from typing import Union
from pathlib import Path
from utils.config import cfg
from utils.logger import log


class Bot(commands.Bot):
	def __init__(self):
		super().__init__(intents=discord.Intents.default(), command_prefix='')

	async def setupCommands(self, directory: Union[str, os.PathLike, Path] = "commands"):
		"""
		Recursively loads all commands in the specified directory.

		Args
		----
		- directory: Union[str, os.PathLike, Path]
			- The directory to load commands from (default: "commands")
		"""
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith(".py") and not file.startswith("_"):
					cog_path = (os.path.join(root, file).replace(os.sep, ".").rstrip(".py"))

					try:
						await self.load_extension(cog_path)
					except (commands.errors.ExtensionAlreadyLoaded):
						pass
					except:
						log.error(f'Unable to load {cog_path}\n{traceback.format_exc()}')

			for dir in dirs:
				await self.setupCommands(os.path.join(root, dir))

	async def setup_hook(self):
		await self.setupCommands("commands")

		try:
			synced = await bot.tree.sync()
			log.info(f"Synced {len(synced)} commands")
		except Exception:
			log.error(f"An error has occurred while syncing commands.\n{traceback.format_exc()}")
			return

	async def on_ready(self):
		await self.wait_until_ready()
		print(f'Logged in as {self.user}.')


# Check to see if the user has any API keys added
if cfg.get('api_keys') == []:
	log.error("No API keys found. Please add them to config.json.")
	exit(1)

# Check to see if the user has a valid Discord token set
token = cfg.get('token')
if not token:
	log.error("No token found. Please add it to config.json.")
	exit(1)

bot = Bot()
bot.run(token)