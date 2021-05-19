import os
import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  print("Bot Is Ready")
  print(bot.user.name)


  
  
bot.run(os.environ['DISCORD_TOKEN'])
