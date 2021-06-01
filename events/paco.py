from discord.ext import commands

class paco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "paco" in message.content:
            await message.channel.send("es puto")


def setup(bot):
    bot.add_cog(paco(bot))