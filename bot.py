import os

os.system("pip install DiscordUtils")

import discord
from discord.ext import commands
from startServer import FifiServer

TOKEN = ...

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'o.', intents=intents, help_command=commands.MinimalHelpCommand(), activity=discord.Activity(type = discord.ActivityType.playing, name = 'o.help | Helping the Server | https://discord.gg/3c5kc8M'), owner_ids=[621266489596444672, 699839134709317642, 737478714048380939], case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} Has Logged In And Is Online!')

@bot.event
async def on_guild_join(guild): #To block guilds from joining
  for channel in guild.text_channels:
    try:
      await channel.send("Sorry, this server is not whitelisted.")
      break
    except:
      pass

  await guild.leave()

server = FifiServer(bot)

bot.load_extension('cogs.music')

server.start()

bot.run(TOKEN)
