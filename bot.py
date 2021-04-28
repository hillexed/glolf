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
    await glolfgame.edit(content=fullheader+game.print_board_game_completed())
    return game.compute_winner()

async def glolfcommand(message):
    # parse a glolf command

    global users_with_games_active
    if message.author in users_with_games_active and not debug:
        return await message.channel.send("To avoid lag, please wait for your current game to finish before starting another.")

    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        if len(glolfer_names) == 1:
            await message.channel.send("It's too dangerous to glolf alone. Bring an opponent.")
            return

    users_with_games_active.append(message.author)
    await newglolfgame(message.channel, glolfer_names)
    users_with_games_active.remove(message.author)

def biggest_power_of_two_less_than(n):
    return 2 ** math.floor(math.log2(n))




async def one_v_one_glolftourney_oneround(message):

    global users_with_games_active
    if message.author in users_with_games_active:
        return await message.channel.send("To avoid lag, please wait for your current game to finish before starting a tournament.")

    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        num_players = len(glolfer_names)
        if num_players == 1:
            await message.channel.send("That's a short tournament... I guess they win by default!")
            return None
        if num_players % 2 == 1:
            await message.channel.send("I need an even number of players!")
            return None
            
    else:
        await message.channel.send("To use, please specify a list of competitors, on one line each")
        return
    
    await message.channel.send(f"One round of {len(glolfer_names)} people starting...")
    users_with_games_active.append(message.author)

    round_num = 1
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
            await asyncio.sleep(30)
    glolfer_names = move_onto_next_round

    if len(move_onto_next_round) > 1:
        await message.channel.send(f"{len(move_onto_next_round)} contestants move on: {', '.join(move_onto_next_round)}.")
        await asyncio.sleep(60)
    
    users_with_games_active.remove(message.author)



async def one_v_one_glolftourney(message):

    global users_with_games_active
    if message.author in users_with_games_active:
        return await message.channel.send("To avoid lag, please wait for your current game to finish before starting a tournament.")

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

    # ensure # of entrants is a power of two
    if not len(glolfer_names) == biggest_power_of_two_less_than(len(glolfer_names)):
        await message.channel.send(f"I need a power-of-two number of people. You have {len(glolfer_names)}")
        return

    
    await message.channel.send(f"{len(glolfer_names)}-person tournament starting...")
    users_with_games_active.append(message.author)

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
                await asyncio.sleep(30)
        glolfer_names = move_onto_next_round

        if len(move_onto_next_round) > 1:
            await message.channel.send(f"{len(move_onto_next_round)} contestants move on: {', '.join(move_onto_next_round)}. Next round starts in one minute...")
            await asyncio.sleep(60)
    
    users_with_games_active.remove(message.author)
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
{newplayer.self_awareness_rating()}
{newplayer.modifications_string()}'''
            await message.channel.send(newmessage)
            
        
    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            raise e

def user_is_admin(message):
    if "ADMIN_IDS" in config:
        if str(message.author.id) in config["ADMIN_IDS"].strip().split(","):
            return True
    return False


users_with_games_active = []






client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")


@client.event
async def on_message(message):
    if message.author == client.user or message.webhook_id is not None:
        return

    if message.content.startswith(prefix + "glolfer"):
        await get_glolfer_stats(message)


    elif message.content.startswith(prefix + "glolf"):
        print("glolf detected")
        await glolfcommand(message)

    elif message.content.startswith(prefix + "tourney"):

        if message.content.startswith(prefix + "tourney 1v1"):
            await one_v_one_glolftourney(message)
        elif message.content.startswith(prefix + "tourney oneround"):
            await one_v_one_glolftourney_oneround(message)
        else:
            await message.channel.send("The llawn only allows 1v1 tourneys right now. try "+prefix+"tourney 1v1")

    elif message.content.startswith(prefix + "discordid"):
        print(message.author.id) # you should only be able to access this if you're an admin

    # 'forceupdate' auto-updater
    elif user_is_admin(message) and message.content.startswith(prefix + "forceupdate"):
        if "yes" not in message.content:
            return await message.channel.send("Are you sure? If so add 'yes' to the end of your message") 
        import subprocess
        output = subprocess.check_output(["git", "stash"])
        await message.channel.send(output)
        await asyncio.sleep(3)
        output = subprocess.check_output(["git", "pull","--force"])
        await message.channel.send(output)
        await message.channel.send(">_< Looks good! Restart me whenever you're ready!")
        print("Update complete! Now I need to be restarted!")

    # forcequit command
    elif user_is_admin(message) and message.content.startswith(prefix + "forcequit"):
        if "yes" not in message.content:
            return await message.channel.send("Are you sure? If so add 'yes' to the end of your message")
        exit()

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]

client.run(token)
    
