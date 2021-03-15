###
# Imports
###

from util.embed import cooldownerror

from asyncio import sleep


###
# Functions
###

async def cooldownhandler(error, ctx, cooldown, cooldownblacklist):
    if ctx.author not in cooldownblacklist:
        cooldownblacklist.append(ctx.author)
        await ctx.send(embed=cooldownerror(error.retry_after))
        await sleep(cooldown)
        cooldownblacklist.remove(ctx.author)
