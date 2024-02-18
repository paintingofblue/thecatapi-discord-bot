import random
from typing import List


class CatAPI:
	def __init__(self, api_key: str | List[str]):
		self.api_key = api_key

	def fetch_key(self):
		if isinstance(self.api_key, list):
			return random.choice(self.api_key)

		return self.api_key

	def image(self):
		pass

	def gif(self):
		pass

	def fact(self):
		pass

	def upvote(self):
		pass

	def downvote(self):
		pass

	def favourite(self):
		pass

	def unfavourite(self):
		pass


