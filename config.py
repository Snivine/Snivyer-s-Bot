import configparser
from os import path
from ast import literal_eval

if path.isfile("config.ini") and path.isfile("e621useragent.txt"): #checks wether or not the files exist
    botconfig = configparser.ConfigParser()
    botconfig.read("config.ini")
    e6useragent = open("e621useragent.txt", "r")
    user_agent = e6useragent.read()
    e621useragent = literal_eval(user_agent)


#don't hate on me python doesn't have switch cases
def getconfig(item):
    if item != "ownerid":
        return botconfig["Bot Config"].get(item)
    elif item == "e621useragent":
        return e621useragent # Put the user agent in this format: {"User-Agent": "Your User Agent / Your version (By "You")}
    else:
        return botconfig["Bot Config"].getint(item)