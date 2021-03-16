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

ammount = random.randint(1, 100)
emoji = "🏳️‍🌈"

###
#acutal command
###

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetch the ammount of gayness of a person")
    async def gay(self, ctx, *, arg):
        if arg == "":
            await ctx.send("You are {ammount}% gay {emoji}")
        else:
            await ctx.send("{arg} is {ammount}% gay {emoji}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))
