import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
import sys
import asyncio
import math

import players
from game import SingleHole


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

async def newglolfgame(channel, glolfer_names, header="", turns=60):
    # start a round of glolf and return the winning player's name

    fullheader = f"Glolf! (alpha) {header}\n"

    game = SingleHole(debug=debug,glolfer_names=glolfer_names)
    glolfgame = await channel.send("Beginning game...")
    await asyncio.sleep(2)
    try:
        await glolfgame.edit(content=fullheader+game.printboard())
        for i in range(turns):
            await asyncio.sleep(3)
            game.update()
            await glolfgame.edit(content=fullheader+game.printboard())
    except (Exception, KeyboardInterrupt) as e:
            await glolfgame.add_reaction('⚠️')
            raise e

    await asyncio.sleep(3)
    await glolfgame.edit(content=fullheader+game.printboard() + '\n' + f"Game over! {game.compute_winner_name()} wins!")
    return game.compute_winner()

async def glolfcommand(message):
    # parse a glolf command
    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        if len(glolfer_names) == 1:
            await message.channel.send("It's too dangerous to glolf alone. Bring an opponent.")
            return 

    await newglolfgame(message.channel, glolfer_names)

def biggest_power_of_two_less_than(n):
    return 2 ** math.floor(math.log2(n))

async def one_v_one_glolftourney(message):

    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        num_players = len(glolfer_names)
        if num_players == 1:
            await message.channel.send("That's a short tournament... I guess they win by default!")
            return None
    else:
        await message.channel.send("To use, please specify a list of competitors, on one line each")
        return

    '''
    num_people_to_eliminate_first_round = num_players - biggest_power_of_two_less_than(n)

    for i in range(num_people_to_eliminate_first_round):
        await asyncio.sleep(2)
        await newglolfgame(message.channel, glolfer_names)
        '''

    # is a power of two
    if not len(glolfer_names) == biggest_power_of_two_less_than(len(glolfer_names)):
        await message.channel.send(f"I need a power-of-two number of people. You have {len(glolfer_names)}")
        return

    
    await message.channel.send(f"{len(glolfer_names)}-person tournament starting...")

    round_num = 0
    while len(glolfer_names) > 1:
        round_num+= 1
        move_onto_next_round = []
        for index in range(0,len(glolfer_names)-1,2):
            # go down the bracket
            # competitors 
            glolfers = [glolfer_names[index],glolfer_names[index+1]]
            await asyncio.sleep(2)

            turns = 60  
            if debug:
                turns = 3

            winner = await newglolfgame(message.channel, glolfer_names=glolfers, header=f"- Match {int(index/2)+1} of round {round_num}!",turns=turns)
            if winner is not None:
                move_onto_next_round.append(winner.name)
            else:
                winningname = random.choice(glolfers)
                move_onto_next_round.append(winningname)
                await message.channel.send(f"Tie game! {winningname} wins the tiebreaking swordfight to advance to the next round!")
        glolfer_names = move_onto_next_round

        if len(move_onto_next_round) > 1:
            await message.channel.send(f"{len(move_onto_next_round)} contestants move on: {', '.join(move_onto_next_round)}")
    
    await message.channel.send(f"{glolfer_names[0]} wins the tournament!")

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

    if message.content.startswith(prefix + "tourney"):
        if message.content.startswith(prefix + "tourney 1v1"):
            await one_v_one_glolftourney(message)
        else:
            await message.channel.send("The llawn only allows 1v1 tourneys right now. try "+prefix+"tourney 1v1")

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]

client.run(token)
    
