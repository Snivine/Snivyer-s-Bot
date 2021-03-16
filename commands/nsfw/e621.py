#Imports
import discord
from discord.ext import commands
import json
import requests
from random import randint

#Actual command

class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetches a post from e621")
    async def e621(self, ctx, *, content):
        if not ctx.channel.is_nsfw():
           await ctx.send("This is a NSFW-only Command")
        else:
            randpage = randint(1, 30)
            randpost = randint(0, 15)
            tags = content.split(",")
            url = "https://e621.net/posts.json?tags="

            for t in tags:
                url += t + "+"

            url += f"&max=16&page={randpage}"

            user_agent = { "User-agent": "Snivyer's Maid" }

            print(url)
            res = requests.get(url, headers = user_agent)
            posts = json.loads(res.text)
            await ctx.send(posts["posts"][randpost]["file"]["url"])

def setup(bot):
    bot.add_cog(e621(bot))

#fixed some shit and made it random, thanks to my friendo to help me with this