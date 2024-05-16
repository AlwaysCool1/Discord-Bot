from keep_alive import keep_alive
"""
Do NOT modify this file
(At least at first)

Instead, modify the functions in `my_bot.py`
"""

import os
import discord
import my_bot

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print(f"Bot logged in as {client.user}")


@client.event
async def on_message(message):
    if message.channel.name == "nabils-bot":
        if message.author != client.user:
            user_name = message.author.display_name
            if my_bot.should_i_respond(message.content, user_name):
                if message.content.startswith('!joke'):
                    response = my_bot.get_random_joke()
                else:
                    response = my_bot.respond(message.content, user_name)
                await message.channel.send(response)
keep_alive()
my_secret = os.environ['DISCORD_BOT_SECRET']
client.run(my_secret)