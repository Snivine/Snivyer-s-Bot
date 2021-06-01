###
# Imports
###

from config import getconfig

from discord.ext import commands
import discord

###
# Cache
###

prefix = getconfig('prefix')
embed = discord.Embed(
    title="Snivyer's Maid",
    description=f'My prefix is `{prefix}` . Type `{prefix}help` for a list of my commands.'
)

###
# Cog
###

class pingdialog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(embed=embed)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(pingdialog(bot))
