from discord.ext import commands


# For more information on commands, see
# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
class ExampleCommand(commands.Cog):
    """
    Pings the command sender and repeats the arguments it was given to them
    """

    # Cog constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def examplecommand(self, ctx, *args):
        message = 'Hello, {}! I recieved {} arguments with this command: {}.'.format(
            ctx.author.mention,  # Used to @ someone
            len(args),  # Length of args
            ', '.join(args)  # Prints the arguments with a comma and a space as a separator for each
        )

        # Sending the finalized message
        await ctx.send(message)


# Constructor for loading the cog
def setup(bot):
    bot.add_cog(ExampleCommand(bot))
