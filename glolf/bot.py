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
from commandwrappers import get_users_with_games_active, clear_users_with_games_active, set_update_coming, is_update_coming
from clubs.clubcommands import save_club, view_club, delete_club, add_player_to_club, remove_player_from_club
from help import parse_help_command
from signup import bet_command
import inventory

import db # debug for ninth internet open


debug = False
prefix = 'g!'
version = '6'
MAX_GAMES = 10

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        logging.info("Debug mode on!")
        prefix = 'd' + prefix




async def get_glolfer_stats(message, arguments):
    playername = arguments.strip()
    if len(playername) == 0:
        await message.channel.send("Please add a glolfer's name to check their stlats!")
    else:
        newplayer = players.get_player_from_name(playername)
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

async def add_modification(message, command_body):
    # Add a modification to the player until the bot restarts. Admin-only
    if len(command_body) == 0:
        await message.channel.send("Please add a glolfer's name! It's g!addmodification <glolfer>\n<modification>")
    else:
        if len(command_body.split("\n")) < 2:
            return await message.channel.send("Please add a glolfer's name, then the modification on a new line.")

        glolfername = command_body.split("\n")[0].strip()
        modification = command_body.split("\n")[1].strip()

        players.add_permanent_modification_to_player(glolfername, modification)

        return await message.channel.send(f"Added modification {modification} to player {glolfername}. Saved in DB.")

async def remove_modification(message, command_body):
    # Add a modification to the player until the bot restarts. Admin-only
    if len(command_body) == 0:
        await message.channel.send("Please add a glolfer's name! It's g!addmodification <glolfer>\n<modification_number>")
    else:
        glolfername = command_body.split("\n")[0].strip()
        player = players.get_player_from_name(glolfername)

        if len(command_body.split("\n")) < 2:
            return await message.channel.send(f"Please add a glolfer's name, then the modification number (0 for first one, 1 for second one) on a new line. \n here's their modifications: {player.modifications}")

        args = command_body.split("\n")[1].strip()

        if len(args) == 0:
            args = "0"
        modification_number = int(args[0])

        if modification_number > len(player.modifications)-1:
            return await message.channel.send(f"That modification wasn't in {glolfername}'s modifications. Here's the list of them: {', '.join([str(m) for m in player.modifications])}. Choose 0 for the first modification, 1 for the second one")
        mod_to_remove = player.modifications[modification_number]
        players.remove_permanent_modification_to_player(glolfername, mod_to_remove)

        return await message.channel.send(f"Removed modification {mod_to_remove} from player {glolfername}. Saved in DB.")

async def list_mods_debug(message, command_body):
    # Add a modification to the player until the bot restarts. Admin-only
    if len(command_body) == 0:
        await message.channel.send("Please add a glolfer's name! It's g!addmodification <glolfer>\n<modification_number>")
    else:
        glolfername = command_body.split("\n")[0].strip()
        player = players.get_player_from_name(glolfername)

        return await message.channel.send(f"Glolfer {glolfername} has these modifications:\n{player.modifications}")

def user_is_admin(message):
    if "ADMIN_IDS" in config:
        if str(message.author.id) in config["ADMIN_IDS"].strip().split(","):
            return True
    return False




intents = discord.Intents(messages=True, message_content=True)
intents.reactions = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    logging.info("The bot is ready!")

def get_command_body(message, command_name_to_remove):
    return message.content.replace(prefix + command_name_to_remove,"")


@client.event
async def on_message(message):
    if message.author == client.user or message.webhook_id is not None:
        return
    try:
        await handle_commands(message)
    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            logging.exception(e)
            raise e

async def handle_commands(message):
    # temp code to handle the ! -> g! migration
    if not debug:
        if message.content.startswith(prefix.replace("g",'') + "glolfer"):
            return await message.channel.send(f"Glolf uses {prefix} as its prefix now! Try g" + message.content)
        if message.content.startswith(prefix.replace("g",'') + "glolf"):
            return await message.channel.send(f"Glolf uses {prefix} as its prefix now! Try g" + message.content)
        if message.content.startswith(prefix.replace("g",'') + "tourney"):
            return await message.channel.send(f"Glolf uses {prefix} as its prefix now! Try g" + message.content)

    if message.content.startswith(prefix + "glolfer"):
        await get_glolfer_stats(message, get_command_body(message, "glolfer"))

    elif message.content.startswith(prefix + "glolf"):
        logging.info("glolf detected")
        await glolfcommand(message, get_command_body(message, "glolf"), debug=debug)

    elif message.content.startswith(prefix + "inventory"):

        message_body = get_command_body(message, "inventory")

        if user_is_admin(message) and len(message_body) > 0 and "regenerate" in message_body:
            if "<@" in message_body and ">" in message_body:
                atted_userID = message_body.split("<@")[1].split(">")[0]
                db.delete_inventory_data(atted_userID)
                await message.channel.send("Their inventory is now:"+ inventory.represent_inventory_as_string(atted_userID))
                return
            return await message.channel.send("on a new line, @ someone.")
            
        if user_is_admin(message) and len(message_body) > 0 and "debug_gift" in message_body:
            if "<@" in message_body and ">" in message_body:
                atted_userID = message_body.split("<@")[1].split(">")[0]
                inventory.give_random_gift(atted_userID)
            else:
                inventory.give_random_gift(userID)

        await inventory.inventory_command(message, get_command_body(message, "inventory"), client)

    elif user_is_admin(message) and message.content.startswith(prefix + "getninthcontestants"):
        await message.channel.send("Contestants: \n"+ str(db.get_game_data("ninth_internet_open_contestants")))

    elif user_is_admin(message) and message.content.startswith(prefix + "clearninthcontestants"):
        db.set_game_data("ninth_internet_open_contestants", [])
        await message.channel.send("Contestants: \n"+ str(db.get_game_data("ninth_internet_open_contestants")))

    elif message.content.startswith(prefix + "version"):
        await message.channel.send(str(version))

    elif message.content.startswith(prefix + "help"):
        await parse_help_command(message, get_command_body(message, "help"), client)


    elif message.content.startswith(prefix + "tourney"):
        await parse_tourney_message(message, get_command_body(message, "tourney"), debug=debug)

    elif message.content.startswith(prefix + "createclub"):
        return await save_club(message, get_command_body(message, "createclub"), client=client)
    elif message.content.startswith(prefix + "deleteclub"):
        return await delete_club(message, get_command_body(message, "deleteclub"), client=client)
    elif message.content.startswith(prefix + "addtoclub"):
        return await add_player_to_club(message, get_command_body(message, "addtoclub"), client=client)
    elif message.content.startswith(prefix + "removefromclub"):
        return await remove_player_from_club(message, get_command_body(message, "removefromclub"), client=client)
    elif message.content.startswith(prefix + "viewclub"):
        return await view_club(message, get_command_body(message, "viewclub"))


    elif message.content.startswith(prefix + "signup"):
        await bet_command(message, get_command_body(message, "signup"), client)

    elif message.content.startswith(prefix + "admincommands"):
        return await message.channel.send("g!discordid, g!addmodification, g!regenerateplayer, g!removemodification g!listmodifications \ng!updatecoming <true/false>, g!clear_game_list, g!forcequit, g!countgames, g!void, g!voidadd, g!doesglolferexist, g!tourney resume <tourney ID>, g!downloadentiredb, g!getninthcontestants, g!clearninthcontestants, g!inventory regenerate (@ someone on new line), g!inventory debug_gift (@ someone on new line)")



    elif message.content.startswith(prefix + "discordid"):
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "countservers"):
        servers = client.guilds
        await message.channel.send(f"{len(servers)}: {[(s.name, s.member_count) for s in servers]}")

    elif user_is_admin(message) and message.content.startswith(prefix + "regenerateplayer"):
        lines = message.content.split("\n")
        if len(lines) == 1:
            return await message.channel.send(f"Put the player on a new line")
            
        success = players.regenerate_player(lines[1].strip())
        await message.channel.send(f"They {'were successfully deleted.' if success else 'weren\'t saved anyways!'}")

    elif user_is_admin(message) and message.content.startswith(prefix + "doesglolferexist"):
        playername = message.content[len(prefix + "doesglolferexist"):].strip()
        is_in_db = players.is_player_in_db(playername)
        await message.channel.send(f"{playername} is {'not' if not is_in_db else ''} in the DB.")


    elif user_is_admin(message) and message.content.startswith(prefix + "voidadd"):
        playername = message.content[len(prefix + "voidadd"):].strip()
        if len(playername) == 0:
            await message.channel.send("Please specify a player name after the command!")
        mockdecree = SwordfightingDecree(None)
        mockdecree.add_to_interdimensional_void(playername)
        await message.channel.send(f"Added {playername} to interdimensional void")

    elif user_is_admin(message) and message.content.startswith(prefix + "void"):
        
        await message.channel.send(f"There are {len(SwordfightingDecree.players_in_interdimensional_void)} people in the interdimensional void right now: {SwordfightingDecree.players_in_interdimensional_void}")
        logging.info(message.author.id) # you should only be able to access this if you're an admin


    elif user_is_admin(message) and message.content.startswith(prefix + "addmodification"):
        await add_modification(message, get_command_body(message, "addmodification"))

    elif user_is_admin(message) and message.content.startswith(prefix + "removemodification"):
        await remove_modification(message, get_command_body(message, "removemodification"))

    elif user_is_admin(message) and message.content.startswith(prefix + "listmodifications"):
        await list_mods_debug(message, get_command_body(message, "listmodifications"))


    elif user_is_admin(message) and message.content.startswith(prefix + "countgames"):
        await message.channel.send(f"There are {len(get_users_with_games_active())} users with games active right now.")

    elif user_is_admin(message) and message.content.startswith(prefix + "countgames"):
        await message.channel.send(f"There are {len(get_users_with_games_active())} users with games active right now.")

    elif user_is_admin(message) and message.content.startswith(prefix + "updatecoming"):
        if "true" not in message.content and "false" not in message.content:
            return await message.channel.send(f"New games are disabled because an update's coming: {update_coming}. Change this by adding 'true' or 'false' to the command")
        elif "true" in message.content:
            set_update_coming(True)     
            await message.channel.send("New games are now disabled. use !countgames to see how many are running.")
        elif "false" in message.content:
            set_update_coming(False)
            await message.channel.send("New games are enabled again.")
        logging.info(f"Changed update_coming to {is_update_coming()}")


    # "clear_game_list" command. just in case
    elif user_is_admin(message) and message.content.startswith(prefix + "clear_game_list"):
        msg = f"Cleared users with active games list. It was previously {get_users_with_games_active()}. The games are still running but those players can now start new games."
        await message.channel.send(msg)
        logging.info(msg)
        clear_users_with_games_active()

    # ultra debug
    elif user_is_admin(message) and message.content.startswith(prefix + "downloadentiredb"):
        # this might hit the discord message filesize limit but it's an admin command so I don't care
        from db import _get_db_filename
        current_time_string = time.asctime(time.localtime()).lower()
        file = discord.File(_get_db_filename(), filename=f"glolf_{current_time_string.replace(' ','_')}.sqlite")
        await message.channel.send(f"Here's a copy of the DB at {current_time_string}", file=file)

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]

client.run(token)
