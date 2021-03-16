###
#imports
###

import discord
from discord.ext import commands
from random import randint
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
        gaynumber = randint(0, 100)

        # If no argument passed, set the phrase to "You are"
        phrase = "You are" if arg is None else f"{arg} is"

        await ctx.send(f"{phrase} {gaynumber}% gay {emoji}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))

###
#Notes
###

#THIS IS DEFINETLY NOT PRODUCTION READY, SINCE THIS IS A HACKY WORKAROUND, EXPECT BUGS
