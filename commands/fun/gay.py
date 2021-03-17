###
#imports
###

from discord.ext import commands
import random

###
#random gen
###

emoji = "🏳️‍🌈"

###
#acutal command
###

class gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Fetch the ammount of gayness of a person")
    async def gay(self, ctx, *, arg=None):
        messagetypes = ["Normal"] * 9999 + ["Meme"] * 1
        randommessage = random.choice(messagetypes) #This took me more than it needed to.
        # no, really, this shit doesn't accept floats and I was trying to use floats

        if randommessage == "Meme":
            await ctx.send("Idk man ask them lmao") #suggested by Floofy Foxor and MrRhino
        else:
             possibilites = [random.randint(0, 100)] * 9799 + ["999"] * 100 + ["255"] * 100 + ["Yes."] * 1
             gaynumber = random.choice(possibilites) #Tried a lot of methods to get this to work, then noticed I'm stupid

             # If no argument passed, set the phrase to "You are"
             phrase = "You are" if arg is None else f"{arg} is"

             await ctx.send(f"{phrase} {gaynumber}% gay {emoji}")
             print(f"Generated gay number: {gaynumber}")

###
# Cog
###

def setup(bot):
    bot.add_cog(gay(bot))

###
#Notes
###

#Reperak bad developer /s
