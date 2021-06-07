"""
MIT License

Copyright (c) 2021 Meme Studios

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sellcopies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

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

extensions = [
    'cogs.music',
    'cogs.owner'
]

server.start()

bot.run(TOKEN)
