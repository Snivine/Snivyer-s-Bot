from discord.ext import commands

### 
# Command
###

class paco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "paco":
            await message.channel.send("es puto")

###
# Setup Command
###

def setup(bot):
    bot.add_cog(paco(bot))