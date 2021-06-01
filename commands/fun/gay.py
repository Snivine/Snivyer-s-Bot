#imports

from discord.ext import commands
import random
from config import getarg

#prefix

prefix = getarg("prefix")

#command

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=f'fun~Fetch how gay is someone~gay `<user>`')
    async def gay(self, ctx, *, arg=None):
        messagetypes = "Meme", "Normal"
        randommessage = random.choices(messagetypes, weights=[99, 1])

        if randommessage == "Meme":
            await ctx.send("Idk man ask them lmao")
        else:
             possibilites = random.randint(0, 100), "999", "Infinity", "Yes."
             gaynumber = random.choices(possibilites, weights=[95.9, 2, 2, 0.1])

             # If no argument passed, set the phrase to "You are"
             phrase = "You are" if arg is None else f"{arg} is"

             await ctx.send(f"{phrase} {str(gaynumber)[1:-1]}% gay 🏳️‍🌈")

#cog

def setup(bot):
    bot.add_cog(gay(bot))

#Reperak bad developer /s
