from discord.ext import commands

class teta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "teta" in message.content:
            await message.channel.send("teta")


def setup(bot):
    bot.add_cog(teta(bot))