import discord, dotenv
config = dotenv.dotenv_values(".env")

from game import SingleHole
import time
import sys
import asyncio

import players


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

    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1:
        glolfer_names = arguments[1:]
        if len(glolfer_names) == 1:
            await message.channel.send("It's too dangerous to glolf alone. Bring an opponent.")
            return 

    game = SingleHole(debug=debug,glolfer_names=glolfer_names)
    glolfgame = await message.channel.send("Beginning game...")
    await asyncio.sleep(2)
    try:
        await glolfgame.edit(content="Glolf! (alpha)\n"+game.printboard())
        for i in range(60):
            await asyncio.sleep(3)
            game.update()
            await glolfgame.edit(content="Glolf! (alpha)\n"+game.printboard())
    except (Exception, KeyboardInterrupt) as e:
            await glolfgame.add_reaction('⚠️')
            raise e

    
    await asyncio.sleep(3)
    await glolfgame.edit(content=game.printboard() + '\n' + f"Game over! {game.compute_winner_name()} wins!")

async def get_glolfer_stats(message):
    try:
        rest = message.content.replace(prefix + "glolfer","").strip()
        if len(rest) == 0:        
            await message.channel.send("Please add a glolfer's name to check their stlats!")
        else:
            newplayer = players.get_player_from_name(rest)
            newmessage = f'''**{newplayer.name}**
Signature: {newplayer.emoji}
Stance: **{newplayer.stlats.stance}**
**Driving:**
{newplayer.driving_rating()}
**Grip:**
{newplayer.precision_rating()}
**Aerodynamics:**
{newplayer.aerodynamics_rating()}
**Self-Awareness:**
{newplayer.self_awareness_rating()}'''
            await message.channel.send(newmessage)
            
        
    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            raise e

@client.event
async def on_message(message):
    if message.author == client.user or message.webhook_id is not None:
        return
    if message.content.startswith(prefix + "glolf"):
        print("glolf detected")
        await newglolfgame(message)

    if message.content.startswith(prefix + "glolfer"):
        await get_glolfer_stats(message)

if debug:
    client.run(config["DEV_TOKEN"])
else:
    client.run(config["TOKEN"])
    
