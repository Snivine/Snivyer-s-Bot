import configparser
from os import path

if path.isfile("config.ini") and path.isfile("e621useragent.txt"): #checks wether or not the files exist
    botconfig = configparser.ConfigParser()
    botconfig.read("config.ini")

#don't hate on me python doesn't have switch cases
def getconfig(item):
    if item != "ownerid":
        return botconfig["Bot Config"].get(item)
    else:
        return botconfig["Bot Config"].getint(item)