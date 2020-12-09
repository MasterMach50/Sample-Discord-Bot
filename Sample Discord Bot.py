import time
import sys
import random
import discord
from discord.ext import commands, tasks
from itertools import cycle
#==================================================
#command_prefix is the prefix for all the bot commands
client = commands.Bot(command_prefix = ".")
#==================================================
#client.event is used for events and client.command is used to read the commands from discord
@client.event
async def on_ready():
    print("Bot is Ready.")
    await change_status.start()
#==================================================
#command for terminating the program
@client.command()
async def terminate(ctx):
    await sys.exit()

#command for checking ping
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

#command for getting invite link of bot
@client.command()
async def invite(ctx):
    await ctx.send("<INSERT INVITE LINK HERE>")

#command for fun!
@client.command()
async def test(ctx):
    await ctx.send("I'm alright")

#command for fun!
@client.command()
async def ting(ctx):
    await ctx.send("tong")

#command for 8ball
@client.command(aliases=["8ball"])
async def _8ball(ctx,*,question):
    responses = ["It is certain.",#yes
    "Without a doubt.",#yes
    "Yes, definitely.",#yes
    "You may rely on it.",#yes
    "As I see it, yes.",#yes
    "Most likely.",#yes
    "Yes.",#yes
    "Signs point to yes.",#yes
    "Ask again later.",#neutral
    "Better not tell you now.",#neutral
    "Cannot predict now.",#neutral
    "Concentrate and ask again.",#neutral
    "Don't count on it.",#no
    "My reply is no.",#no
    "No.",#no
    "My sources say no.",#no
    "Very doubtful."]#no

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

#command to clear messages
@client.command()
async def clear(ctx, amt=1):
    await ctx.channel.purge(limit = amt+1);
    await ctx.send(f"{amt+1} messages were deleted")
    time.sleep(3)
    await ctx.channel.purge(limit = 1)
#==================================================
#tasks
status = cycle(["Something", "Nothing", "Everything"])

# task loop
@tasks.loop(minutes = 5)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))
#==================================================
#the client id by discord
client.run("<INSERT DISCORD CLIENT ID change_presence>")
