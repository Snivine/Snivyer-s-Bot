###
# Imports
###

import discord


###
# Functions
###

def errorbox(message):
    embed = discord.Embed(
        title=':exploding_head: Yikes! An error occured.',
        description=str(message)
    )

    return embed


def cooldownerror(timeremaining):
    embed = discord.Embed(
        title=':ice_cube: Looks like you\'re on cooldown.',
        description=f'Try again in {round(timeremaining)} seconds.'
    )

    return embed
