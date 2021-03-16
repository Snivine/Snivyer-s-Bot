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
            await ctx.send(f"{arg} is {ammount}% gay {emoji}")

###
#non-argument command (workaround)
###

@gay.error
async def gay_error(ctx, error):
    if isinstance(error,discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f"You are {ammount}% gay {emoji}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))

###
#Notes
###

#THIS IS DEFINETLY NOT PRODUCTION READY, SINCE THIS IS A HACKY WORKAROUND, EXPECT BUGS