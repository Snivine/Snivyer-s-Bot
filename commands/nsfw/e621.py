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
            tags = content.split(",")
            url = "https://e621.net/posts.json?tags="

            for t in tags:
                url += t + "+"

            url += f"&max=16&page={randpage}"

            user_agent = { "User-agent": "Snivyer's Maid/0.1.0 (by Snivyer1910)" }

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

def setup(bot):
    bot.add_cog(e621(bot))

#fixed some shit and made it random, thanks to my friendo to help me with this
