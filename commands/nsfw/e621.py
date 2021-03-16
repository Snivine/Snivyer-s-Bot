#Imports
import discord
from discord.ext import commands
from util.embed import errorbox
from util.cooldownhandler import cooldownhandler
import json
import requests
from random import randint

# Cache
user_agent = { "User-agent": "Snivyer's Maid/0.1.0 (by Snivyer1910)" }
cooldownblacklist = []
#Actual command

limit = 4
cooldown = 10

class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(limit, cooldown, commands.BucketType.user)
    @commands.command(description="Fetches a post from e621")
    async def e621(self, ctx, *, content):
        if not ctx.channel.is_nsfw():
           await ctx.send("This is a NSFW-only Command")
           return

        tags = content.split(",")
        url = "https://e621.net/posts.json?tags="

        for t in tags:
            url += t + "+"

        url += f"&max=319&page=1"

        print(url)
        res = requests.get(url, headers = user_agent)
        posts = json.loads(res.text)

        randPost = randint(0, len(posts["posts"]) - 1)

        post = posts["posts"][randPost]
        postUrl = post["file"]["url"]

        # Create embed

        postEmbed = discord.Embed(color=discord.Color.blue())
        postEmbed.set_author(name=ctx.author.display_name, url=discord.Embed.Empty, icon_url=ctx.author.avatar_url)
        postEmbed.set_image(url=postUrl)
        postEmbed.set_footer(text=f"Tags: {content} • Score {post['score']['total']}" )

        await ctx.send(embed=postEmbed)
    @e621.error
    async def e621_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await cooldownhandler(error, ctx, cooldown, cooldownblacklist)


def setup(bot):
    bot.add_cog(e621(bot))

#fixed some shit and made it random, thanks to Isfy/Lifo to help me with this
