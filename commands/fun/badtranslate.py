###
# Imports
###

import discord
from discord.ext import commands
from util.embed import errorbox
from util.cooldownhandler import cooldownhandler
from asgiref.sync import sync_to_async
from random import choice
import googletrans
from googletrans import Translator
import httpx
from httpx import Timeout


###
# Server
###

translator = Translator(service_urls=[
      'translate.google.us'
    ])

###
# Cache
###

translator = Translator(timeout=Timeout(30))
languagelist = list(googletrans.LANGUAGES.keys())


###
# Cooldown Blacklist
###

cooldownblacklist = []


###
# Cooldown Settings
###

limit = 3
cooldown = 30


###
# Functions
###

def resettranslator():
    global translator
    global languagelist

    del translator
    del languagelist

    translator = Translator(timeout=Timeout(30))
    languagelist = list(googletrans.LANGUAGES.keys())


@sync_to_async()
def process(_input, count: int):
    queue = []

    # Generate map of target languages
    cycle = 0
    while cycle < count:
        candidate = choice(languagelist)
        if candidate not in queue:
            queue.append(candidate)
            cycle = cycle + 1

    # Translation phase
    _output = _input
    for language in queue:
        _output = translator.translate(_output, dest=language).text
    _output = translator.translate(_output, dest='en').text

    # Return processed text
    return _output


###
# Cog
###

class badtranslate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(limit, cooldown, commands.BucketType.user)
    @commands.command(description=f'fun~Runs text through Google Translate five times through random languages to '
                                  f'completely ruin it.~badtranslate <text/"reply">')
    async def badtranslate(self, ctx, *, content):
        if ctx.author in cooldownblacklist:
            return

        if content == 'reply':
            try:
                response = ctx.message.reference.resolved.content
            except AttributeError:
                await ctx.send(embed=errorbox('Unable to get reply.'))
                return
        else:
            response = content

        # Actual translation bit
        try:
            response = await process(response, 5)
        except httpx.ReadTimeout:
            await ctx.send(embed=errorbox(
                'The translation timed out. Attempting to reset the client; try again in a few seconds.'
            ))

            resettranslator()
            return

        # Sending message
        try:
            await ctx.reply(response, mention_author=False)
        except discord.HTTPException:
            await ctx.send(embed=errorbox('Unable to send message.'))
            return

    @badtranslate.error
    async def badtranslate_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await cooldownhandler(error, ctx, cooldown, cooldownblacklist)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(badtranslate(bot))
