###
# Imports
###

from discord.ext import commands

###
# Command
###

class culo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "culo":
            await message.channel.send("culo")

###
# Setup Command
###

def setup(bot):
    bot.add_cog(culo(bot))
