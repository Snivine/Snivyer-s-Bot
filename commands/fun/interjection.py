#imports

import discord
from discord.ext import commands
from asgiref.sync import sync_to_async
from util.cooldownhandler import cooldownhandler


#cache

copypasta = 'I\'d just like to interject for a moment. What you\'re referring to as Linux, is in fact, GNU/Linux, ' \
            'or as I\'ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, ' \
            'but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, ' \
            'shell utilities and vital system components comprising a full OS as defined by POSIX.\n\nMany computer ' \
            'users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn ' \
            'of events, the version of GNU which is widely used today is often called "Linux", and many of its users ' \
            'are not aware that it is basically the GNU system, developed by the GNU Project.\n\nThere really is a ' \
            'Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: '\
            'the program in the system that allocates the machine\'s resources to the other programs that you run. ' \
            'The kernel is an essential part of an operating system, but useless by itself; it can only function in ' \
            'the context of a complete operating system. Linux is normally used in combination with the GNU operating '\
            'system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called "Linux" ' \
            'distributions are really distributions of GNU/Linux. '


###
# Cooldown Blacklist
###

cooldownblacklist = []


###
# Cooldown Settings
###

limit = 4
cooldown = 30


###
# Functions
###

@sync_to_async()
def copypastaify(gnu_replacement, linux_replacement):
    return copypasta.replace('GNU', gnu_replacement).replace('Linux', linux_replacement)


###
# Cog
###

class interjection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(limit, cooldown, commands.BucketType.user)
    @commands.command(description=f'fun~Make a custom GNU/Linux copypasta.~interjection `<word1>/<word2>`')
    async def interjection(self, ctx, *, args):

        splittext = str(args).split('/')
        finalized = await copypastaify(splittext[0], splittext[1])

        embed = discord.Embed(
            title=str(args),
            description=finalized
        )

        await ctx.send(embed=embed)

    @interjection.error
    async def interjection_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await cooldownhandler(error, ctx, cooldown, cooldownblacklist)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(interjection(bot))
