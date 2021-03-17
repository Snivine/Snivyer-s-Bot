from discord.ext import commands
from config import getarg
from cogregister import commandregister, eventregister
import os

# Creates two types of bots based on the value of the --no-auto-sharding flag
if getarg('no_auto_sharding'):
    bot = commands.Bot
else:
    bot = commands.AutoShardedBot

# Initialize method into bot object
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

# Confirmation of running
print(f"Process is running with PID = {os.getpid()}")