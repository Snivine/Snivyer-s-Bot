###
# These things are bugged the issue is that I don't know how to check for this literally
###

from discord.ext import commands

### 
# Command
###

class teta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "teta":
            await message.channel.send("teta")

###
# Setup Command
###

def setup(bot):
    bot.add_cog(teta(bot))