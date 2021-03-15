# waffle
A libre framework for creating Discord.py bots. Simple, structured, and painless.

## Making a command
1. Create a Python file in the [command folder](commands)
2. Write the command inside [a cog](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html)
3. Register your command in [cogregister.py](cogregister.py)

## Running
Install Discord.py - `$ pip3 install discord.py`

Running the bot - `$ python3 waffle.py -t <TOKEN> -p <PREFIX>`
