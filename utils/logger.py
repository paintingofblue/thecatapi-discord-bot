from datetime import datetime
from typing import Literal

class Logger:
	def __init__(self):
		self.colors = {
			'red': '\033[91m',
			'yellow': '\033[93m',
			'green': '\033[92m',
			'grey': '\033[90m',
			'reset': '\033[37m'
		}

	def fmt_date(self):
		time = datetime.now().strftime('%H:%M:%S')
		return f'[{time}]'

	def fmt_log_type(
		self,
		_color: Literal["red", "yellow", "green", "grey", "reset"],
		_type: Literal["~", "!", "-", "+"]
	):
		color = self.colors.get(_color, self.colors['reset'])

		return f'{color}[{_type}]{self.colors["reset"]}'

	def log(
		self,
		_color: Literal["red", "yellow", "green", "grey", "reset"],
		_type: Literal["~", "!", "-", "+"],
		text: str
	):
		date = self.fmt_date()
		log_type = self.fmt_log_type(_color, _type)
		print(f'{date} {log_type} {text}')

	def info(self, text: str):
		self.log('grey', '~', text)

	def error(self, text: str):
		self.log('red', '!', text)

	def warning(self, text: str):
		self.log('yellow', '-', text)

	def success(self, text: str):
		self.log('green', '+', text)