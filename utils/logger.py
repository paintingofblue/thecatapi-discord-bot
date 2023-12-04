from datetime import datetime

class Logger:
    def __init__(self):
        self.red = "\033[91m"
        self.yellow = "\033[93m"
        self.green = "\033[92m"
        self.grey = "\033[90m"
        self.reset = "\033[37m"

    @staticmethod
    def fetch_time():
        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}]"

    def info(self, text):
        print(f"{self.fetch_time()} {self.grey}[~]{self.reset} {text}")

    def error(self, text):
        print(f"{self.fetch_time()} {self.red}[-]{self.reset} {text}")

    def warning(self, text):
        print(f"{self.fetch_time()} {self.yellow}[!]{self.reset} {text}")

    def success(self, text):
        print(f"{self.fetch_time()} {self.green}[+]{self.reset} {text}")

log = Logger()