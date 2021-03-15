#Imports
import discord
from discord.ext import commands
#import insert e621 api here

#ples end me I can't find API

#Actual command

class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetches a post from e621")
    async def e621(self, ctx, *, content):
        if not ctx.channel.is_nsfw():
            ctx.send("This is a NSFW-only Command")
        elif content == "":
            ctx.send("You have to input a set of tags to search")
        else:

