###
#imports
###

import discord
from discord.ext import commands
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
    async def gay(self, ctx, *, arg):
        if arg == None:
            ammount = random.randint(1, 100)
            await ctx.send(f"You are {ammount}% gay {emoji}")
        else:
            ammount = random.randint(1, 100)
            await ctx.send(f"{arg} is {ammount}% gay {emoji}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))

###
#Notes
###

#THIS IS DEFINETLY NOT PRODUCTION READY, SINCE THIS IS A HACKY WORKAROUND, EXPECT BUGS