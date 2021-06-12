import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
import sys
import asyncio
import math
import random
import logging
import re
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from data import players
from game import SingleHole
from modifications.swordfighting import SwordfightingDecree

from tourneycommands import parse_tourney_message
from gamecommands import glolfcommand


debug = False
prefix = '!'
MAX_GAMES = 10

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        logging.info("Debug mode on!")
        prefix = 'd' + prefix




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
            await message.channel.send("Please add a glolfer's name! It's !addtempmodification <glolfer>\n<modification>")
        else:
            if len(rest.split("\n")) < 2:
                return await message.channel.send("Please add a glolfer's name, then the modification on a new line.")

            glolfername = rest.split("\n")[0].strip()
            modification = rest.split("\n")[1].strip()

            newplayer = players.get_player_from_name(glolfername)
            newplayer.modifications.append(modification)
            players.known_players[glolfername.title()] = newplayer

            return await message.channel.send(f"Added modification {modification} to player {glolfername}. It'll go away when you restart the bot, so make sure to edit the code!")

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
        await parse_tourney_message(message)

    elif message.content.startswith(prefix + "createclub"):
        await create_club(message)
    elif message.content.startswith(prefix + "deleteclub"):
        await create_club(message)

    elif message.content.startswith(prefix + "admincommands"):
        return await message.channel.send("!discordid, !addtempmodification, !updatecoming <true/false>, !clear_game_list, !forcequit, !countgames, !void")

    elif message.content.startswith(prefix + "discordid"):
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "void"):
        
        await message.channel.send(f"There are {len(SwordfightingDecree.players_in_interdimensional_void)} people in the interdimensional void right now: {SwordfightingDecree.players_in_interdimensional_void}")
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
