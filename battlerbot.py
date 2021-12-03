import os
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.environ['DISCORD_TOKEN']

bot = discord.Bot()

bot.run(token)
