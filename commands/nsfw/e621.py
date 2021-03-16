#Imports
import discord
from discord.ext import commands
import json
import requests

#ples end me I can't find API

#Actual command

class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetches a post from e621")
    async def e621(self, ctx, *, content):
        if not ctx.channel.is_nsfw():
           await ctx.send("This is a NSFW-only Command")
        else:
            tags = content.split(",")
            url = "https://e621.net/posts.json?tags="

            for t in tags:
                url += t + "+"

            url += "&max=5&page=1"

            user_agent = { "User-agent": "Snivyer's Maid" }

            print(url)
            res = requests.get(url, headers = user_agent)
            posts = json.loads(res.text)
            await ctx.send(posts["posts"][0]["file"]["url"])

def setup(bot):
    bot.add_cog(e621(bot))