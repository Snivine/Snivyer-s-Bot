###
# Imports
###

import discord
from discord.ext import commands

from util.embed import errorbox
from util.cooldownhandler import cooldownhandler

import owoify as pyowoify


###
# Cooldown Blacklist
###

cooldownblacklist = []  # Apparently lists have O(n) complexity? Oh well!


###
# Cooldown Settings
###

limit = 5
cooldown = 10


###
# Cog
###

class owoify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(limit, cooldown, commands.BucketType.user)
    @commands.command(description=f'fun~OwOify your text!~owoify `<text>/<"reply">`')
    async def owoify(self, ctx, *, content):
        if ctx.author in cooldownblacklist:
            return
        if content == 'reply':
            try:
                message = ctx.message.reference.resolved.content
            except AttributeError:
                await ctx.send(embed=errorbox('Unable to get reply.'))
                return
        else:
            message = content

        message = pyowoify.owoify(message)

        try:
            await ctx.reply(message, mention_author=False)
        except discord.HTTPException:
            await ctx.send(embed=errorbox('Unable to send message.'))
            return

    @owoify.error
    async def owoify_error(self, ctx, error):
        await cooldownhandler(error, ctx, cooldown, cooldownblacklist)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(owoify(bot))
