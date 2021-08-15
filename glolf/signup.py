import discord
import logging
logger = logging.getLogger(__name__)
import emoji
import asyncio

import db
from clubs.clubdata import GlolfClubData

bets = {}
def get_bets():
    bets = db.get_game_data("bets")
    if bets is None:
        bets = {}
    return bets

def get_bets_by_team():
    bets = db.get_game_data("bets_by_team")
    if bets is None:
        bets = {}
    return bets

def record_bet(userid, fav_team_name):
    bets = get_bets()
    bets_by_team = get_bets_by_team()

    bets[userid] = fav_team_name

    if fav_team_name not in bets_by_team:
        bets_by_team[fav_team_name] = []
    bets_by_team[fav_team_name].append(userid)
    
    db.set_game_data("bets", bets)
    db.set_game_data("bets_by_team", bets_by_team)

async def bet_command(message, message_body, client):
    userid = str(message.author.id)

    bets = get_bets()
    if userid in bets:
        await message.channel.send(f":horse: Ya got a favorite team already, pardner: the {bets[userid]}")

    clubs = []

    club_name_list = message_body.strip().split("\n")
    club_name_list = [
    'Spakistan Sputters',
    'Steamy Irons',
    'Wedge Products',
    ''
    ]
    
    for clubname in club_name_list:
        clubdata = db.get_club_data(clubname)
        if clubdata is None:
            await message.channel.send(f"umm couldnt find a club named {clubname}")
            return
        club = GlolfClubData(*clubdata)
        clubs.append(club)
    print(clubs)

    

    printmessage = ":horse: react ta place yer bets\n\n"

    emojis_to_clubs = {}
    backup_emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣']
    for club in clubs:
        newemoji = club.emoji
        distinct_and_valid = True
        if emoji.emoji_count(newemoji) != 1: # invalid emoji, can't react'
            distinct_and_valid = False
        if newemoji in emojis_to_clubs:
            distinct_and_valid = False
        # use a backup to ensure emojis are unique
        if not distinct_and_valid:
            for backupemoji in backup_emojis:
                if backupemoji not in emojis_to_clubs:
                    newemoji = backupemoji
                    distinct_and_valid = True
                    break
        if not distinct_and_valid:
            raise ValueError("No valid emojis!")

        emojis_to_clubs[newemoji] = club
        printmessage += f"{newemoji} {club.name}\n"

    sent_message = await message.channel.send(printmessage)

    for club_emoji in emojis_to_clubs:
        try:    
            await sent_message.add_reaction(club_emoji)
        # except NoSuchEmojiError:
        except discord.errors.HTTPException as e:
            logger.error(f"Club {emojis_to_clubs[club_emoji].name} has a broken emoji {club_emoji} which can't be used as a reaction!")
            raise e

    # if you react
    # save that you reacted
    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in emojis_to_clubs

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
         # remove all reactions?
        try:    
            await sent_message.clear_reactions()
        except discord.errors.Forbidden:
            pass

        chosen_club = emojis_to_clubs[reaction.emoji]

        record_bet(user.id, chosen_club.name) # save bet

        
        bets_on_your_team = get_bets_by_team()[chosen_club.name]

        await message.channel.send(f":horse: Yer now fan #{len(bets_on_your_team)} of the {chosen_club.name}! Cheer hard for em!")
            
            
    except asyncio.TimeoutError:
        try:    
            await sent_message.clear_reactions()
        except discord.errors.Forbidden:
            pass
