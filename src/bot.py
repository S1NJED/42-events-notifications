import discord
from discord.ext import tasks, commands
import os
import asyncio
from dotenv import load_dotenv
import argparse
import logging
from utils import db_query

parser = argparse.ArgumentParser()
parser.add_argument("--mode")
args = parser.parse_args()
mode = args.mode

LOOP_INTERVAL_SECONDS = 60 if mode == "prod" else 10

class Bot(commands.Bot):
	
	def __init__(self, *args, **kwargs):
		self.letterboxd_text_channel = None
		self.loop_running = False
		super().__init__(*args, **kwargs)
	
	async def setup_hook(self):
		self.db_path = "database/db.sqlite" if mode == "prod" else "database/db_dev.sqlite"
		if not os.path.exists(self.db_path):
			raise FileNotFoundError(f"Database does not exist, create it")

		self.letterboxd_check_task.start()

		for file in os.listdir("src/cogs"):
			try:
				if file.endswith(".py"):
					await self.load_extension(f"cogs.{file.removesuffix(".py")}")
					print(f"Sucessfully loaded {file} cog")
			except discord.ext.commands.errors.ExtensionAlreadyLoaded as err:
				print(err)
				print(f"{file} cog is already loaded")
			except Exception as err:
				raise err
		

	async def on_ready(self):
		print(f"Bot is ready: {self.user}")

load_dotenv()
tokens = {
	"prod": os.getenv("DISCORD_BOT_TOKEN"),
	"dev": os.getenv("DISCORD_BOT_TOKEN_DEV")	
}

# by default prod if not specified
if not mode:
	mode = "prod"


handler = logging.FileHandler(filename="log", encoding="utf-8", mode="w")
client = Bot(intents=discord.Intents.all(), log_handler=handler, command_prefix="!" ) # change all
client.run( tokens[mode] )