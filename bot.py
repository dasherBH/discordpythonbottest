import discord 
from discord.ext import commands

token = "" 

bot = commands.Bot(command_prefix='.')

@bot.event()
aysinc def on_ready():
  print("Bot Is Ready")
  
  
bot.run(token)
