# Should I remove this thing? Since really this is not a template anymore

from discord.ext import commands


# For more information on commands, see
# https://discordpy.readthedocs.io/en/latest/api.html#event-reference
class ExampleEvent(commands.Cog):
    """
    Sends "Welcome!" in the system channel when a member joins the guild.
    """

    # Cog constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel

        if channel is not None:  # if the system channel is set
            await channel.send('Welcome!')


# Constructor for loading the cog
def setup(bot):
    bot.add_cog(ExampleEvent(bot))
