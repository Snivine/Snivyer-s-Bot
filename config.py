###
# Imports
###

import configparser
from os import path

###
# Load the config file
### 

if path.isfile("config.ini") and path.isfile("e621useragent.txt"): # Checks wether or not the files exist
    botconfig = configparser.ConfigParser()                        # If they don't exist the bot crashes
    botconfig.read("config.ini")                                   # Under no circumstance this should be the case, but I should still add a failsafe for it

###
# Get the config from the parsed configs
###

# To get the config item you need simply import the config, then use the getconfig def to get the requiered config

def getconfig(item):
    if item != "ownerid":
        return botconfig["Bot Config"].get(item)
    else:
        return botconfig["Bot Config"].getint(item)