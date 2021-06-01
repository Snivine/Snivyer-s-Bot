#Imports
import discord
from discord.ext import commands
import json
import requests
from random import randint
from ast import literal_eval

#dynamic user agent
e6useragent = open("e621useragent.txt", "r")
agent = e6useragent.read()
user_agent = literal_eval(agent)

#command

class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=f'nsfw~Fetches a post from e621~e621 `<tags>`')
    async def e621(self, ctx, *, content=None):
        if not ctx.channel.is_nsfw(): #checks if the channel is nsfw
            await ctx.send("This is a NSFW-only Command")
            return
        if content is None: #checks if the content is empty
            await ctx.send("You must provide a set of tags")
            return

        #fetches the post based on tags
        tags = content.split(",")
        url = "https://e621.net/posts.json?tags="

        for t in tags:
            url += t + "+"

        url += f"&max=319&page=1"

        print(url) #do we need this?
        res = requests.get(url, headers=user_agent)
        posts = json.loads(res.text)

        randPost = randint(0, len(posts["posts"]) - 1)

        post = posts["posts"][randPost]
        postUrl = post["file"]["url"]

        # Create embed

        postEmbed = discord.Embed(color=discord.Color.blue())
        postEmbed.set_author(name=ctx.author.display_name, url=discord.Embed.Empty, icon_url=ctx.author.avatar_url)
        postEmbed.set_image(url=postUrl)
        postEmbed.set_footer(text=f"Tags: {content} • Score {post['score']['total']}")

        await ctx.send(embed=postEmbed)

#cog

def setup(bot):
    bot.add_cog(e621(bot))

#fixed some shit and made it random, thanks to Isfy/Lifo to help me with this
#Implemented Reperak's changes, thanks bro
