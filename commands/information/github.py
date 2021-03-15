###
# Imports
###

import discord
from discord.ext import commands

from config import getarg
from util.embed import errorbox
from util.cooldownhandler import cooldownhandler

import github as pygithub


###
# Objects
###

githubobject = pygithub.Github(
    getarg('ghtoken')
)


###
# Cooldown Blacklist
###

cooldownblacklist = []


###
# Cooldown Settings
###

limit = 2
cooldown = 15


###
# Cog
###

class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(limit, cooldown, commands.BucketType.user)
    @commands.command(description='information~Gets info about a GitHub repo~github <owner>/<repo>')
    async def github(self, ctx, arg):
        if ctx.author in cooldownblacklist:
            return
        try:
            repo = githubobject.get_repo(arg)
        except pygithub.UnknownObjectException:  # UnknownObjectException is a dumb way of saying "not found"
            await ctx.send(embed=errorbox('I couldn\'t find that repo. Have you checked for typos?'))
            return

        repoembed = discord.Embed()

        repoembed.title = repo.name
        repoembed.description = repo.description
        repoembed.url = repo.html_url

        # Author
        repoembed.set_author(
            name=repo.owner.name,
            url=repo.owner.url,
            icon_url=repo.owner.avatar_url
        )

        # License
        repoembed.add_field(
            name='License',
            value=repo.get_license().license.name,
            inline=True
        )

        # Language
        repoembed.add_field(
            name='Most-used Language',
            value=repo.language,
            inline=True
        )

        # Open PRs
        repoembed.add_field(
            name='Open PRs',
            value=str(repo.get_pulls().totalCount),
            inline=True
        )

        # Open Issues
        repoembed.add_field(
            name='Open Issues',
            value=str(repo.open_issues_count - repo.get_pulls().totalCount),
            inline=True
        )

        # Watchers
        repoembed.add_field(
            name='Watchers',
            value=str(repo.subscribers_count),
            inline=True
        )

        # Stars
        repoembed.add_field(
            name='Stars',
            value=str(repo.stargazers_count),
            inline=True
        )

        # Forks
        repoembed.add_field(
            name='Forks',
            value=str(repo.forks_count),
            inline=True
        )

        # Remember the bot!
        repoembed.set_footer(
            text='Beep boop. I\'m still in beta.\nCheck out my source code at https://github.com/ReperakPro/Botperak.'
        )

        await ctx.send(embed=repoembed)

    @github.error
    async def github_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await cooldownhandler(error, ctx, cooldown, cooldownblacklist)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(github(bot))