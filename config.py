# If you're looking to expand upon the arguments, https://docs.python.org/3/library/argparse.html may be useful to you.
from argparse import ArgumentParser
__parser = ArgumentParser()

# Essential configuration (e.g. token, prefix)
__botdetails = __parser.add_argument_group('bot details')
__botdetails.add_argument('-t', '--token', type=str, help='token for the bot')
__botdetails.add_argument('-p', '--prefix', type=str, default='%', help='prefix for the bot')
__botdetails.add_argument("-gh", "--ghtoken", type=str, help="github token")
__botdetails.add_argument("-e6u", "--e621useragent", type=str, help="e621 user agent")

# Tuning configuration (e.g. disabling sharding)
__bottuning = __parser.add_argument_group('bot tuning')
__bottuning.add_argument('--no-auto-sharding', action='store_true', help='disable sharding')

args = vars(__parser.parse_args())


def getarg(argname: str):
    """
    Returns the value of a commandline argument.

    :param argname: Argument value to fetch
    :type argname: str
    """

    return args[argname]
