import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from data import players, playerstlats
from modifications.swordfighting import SwordfightingDecree

from tourneycommands import parse_tourney_message
from gamecommands import glolfcommand
from clubs.clubcommands import save_club, view_club


debug = False
prefix = '!'
MAX_GAMES = 10

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        logging.info("Debug mode on!")
        prefix = 'd' + prefix




async def get_glolfer_stats(message, arguments):
    try:
        if len(arguments) == 0:
            await message.channel.send("Please add a glolfer's name to check their stlats!")
        else:
            newplayer = players.get_player_from_name(arguments)
            newmessage = f'''**{newplayer.name}**
Signature: {newplayer.emoji}
Stance: **{newplayer.stlats.stance}**
Favorite Tea: **{newplayer.stlats.fav_tea}**
**Driving:**
{newplayer.compute_driving_moons()}
**Grip:**
{newplayer.compute_precision_moons()}
**Aerodynamics:**
{newplayer.compute_aerodynamics_moons()}
**Self-Awareness:**
{newplayer.compute_self_awareness_moons()}
{newplayer.vk_stat_of_the_day()}
{newplayer.modifications_string()}'''
            await message.channel.send(newmessage)

    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            logging.exception(e)
            raise e


async def add_temp_modification(message, command_body):
    # Add a modification to the player until the bot restarts. Admin-only
    try:
        if len(command_body) == 0:
            await message.channel.send("Please add a glolfer's name! It's !addtempmodification <glolfer>\n<modification>")
        else:
            if len(command_body.split("\n")) < 2:
                return await message.channel.send("Please add a glolfer's name, then the modification on a new line.")

            glolfername = command_body.split("\n")[0].strip()
            modification = command_body.split("\n")[1].strip()

            newplayer = players.get_player_from_name(glolfername)
            newplayer.modifications.append(modification)
            playerstlats.known_players[glolfername.title()] = newplayer

            return await message.channel.send(f"Added modification {modification} to player {glolfername}. It'll go away when you restart the bot, so make sure to edit the code!")

    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            logging.exception(e)
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

def get_command_body(message, command_name_to_remove):
    return message.content.replace(prefix + command_name_to_remove,"").strip()


@client.event
async def on_message(message):
    if message.author == client.user or message.webhook_id is not None:
        return
    if message.content.startswith(prefix + "glolfer"):
        await get_glolfer_stats(message, get_command_body(message, "glolfer"))


    elif message.content.startswith(prefix + "glolf"):
        logging.info("glolf detected")
        await glolfcommand(message, get_command_body(message, "glolf"), debug=debug)


    elif message.content.startswith(prefix + "tourney"):
        await parse_tourney_message(message, get_command_body(message, "tourney"), debug=debug)

    #elif message.content.startswith(prefix + "createclub"):
    #    await save_club(message, get_command_body(message, "createclub"), client=client)
    #elif message.content.startswith(prefix + "viewclub"):
    #    await view_club(message, get_command_body(message, "viewclub"))

    elif message.content.startswith(prefix + "admincommands"):
        return await message.channel.send("!discordid, !addtempmodification, !updatecoming <true/false>, !clear_game_list, !forcequit, !countgames, !void")

    elif message.content.startswith(prefix + "discordid"):
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "void"):
        
        await message.channel.send(f"There are {len(SwordfightingDecree.players_in_interdimensional_void)} people in the interdimensional void right now: {SwordfightingDecree.players_in_interdimensional_void}")
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "addtempmodification"):
        await add_temp_modification(message, get_command_body(message, "addtempmodification"))

    elif user_is_admin(message) and message.content.startswith(prefix + "countgames"):
        await message.channel.send(f"There are {len(get_users_with_games_active())} users with games active right now.")

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
        msg = f"Cleared users with active games list. It was previously {get_users_with_games_active()}. The games are still running but those players can now start new games."
        await message.channel.send(msg)
        logging.info(msg)
        clear_users_with_games_active()

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]

client.run(token)
