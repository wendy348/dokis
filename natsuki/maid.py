import discord, os, traceback, random, chalk
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from Cogs.config import conf
#Import some important modules
if conf.sharding is True:
    client = commands.AutoShardedBot(command_prefix=conf.prefix, status=discord.Status.do_not_disturb, activity=discord.Game(name="Starting..."), shard_count=2, shard_ids=(0, 1)) # Defining what our prefix for the bot will be
elif conf.sharding is False:
    client = commands.Bot(command_prefix=conf.prefix, status=discord.Status.do_not_disturb, activity=discord.Game(name="Starting...")) # Defining what our prefix for the bot will be


Cogs = conf.cogd

if __name__ == '__main__': # Load every file that have a .py extension in the Cogs folder
    for extension in [f.replace('.py', '') for f in listdir(Cogs) if isfile(join(Cogs, f))]:
        try:
            if extension == "config" or extension == "checks":
                pass
            else:   
                client.load_extension(Cogs + "." + extension) # Here's were we load them
                print(chalk.green(f"Loaded {extension}"))
        except (discord.ClientException, ModuleNotFoundError): # Oh fuck something happened lets reppoooooorrrrrt it!!!!111111!!!!!!
            crash_thing = traceback.format_exc()
            print(chalk.red(f'Failed to load extension {extension}', file=sys.stderr))
            ono = traceback.format_exc()
            print(chalk.red(ono))
            print("\n")
            continue

client.run(conf.token, reconnect=True) # Login via our token inside of the config file
