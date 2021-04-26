import discord, dotenv
config = dotenv.dotenv_values(".env")

from game import SingleHole
import time

client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")

async def newglolfgame(message):
    game = SingleHole()
    glolfgame = await message.channel.send(game.printboard())
    for i in range(60):
        time.sleep(3)
        game.update()
        await glolfgame.edit(content=game.printboard())

    
    await glolfgame.edit(content=game.printboard() + '\n' + "Game over!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!glolf":
        print("glolf detected")
        await newglolfgame(message)

client.run(config["TOKEN"])
