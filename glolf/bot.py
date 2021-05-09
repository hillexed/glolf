import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
import sys
import asyncio
import math
import random
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import players
from game import SingleHole


debug = False
prefix = '!'

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        logging.info("Debug mode on!")
        prefix = 'd' + prefix

users_with_games_active = []

def limit_one_game_per_person(func):
    '''
    A decorator to ensure someone can only run one command at a time.
    Also, has some bonus error reporting if something goes wrong.
    The first argument of a function using this decorator must be 'message', a discord message to react to if something goes wrong
    '''
    async def wrapper(message, *args, **kwargs):
        global users_with_games_active

        if message.author in users_with_games_active:
            await message.channel.send("To avoid lag, please wait for your current game to finish before starting any more.")
            return
        users_with_games_active.append(message.author)
        try:
            return await func(message, *args, **kwargs)
        except (Exception, KeyboardInterrupt) as e:
                logging.error(e)
                await message.add_reaction('⚠️')
                raise e
        finally:
            if message.author in users_with_games_active:
                users_with_games_active.remove(message.author)

    return wrapper

update_coming = False

def disable_if_update_coming(func):
    '''
    A decorator to disable starting new games if updates are coming
    '''
    async def wrapper(message, *args, **kwargs):
        global update_coming
        if update_coming:
            await message.channel.send(":loop: HANG TIGHT FOR A MOMENT, GOT SOME RADICAL RENOVATIONS COMIN' RIGHT UP\n:loop: PLEASE LEAVE A MESSAGE AFTER THE TONE")
            return
        return await func(message, *args, **kwargs)
    return wrapper


async def newglolfgame(message, glolfer_names, header=None, max_turns=60):
    # start a round of glolf and return the winning player's name

    glolfgame = await message.channel.send("Beginning game...")
    logging.info(f"Starting game between {glolfer_names} in channel #{message.channel} in server '{message.channel.guild.name}'")
    try:
        game = SingleHole(debug=debug,glolfer_names=glolfer_names,max_turns=max_turns)
        await asyncio.sleep(2)
        await glolfgame.edit(content=game.printgamestate(header=header))
        await asyncio.sleep(2)

        while not game.over:
            delay = game.update()
            await glolfgame.edit(content=game.printgamestate(header=header))
            await asyncio.sleep(delay)

        await glolfgame.edit(content=game.printgamestate(include_board=True,header=header))
        await asyncio.sleep(10)
        await glolfgame.edit(content=game.printgamestate(include_board=False,header=header))
        return game.compute_winner()
    except (Exception, KeyboardInterrupt) as e:
            await glolfgame.add_reaction('⚠️')
            raise e

@disable_if_update_coming
@limit_one_game_per_person
async def glolfcommand(message):
    # parse a glolf command

    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        if len(glolfer_names) == 1:
            await message.channel.send("It's too dangerous to glolf alone. Bring an opponent.")
            return

    await newglolfgame(message, glolfer_names)

def biggest_power_of_two_less_than(n):
    return 2 ** math.floor(math.log2(n))

@disable_if_update_coming
@limit_one_game_per_person
async def one_v_one_glolftourney(message):
    arguments = message.content.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1:
        glolfer_names = arguments[1:]
        num_players = len(glolfer_names)
        if num_players == 1:
            await message.channel.send("That's a short tournament... I guess they win by default!")
            return None
    else: # 0 players
        await message.channel.send("To use, please specify a list of competitors, on one line each")
        return


    await message.channel.send(f"{len(glolfer_names)}-person tournament starting...")
    move_onto_next_round = []

    random.shuffle(glolfer_names)

    competitors_this_round = glolfer_names[:]

    # If # of entrants isn't a power of two, give some contestants byes
    if not len(glolfer_names) == biggest_power_of_two_less_than(len(glolfer_names)):
        #await message.channel.send(f"I need a power-of-two number of people. You have {len(glolfer_names)}")
        num_matches_required = len(glolfer_names) - biggest_power_of_two_less_than(len(glolfer_names))

        competitors_this_round = glolfer_names[0:num_matches_required*2]
        move_onto_next_round = glolfer_names[num_matches_required*2:]

        print(len(competitors_this_round)/2 + len(move_onto_next_round))
        await message.channel.send(f"{', '.join(move_onto_next_round)} randomly recieve byes and move onto the next round. Let's see who joins them!")

    # actual tourney time!
    round_num = 0
    while len(competitors_this_round) > 1:
        round_num+= 1

        max_turns = 60
        if len(competitors_this_round) >= 16:
            max_turns = 40
        if debug:
            max_turns = 3

        round_name = f"round {round_num}"
        if len(competitors_this_round) + len(move_onto_next_round) == 2:
            round_name = "the finals"
        if len(competitors_this_round) + len(move_onto_next_round) == 4 and round_num != 1:
            round_name = "the almostfinals"
        if len(competitors_this_round) + len(move_onto_next_round) == 8 and round_num != 1:
            round_name = "the nearfinals"
        if len(move_onto_next_round) > 0:
            # this is right after move_onto_next_round should be []
            #if it isn't [], we're in the first round of a tourney with a non-power-of-two number of entrants
            round_name = "qualifiers"

        for index in range(0,len(competitors_this_round)-1,2):
            # go down the bracket
            # competitors
            glolfers = [competitors_this_round[index],competitors_this_round[index+1]]
            await asyncio.sleep(2)

            match_number = int(index/2)+1
            total_matches = int(len(competitors_this_round)/2)

            match_name = f"Match {match_number}/{total_matches}"
            if match_number == total_matches and round_name != "the finals" and total_matches == 1:
                match_name = "Final match"

            winner = await newglolfgame(message, glolfer_names=glolfers, header=f"{match_name} of {round_name}!",max_turns=max_turns)
            if winner is not None:
                move_onto_next_round.append(winner.name)
            else:
                winningname = random.choice(glolfers)
                move_onto_next_round.append(winningname)
                await message.channel.send(f"Tie game! {winningname} wins the tiebreaking duel to advance to the next round!")
                await asyncio.sleep(5)

        if len(move_onto_next_round) > 1:

            round_descriptor = f"Round {round_num} results:"
            if len(move_onto_next_round) == 2 and round_num != 1:
                round_descriptor = "Almostfinals results:"
            if len(move_onto_next_round) == 4 and round_num != 1:
                round_descriptor = "Nearfinals results:"

            await message.channel.send(f"**{round_descriptor}** {len(move_onto_next_round)} contestants move on: **{', '.join(move_onto_next_round)}**. Next round starts in one minute...")
            await asyncio.sleep(60)

        competitors_this_round = move_onto_next_round
        move_onto_next_round = []

    await message.channel.send(f"**{competitors_this_round[0]} wins the tournament!**")

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
Favorite Tea: **{newplayer.stlats.fav_tea}**
**Driving:**
{newplayer.driving_rating()}
**Grip:**
{newplayer.precision_rating()}
**Aerodynamics:**
{newplayer.aerodynamics_rating()}
**Self-Awareness:**
{newplayer.self_awareness_rating()}
{newplayer.vk_stat_of_the_day()}
{newplayer.modifications_string()}'''
            await message.channel.send(newmessage)

    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            raise e


async def add_temp_modification(message):
    # Add a modification to the player until the bot restarts. Admin-only
    try:
        print(message.content)
        rest = message.content.replace(prefix + "addtempmodification","").strip()
        if len(rest) == 0:
            await message.channel.send("Please add a glolfer's name!")
        else:
            if len(rest.split("\n")) < 2:
                return await message.channel.send("Please add a glolfer's name, then the modification on a new line.")

            glolfername = rest.split("\n")[0].strip()
            modification = rest.split("\n")[1].strip()

            newplayer = players.get_player_from_name(glolfername)
            newplayer.modifications.append(modification)
            players.known_players[glolfername] = newplayer

            return await message.channel.send(f"Added modification {} to player {}. It'll go away when you restart the bot, so make sure to edit the code!")

    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            raise e

def user_is_admin(message):
    if "ADMIN_IDS" in config:
        if str(message.author.id) in config["ADMIN_IDS"].strip().split(","):
            return True
    return False








client = discord.Client()
@client.event
async def on_ready():
    logging.info("The bot is ready!")


@client.event
async def on_message(message):
    global users_with_games_active
    if message.author == client.user or message.webhook_id is not None:
        return

    if message.content.startswith(prefix + "glolfer"):
        await get_glolfer_stats(message)


    elif message.content.startswith(prefix + "glolf"):
        logging.info("glolf detected")
        await glolfcommand(message)

    elif message.content.startswith(prefix + "tourney"):

        if message.content.startswith(prefix + "tourney 1v1"):
            await one_v_one_glolftourney(message)
        else:
            await message.channel.send("The llawn only allows 1v1 tourneys right now. try "+prefix+"tourney 1v1")



    elif message.content.startswith(prefix + "admincommands"):
        return await message.channel.send("!discordid, !addtempmodification, !updatecoming <true/false>, !clear_game_list, !forcequit")

    elif message.content.startswith(prefix + "discordid"):
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "addtempmodification"):
        await add_temp_modification(message)

    elif user_is_admin(message) and message.content.startswith(prefix + "countgames"):
        await message.channel.send(f"There are {len(users_with_games_active)} users with games active right now.")

    elif user_is_admin(message) and message.content.startswith(prefix + "updatecoming"):
        global update_coming
        if "true" not in message.content and "false" not in message.content:
            return await message.channel.send(f"New games are disabled because an update's coming: {update_coming}. Change this by adding 'true' or 'false' to the command")
        elif "true" in message.content:

            update_coming = True        
            await message.channel.send("New games are now disabled. use !countgames to see how many are running.")
        elif "false" in message.content:
            update_coming = False
            await message.channel.send("New games are enabled again.")
        logging.info(f"Changed update_coming to {update_coming}")


    # "clear_game_list" command. just in case
    elif user_is_admin(message) and message.content.startswith(prefix + "clear_game_list"):
        msg = f"Cleared users with active games list. It was previously {users_with_games_active}. The games are still running but those players can now start new games."
        await message.channel.send(msg)
        logging.info(msg)
        users_with_games_active = []

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]

client.run(token)
