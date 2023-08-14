from modifications.modification_halves import choose_random_trigger_ID, choose_random_effect_ID, available_effects, available_triggers
from modifications.merged_modifications import merge_descriptions, merge_emojis
from data.saved_mod_data import MergedModificationDataTemplate, nutrisocks
from data.players import default_player_names

from math import ceil, floor
import db
import random
import json
import logging

import data.players
import asyncio

#g!inventory, g!inventory merge

class ITEM_TYPE:
    mod_half_trigger = "mod_half_trigger"
    mod_half_effect = "mod_half_effect"

def compute_inventory(userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        inventory = json.loads(inventory)
    else: # not in DB
        inventory = []
        inventory.append(generate_random_gift()) # give someone new a welcome gift!
        db.set_inventory_data(userid, json.dumps(inventory))
    return inventory

def remove_from_inventory(userid, thing_to_remove):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        inventory = json.loads(inventory)
    else: # not in DB
        raise ValueError("Userid not in inventory DB!")

    if thing_to_remove in inventory:
        inventory.remove(thing_to_remove)
        db.set_inventory_data(userid, json.dumps(inventory))
    else:
        raise ValueError("Thing not in user's inventory in DB!")
        


def give_random_gift(userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        inventory = json.loads(inventory)
    else: # not in DB
        inventory = []
    inventory.append(generate_random_gift()) # give someone new a welcome gift!
    db.set_inventory_data(userid, json.dumps(inventory))


def represent_inventory_as_string(username):
    inventory = compute_inventory(username)

    prefix = "**Your mailball:**\n"

    if len(inventory) == 0:
        return prefix + "Empty!"

    return prefix + '\n'.join([format_item(item_data) for item_data in inventory]) + '\n(use `g!inventory merge` to Merge your stocks with others\' help!)'

def format_item(item_data):
    return f'- {item_emoji(item_data)}\n    {item_data["description"]}'

def item_emoji(item_data):

    if item_data["type"] == ITEM_TYPE.mod_half_trigger:
        return "🦴"
    if item_data["type"] == ITEM_TYPE.mod_half_effect:
        return "🥩"
    return "🎁"


def generate_random_gift():
    if random.random() < 0.5:
        return generate_random_trigger()
    else:
        return generate_random_effect()

def generate_random_trigger():
    chosen_ID = choose_random_trigger_ID()
    trigger_emoji = available_triggers[chosen_ID].emoji
    description = f"A glass jar of bone stock, stamped with a {trigger_emoji} symbol. Useless on its own, but maybe if combined..."
    return {"type":ITEM_TYPE.mod_half_trigger, "contains": chosen_ID, "description":description}

def generate_random_effect():
    chosen_ID = choose_random_effect_ID()
    trigger_emoji = available_effects[chosen_ID].emoji
    description = f"A sealed can of meat stock, stamped with a {trigger_emoji} symbol. Useless on its own, but maybe if combined..."
    return {"type":ITEM_TYPE.mod_half_effect, "contains": chosen_ID, "description":description}


def merge(trigger_item, effect_item):

    trigger_ID = trigger_item["contains"]
    effect_ID = effect_item["contains"]

    trigger = available_triggers[trigger_ID]
    effect = available_effects[effect_ID]
    
    merged_mod_data = MergedModificationDataTemplate(name="Joint Stock Venture", description=merge_descriptions(trigger, effect), emoji=merge_emojis(trigger, effect), trigger_ID=trigger_ID, effect_ID = effect_ID)
    return merged_mod_data



async def inventory_command(message, message_body, client):
    userid = message.author.id

    username = message.author.display_name.lower() # I'd love to use global_name but it doesn't work.

    if len(message_body) > 0 and "merge" in message_body:
        return await merge_offer(message, client)

    if len(message_body) > 0 and "regenerate" in message_body:
        return db.delete_inventory_data(userid)

    #if len(message_body) > 0 and "debug_getgift" in message_body:
    #    give_random_gift(userid)

    return await message.channel.send(represent_inventory_as_string(userid))


def get_first_item_of_type(userid, type):
    inv = compute_inventory(userid)
    for item in inv:
        if item["type"] == type:
            return item
    return None

async def merge_offer(message, client):
    user1 = message.author
    user1id = user1.id
    
    trigger_item = get_first_item_of_type(user1id, ITEM_TYPE.mod_half_trigger)
    effect_item = get_first_item_of_type(user1id, ITEM_TYPE.mod_half_effect)

    has_trigger = (trigger_item is not None)
    has_effect = (effect_item is not None)

    if not has_trigger and not has_effect:
        return await message.channel.send(":horse: Yer plum outta stock, pardner.")
    
    if has_trigger and not has_effect:
        requesting_thing = "a meat stock"
    if not has_trigger and has_effect:
        requesting_thing = "a bone stock"
    else:
        requesting_thing = "a stock"

    offer_msg = f":horse: {user1.display_name} is making a Merger offer! React with 👀 if ya have {requesting_thing} ta explore Merger opportunities!"
    sentmessage = await message.channel.send(offer_msg)
    await sentmessage.add_reaction("👀")

    def is_potential_deal_partner(reaction, user2):
        if user2.id == user1.id:
            return False
        user2id = user2.id
        
        if has_effect and get_first_item_of_type(user2id, ITEM_TYPE.mod_half_trigger) is not None:
            return True
        if has_trigger and get_first_item_of_type(user2id, ITEM_TYPE.mod_half_effect) is not None:
            return True
        return False

    try:
        reaction, user2 = await client.wait_for('reaction_add', timeout=300.0, check=is_potential_deal_partner)
        if str(reaction.emoji) == "👀":
            try:    
                await sentmessage.clear_reactions()
            except discord.errors.Forbidden:
                pass

            user2_trigger = get_first_item_of_type(user2.id, ITEM_TYPE.mod_half_trigger)
            if has_trigger and user2_trigger is not None:
                await close_deal(sentmessage, client, trigger_user=user1, effect_user=user2)
            else:
                assert has_effect
                await close_deal(sentmessage, client, trigger_user=user2, effect_user=user1)
    except asyncio.TimeoutError:
        try:    
            await sentmessage.clear_reactions()
            await sentmessage.edit(content=":horse: Too long with no Merger, I'm closin' this tab. Better luck next time")
        except discord.errors.Forbidden:
            pass
    return

async def close_deal(sentmessage, client, trigger_user, effect_user):

    trigger_item = None
    effect_item = None

    trigger_item = get_first_item_of_type(trigger_user.id, ITEM_TYPE.mod_half_trigger)
    effect_item = get_first_item_of_type(effect_user.id, ITEM_TYPE.mod_half_effect)

    if trigger_item is None and effect_item is None:
        # should never get here
        sentmessage.edit(content=f":horse: Ya don't have the right items! Deal's over.")
        raise ValueError("The users don't have the right items")

    trigger_ID = trigger_item["contains"]
    effect_ID = effect_item["contains"]

    trigger = available_triggers[trigger_ID]
    effect = available_effects[effect_ID]
    

    await sentmessage.edit(content=f"How bout it? Ya want to merge {trigger_user.display_name}'s {trigger.emoji} bone stock and {effect_user.display_name}'s {effect.emoji} meat stock? If so, y'all both gotta react with :thumbsup:.")
    await sentmessage.add_reaction("👍")
    await sentmessage.add_reaction("👎")

    users_yet_to_thumbs_up = [trigger_user.id, effect_user.id]
    print(users_yet_to_thumbs_up)
    try:
        for i in range(2):
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, 
                check=lambda reaction, user: user.id in users_yet_to_thumbs_up and str(reaction.emoji) in ("👍", "👎"))

            if str(reaction.emoji) == "👍":
                users_yet_to_thumbs_up.remove(user.id)
            else:
                raise asyncio.TimeoutError("no deal")
            
    except asyncio.TimeoutError:
        return await sentmessage.edit(content=":horse: No deal? Better luck next time")


    # who should get the new mod?
    # todo: get to choose who gets it.
    # but for now... mergers

    glolfername="mod"

    glolfer1, glolfer2 = choose_glolfer_names(trigger_user, effect_user)
    glolfername = merge_names(glolfer1, glolfer2)
    

    mod = merge(trigger_item, effect_item)
    data.players.add_permanent_modification_to_player(glolfername, mod)

    logging.info(mod, trigger_item, trigger_user.id, effect_item, effect_user.id, compute_inventory(trigger_user.id), compute_inventory(effect_user.id))

    remove_from_inventory(trigger_user.id, trigger_item)
    remove_from_inventory(effect_user.id, effect_item)

    await sentmessage.edit(content=f""":horse: Congrats on the Merger, pardners!
:moneybag: Your Merger Comes With An Acquisition!
:moneybag: Using Your Wonderful Submissions
:moneybag: We Have Taken Notice Of {glolfer1} and {glolfer2}...
:moneybag: And Merged Player {glolfername} has Acquired Something New!
:moneybag: Now {glolfername} Has Been Entered in the Ninth Internet Open!
:moneybag: {random.choice(('What A Twist!', 'How Exciting!', 'Truly Unique Talent', 'A Shocking Development', 'What A Twist', 'Better Tune In'))}""")

    contestants = db.get_game_data("ninth_internet_open_contestants")
    if contestants is None:
        contestants = ""
    contestants += glolfername + ", "
    db.set_game_data("ninth_internet_open_contestants", contestants)

    return 


ninth_internet_open_entrants = {"nic":	"sebqey qiz",
"syl":"Rutabaga Adams",
"Bogle":"Hedgey the Hedgehog",
"The Menagerie (She/They) Rep": "The Worst Person You Know",
"cheshirecat": "Asphalt Polygamy",
"Ditto":"Rebecca Monarch",			
"🌌Blackout Galaxy🌌 [they/void]":	"Nab Nab",
"Palsonny☀🛠": "Iterant Gambler",
"A Normal Box":"Dandori Daniel",
"Shorkball 🔏(he/they)":"Ace Ukiyo",
"IntoAMuteCrypt (he/him)": "Robert'); DROP TABLE Students;--",
"Neutronicxz (he/him)":	"A pack of AA batteries",
"fraZ0R (Any Pronouns) | ∅": "Topo Palo"
}

other_entrants = ("Ryusei Sakuta","Wormichael Zarlinski") + default_player_names

def choose_glolfer_names(user1, user2):
    # eventually this should be

    user1name = random.choice(other_entrants)
    user2name = random.choice(other_entrants)

    if user1.display_name in ninth_internet_open_entrants:
        user1name = ninth_internet_open_entrants[user1.display_name]

    if user2.display_name in ninth_internet_open_entrants:
        user2name = ninth_internet_open_entrants[user2.display_name]
    return user1name, user2name

def merge_names(name1, name2):
    # combine first name of one with second name of another, taking into account more than one space in the name
    splitnames1 = name1.split(" ")
    splitnames2 = name2.split(" ")

    return " ".join(splitnames1[:ceil(len(splitnames1)/2)] + splitnames2[ceil(len(splitnames2)/2):])
    
        
    


async def merge_apply_test(message):
    glolfername = "test"
    mod = merge(generate_random_trigger(), generate_random_effect())
    data.players.add_permanent_modification_to_player(glolfername, mod)

    return await message.channel.send(f"Added modification {mod} to player {glolfername}. Saved in DB.")
