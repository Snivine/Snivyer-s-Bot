import discord
from discord.ext import commands
from config import getarg
from util.embed import errorbox

prefix = getarg('prefix')

#command

class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=f'information~Get help and syntax for commands.~help `<category/command>`')
    async def help(self, ctx, arg=None):
        cmdlist = {}

        categories = {
            'information': {
                'name': ':thinking: Information',
                'description': 'Retrieve information from the internet.',
                'commands': []
            },
            'fun': {
                'name': ':zany_face: Fun',
                'description': 'Commands for fun that have no practical use.',
                'commands': []
            },
            "nsfw": {
                "name": ":: NSFW",
                "description": "For horny stuff",
                "commands": []
            }
        }

        for command in self.bot.commands:
            cmdlist[str(command)] = {
                'name': str(command),
                'category': command.description.split('~')[0],
                'description': command.description.split('~')[1],
                'usage': command.description.split('~')[2]
            }
            tmpcmd = cmdlist[str(command)]
            categories[tmpcmd['category']]['commands'].append(tmpcmd)

        helptype = None

        if not arg:
            helptype = 0
        elif arg in categories:
            helptype = 1
        else:
            await ctx.send(embed=errorbox('Unknown category/command.'))
            return

        # Embed stuff
        embed = discord.Embed()

        embed.title = [
            'Help - Category List',
            'Help - Command List'
        ][helptype]

        if helptype == 0:
            for x in categories.keys():
                item = categories[x]

                embed.add_field(
                    name=str(item['name']),
                    value=str(item['description']) + '\n\n' + f'Run `{prefix}help {x}` for more info.',
                    inline=True
                )
        elif helptype == 1:
            embed.description = 'Note: for command syntax, arguments surrounded by asterisks `*<argument>*` are ' \
                                'optional. Arguments that have double quotes `<"argument">` around them means that is ' \
                                'what you type to use that argument.'

            for x in categories[arg]['commands']:
                item = dict(x)

                embed.add_field(
                    name=':arrow_right:   ' + prefix + item['name'],
                    value=item['description'] + '\n\n' + 'Usage: ' + item['usage'] + ''
                )

        await ctx.send(embed=embed)

#cog

def setup(bot):
    bot.add_cog(helpcommand(bot))
