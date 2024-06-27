import os
import discord
from config import DISCORD_TOKEN
from bot_logic import process_message, log_interaction, rate_limited

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user = str(message.author)
    user_message = message.content
    
    if rate_limited(user):
        await message.channel.send("You are sending messages too quickly. Please wait a while before trying again.")
        return
    
    response = process_message(user_message)
    log_interaction('Discord', user, user_message, response)
    await message.channel.send(response)

def start_discord_bot():
    client.run(DISCORD_TOKEN)
