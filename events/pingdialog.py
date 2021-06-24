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

###
# Cog
###

class pingdialog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        embed = discord.Embed(
            color=discord.Color.random(),
            title="Snivyer's Maid",
            description=f'My prefix is `{prefix}` . Type `{prefix}help` for a list of my commands.'
        )
        if self.bot.user.mentioned_in(message):
            await message.channel.send(embed=embed)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(pingdialog(bot))
