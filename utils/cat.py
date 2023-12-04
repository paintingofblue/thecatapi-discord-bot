import random
from httpx import AsyncClient, Response
from datetime import datetime, timedelta
from utils.config import cfg, deep_merge
from utils.globals import BASE_HEADERS


class ApiWrapper:
	def __init__(self):
		self.cache = {
			"edgecats_gifs": {"data": [], "expiry_date": 0},
			"facts": {"data": [], "expiry_date": 0},
			"breeds": {"data": [], "expiry_date": 0},
		}

	async def _make_request(self, url, headers={}, params = {}):
		headers = deep_merge(BASE_HEADERS, headers)

		async with AsyncClient() as client:
			return await client.get(url, headers=headers, params = params)

	async def gif(self) -> dict:
		num = random.randint(1, 2)

		# -- Select between multiple gif sources at random --
		# TheCatAPI
		if num == 1:
			res = await self._make_request(
				url="https://api.thecatapi.com/v1/images/search?mime_types=gif",
				headers={"x-api-key": random.choice(cfg.get("api_keys"))},
			)

			if res.status_code == 200:
				obj = res.json()
				if isinstance(obj, list):
					obj = obj[0]

				return obj.get("url")

		# Edgecats
		if datetime.now().timestamp() > self.cache["edgecats_gifs"]["expiry_date"]:
			res: Response = await self._make_request(url="https://edgecats.net/all")

			self.cache["edgecats_gifs"] = {
				"data": [
					line.split('href="')[1].split('"')[0]
					for line in res.text.splitlines()
					if 'href="' in line
				],
				"expiry_date": (datetime.now() + timedelta(days=1)).timestamp(),
			}
			print(self.cache["edgecats_gifs"]["data"])

		return random.choice(self.cache["edgecats_gifs"]["data"])

	async def image(self, limit = 1, breed = None):
        # initialize query params
		params = {
			"mime_types": "jpg,png",
			"limit": limit
		}

		# add breed id to query params if specified
		if breed:
			params["breed_ids"] = breed

		# make request
		res = await self._make_request(
			url="https://api.thecatapi.com/v1/images/search",
			headers={"x-api-key": random.choice(cfg.get("api_keys"))},
			params=params
		)

		return res.json()

	async def fact(self) -> str:
		if datetime.now().timestamp() > self.cache["facts"]["expiry_date"]:
			res = await self._make_request(
				url="https://gist.githubusercontent.com/paintingofblue/657d0c4d1202374889ce4a98a6b7f35f/raw/catfacts.txt"
			)

			self.cache["facts"] = {
				"data": [line.strip() for line in res.text.splitlines()],
				"expiry_date": (datetime.now() + timedelta(days=1)).timestamp(),
			}

		return random.choice(self.cache["facts"]["data"])

	async def breeds(self) -> dict:
		if datetime.now().timestamp() > self.cache["breeds"]["expiry_date"]:
			res = await self._make_request(
				url="https://api.thecatapi.com/v1/breeds",
				headers={"x-api-key": random.choice(cfg.get("api_keys"))},
			)

			self.cache["breeds"] = {
				"data": sorted(res.json(), key=lambda x: x.get("name")),
				"expiry_date": (datetime.now() + timedelta(days=1)).timestamp(),
			}

		return self.cache["breeds"]["data"]

cat = ApiWrapper()