import os
import discord
from discord.commands import Option
from dotenv import load_dotenv
import db as dbee
import asyncio

load_dotenv()

token = os.environ['DISCORD_TOKEN']

bot = discord.Bot()

async def connect_db():
    global db
    db = await dbee.database.create()

@bot.slash_command(guild_ids=[897656497826304051])
async def new_game_g(ctx, name : Option(str, "the name for your character")):
    """create a new game"""
    player_exists = await db.does_player_exist(ctx.author.id)
    if player_exists:
        await ctx.respond("you already have a character!")
    else:
        await db.create_player(ctx.author.id, name)
        await ctx.respond(f'created character {name}!')

def start_bot(token):
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(connect_db())
        loop.run_until_complete(bot.start(token))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.close())
    # cancel all tasks lingering
    finally:
        loop.close()

start_bot(token)