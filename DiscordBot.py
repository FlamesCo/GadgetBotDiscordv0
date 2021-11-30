### this is a test bot that says hello when a user joins the server and greets them
import nextcord
import os
import discord
import os 
import sys 
import asyncio
import time
import random
import json
import requests
def main():
    client = discord.Client()
    token = os.environ['****************']
    client.run(token)

    def Greeting(message):  # this is the greeting function
        if message.content.startswith('!hello'):
            channel = message.channel
            channel.send('Hello!')
            ## IF A new user joins the server display their discord tag and greet them
            if message.author.bot == False:
                channel.send('Welcome ' + message.author.mention + ' to the server!')
                channel.send('Please read the rules and guidelines in #rules-and-guidelines')
                channel.send('If you have any questions, please ask a moderator or admin')
