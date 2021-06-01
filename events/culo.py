from discord.ext import commands

class culo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "culo" in message.content:
            await message.channel.send("culo")


def setup(bot):
    bot.add_cog(culo(bot))
