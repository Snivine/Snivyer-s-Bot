###
#imports
###

import discord
from discord.ext import commands
from random import randint
import random
import asyncio

###
#random gen
###

emoji = "🏳️‍🌈"


###
#acutal command
###

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetch the ammount of gayness of a person")
    async def gay(self, ctx, *, arg=None):
        possibilites = [randint(0, 100)] * 90 + ["999"] * 4 + ["255"] * 4 + ["`yes.`"] * 1
        gaynumber = random.choice(possibilites)

        # If no argument passed, set the phrase to "You are"
        phrase = "You are" if arg is None else f"{arg} is"

        await ctx.send(f"{phrase} {gaynumber}% gay {emoji}")
        print(f"Generated gay number: {gaynumber}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))

###
#Notes
###

#THIS IS DEFINETLY NOT PRODUCTION READY, SINCE THIS IS A HACKY WORKAROUND, EXPECT BUGS
