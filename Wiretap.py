import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix = '!')

TOKEN = ''

@bot.event
async def on_message(message):
	msg = '\nMessage:\n     Author: ' + message.author.name + '\n     Author ID: ' + message.author.id + '\n     Content: ' + message.content + '\n     Message ID: ' + message.id + '\n     In Server: '
	if message.channel.is_private == True:
		msg = msg + 'False'
		rec = ''
		for item in message.channel.recipients:
			rec = rec + item.name + ', '
		msg = msg + '\n     Recipients: ' + rec
	else:
		msg = msg + 'True'
		msg = msg + '\n     Server Name: ' + message.server.name + '\n     Server ID: ' + message.server.id + '\n     Channel Name: ' + message.channel.name + '\n     Channel ID: ' + message.channel.id
	msg = msg + '\n     Timestamp: ' + message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
	print(msg)
	with open('wiretap.txt', 'a') as f_o:
		f_o.write(msg)
bot.run(TOKEN, bot=False)