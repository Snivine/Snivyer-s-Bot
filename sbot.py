from discord.ext import commands
from config import getarg
from cogregister import commandregister, eventregister
from os import getpid
import logging

#this is most definitely not the way, but this is how Imma do it for now till I figure things out
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARN)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.CRITICAL)

print(f"Process is running with PID = {getpid()}")

if getarg('no_auto_sharding'):
    bot = commands.Bot
else:
    bot = commands.AutoShardedBot

bot = bot(command_prefix=getarg('prefix'),
    help_command=None
)



# Loading cogs from register
for x in commandregister:
    bot.load_extension(x)
for x in eventregister:
    bot.load_extension(x)


# Running
bot.run(
    getarg('token')
)
