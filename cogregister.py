# To register or unregister a cog, place the location of the object in the relevant list.
#
# To load a cog located in "<PROJECT DIRECTORY>/commands/examplecommand.py", you would insert "commands.examplecommand"
# into the appropriate list, omitting the .py file extension.
#
# If a command/event you've added doesn't load, check this file to see if you've forgotten to register the cog.
# Note: events is also intended to be used for tasks, as well.

commandregister = [
    'commands.examplecommand'
]

eventregister = [
    'events.exampleevent'
]
