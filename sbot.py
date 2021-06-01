from discord.ext import commands
from cogregister import commandregister, eventregister
from config import getconfig
import os
import logging
import configparser

#this is most definitely not the way, but this is how Imma do it for now till I figure things out
logging.basicConfig(level=logging.INFO)

if not os.path.isfile("config.ini") and not os.path.isfile("e621useragent.txt"):
    botconfig = configparser.ConfigParser()

    botconfig["Bot Config"] = {
        "token": "tokenhere",
        "githubtoken": "tokenhere",
        "ownerid": "owneridhere",
        "prefix": "prefixhere"
    }

    with open('config.ini', 'w') as conf:
        botconfig.write(conf)
    open('e621useragent.txt', 'w')
    print("Config files created, please read and edit very carefully to make sure that the bot works")
    exit()
else:
     print(f"Process is running with PID = {os.getpid()}")

     bot = commands.AutoShardedBot

     bot = bot(command_prefix=getconfig('prefix'),
     help_command=None
)

     for x in commandregister:
         bot.load_extension(x)
     for x in eventregister:
         bot.load_extension(x)

     bot.run(
        getconfig('token')
)
     bot.owner_id(
        getconfig("ownerid")
)