###
# Imports
###

from discord.ext import commands, tasks
import discord
from asyncio import sleep


###
# Cog Configuration
###

pausetime = 20


###
# Cog
###

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuschanger.start()

    @tasks.loop(seconds=pausetime)
    async def statuschanger(self):
        await self.bot.change_presence(activity=discord.Game(name='Serving my owner Snivyer'))
        await sleep(pausetime)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='My owner developing me'))
        await sleep(pausetime)

    @statuschanger.before_loop
    async def before_statuschanger(self):
        await self.bot.wait_until_ready()


###
# Setup Cog
###
def setup(bot):
    bot.add_cog(status(bot))
