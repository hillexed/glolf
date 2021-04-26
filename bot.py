import discord, dotenv
config = dotenv.dotenv_values(".env")

from game import SingleHole
import time
import sys
import asyncio


debug = False
prefix = '!'

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        print("Debug mode on!")
        prefix = 'd' + prefix

client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")

async def newglolfgame(message):
    game = SingleHole()
    glolfgame = await message.channel.send("Beginning game...")
    await asyncio.sleep(2)
    try:
        await glolfgame.edit(content=game.printboard())
        for i in range(60):
            await asyncio.sleep(3)
            game.update()
            await glolfgame.edit(content=game.printboard())
    except Exception as e:
            await glolfgame.add_reaction('⚠️')
            raise e

    
    await glolfgame.edit(content=game.printboard() + '\n' + "Game over!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == prefix + "glolf":
        print("glolf detected")
        await newglolfgame(message)

if debug:
    client.run(config["DEV_TOKEN"])
else:
    client.run(config["TOKEN"])
    
