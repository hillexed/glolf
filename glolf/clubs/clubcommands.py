import db
import asyncio
import random

from .clubdata import GlolfClubData
from data.degrees import generate_degree_based_on_name

async def save_club(message, command_body, client):

    secret_full_template_ssshhhhh_dont_tell_anyone='''g!createclub <Club Name>
<team emoji> "<motto here>"
Cheer: "We're cool!" (optional)
Friends: A, B, C (optional)
Rivals: A, B, C (optional)
Loft: 75 (optional)
player1
player2
player3

caddy1
caddy2
'''

    template='''g!createclub <Club Name>
<team emoji> "<motto here>"
Cheer: "We're cool!" (optional)
player1
player2
player3
'''
    if len(command_body) == 0:
        return await message.channel.send("umm use the command like this: \n" + template)

    lines = command_body.split("\n")

    club_name = lines[0].strip()
    if len(club_name) == 0:
        return await message.channel.send('umm what do you want to call the club? put it on the first line')


    # check to make sure there's no club with this name already
    existing_clubdata = db.get_club_data(club_name)
    if existing_clubdata is not None:
        return await message.channel.send('umm theres a club with that name already. sorry')



    if command_body.count("\n") < 2:
        return await message.channel.send('on a new line, please give me a team emoji and motto! they should look like this:\n<team emoji> "<motto here>"')

    line2words = lines[1].split(" ")
    emoji = line2words[0]
    motto = " ".join(line2words[1:])

    if len(emoji) == 0:
        return await message.channel.send("on line 2, please give me a team emoji at the start of the line!")
    if len(motto) == 0:
        return await message.channel.send("on line 2, please give me a club motto after the emoji!")
    if (len(emoji) > 5 and ":" not in emoji) or len(emoji) > 40:
        if len(motto) == 0:
            return await message.channel.send(f"umm are you sure {emoji} is the right emoji? looks a bit weird to me")
        else:
            return await message.channel.send(f"um was that a team with emoji {emoji} and motto {motto}? i don't think i understood that correctly...") 

    if command_body.count("\n") <= 2:
        return await message.channel.send("umm your club doesnt have any players. thats kinda lonely. give it some players by saying each players name on a new line")

    cheer = None
    friends = []
    rivals = []
    degrees = None

    player_names = []
    caddy_names = []
    empty_lines = 0
    for remaining_line in lines[2:]:

        # switch to caddies if seeing an empty line
        if remaining_line.strip() == "":
            empty_lines += 1
            continue

        # optional things
        if remaining_line.lower().startswith("cheer:"):
            cheer = remaining_line[len("cheer:"):]
            continue

        if remaining_line.lower().startswith("degrees:"):
            degrees = remaining_line[len("degrees:"):].strip()
            continue

        if remaining_line.lower().startswith("friends:"):
            friends = remaining_line[len("friends:"):].split(",")
            friends = [f.strip() for f in friends]
            continue

        if remaining_line.lower().startswith("rivals:"):
            rivals = remaining_line[len("rivals:"):].split(",")
            rivals = [r.strip() for r in rivals]
            continue

        # save the player name
        if empty_lines == 0:
            player_names.append(remaining_line)
        
        elif empty_lines == 1:
            caddy_names.append(remaining_line)
        else:
            return await message.channel.send("There's too many blank lines!")
            
    # sanity checking
    if len(player_names) > 15:
        return await message.channel.send("oh umm wow thats too many players to keep track of. can you stick to umm 15 or less")

    if len(caddy_names) > 12:
        return await message.channel.send("oh umm wow thats too many caddies to keep track of. can you stick to umm 12 or less")
        
    if len(motto) > 80:
        return await message.channel.send("umm thats a really long motto can you choose something shorter and easier to remember")

    if degrees is not None:
        if not degrees.isnumeric():
            return await message.channel.send("umm that club's degrees needs to be a number. sorry")
        elif degrees is not None and (int(degrees) < 1 or int(degrees) >= 180):
            return await message.channel.send("umm that amount of degrees doesnt make sense for a club. sorry. keep it between 1 and 180 ")

    if ':' in club_name:
        return await message.channel.send("sorry but club names cant have ':' in them. its verboten")

    for player in player_names:
        if player_names.count(player) > 1:
            return await message.channel.send(f"sorry but i think theres a duplicate of {player}")

    for caddy in caddy_names:
        if caddy_names.count(caddy) > 1:
            return await message.channel.send(f"sorry but i think theres a duplicate of {caddy}")

    if degrees is None:
        rng = random.Random(club_name) # seeded by club_name so it's deterministic
        loft_degrees = rng.randrange(5,180)
    else:
        loft_degrees = int(degrees)
    displayed_loft_education = [generate_degree_based_on_name(club_name)]

    new_club_data = GlolfClubData(name=club_name, emoji=emoji, motto=motto, player_names=player_names, cheer=cheer, loft_degrees=loft_degrees, displayed_loft_education =displayed_loft_education,   caddy_names=caddy_names,
        friends = friends, rivals = rivals, sponsors = [], modifications = [], owner_ids = [message.author.id])

    await message.channel.send(new_club_data.printTeamInfo())

    reactmessage = await message.channel.send("umm does that look good")
    await reactmessage.add_reaction('👍')
    await reactmessage.add_reaction('👎')


    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ('👍', '👎')

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
        if str(reaction.emoji) == '👍':
            db.set_club_data(club_name, new_club_data)
            await message.channel.send(f'ok nice looks like a new club has been formed')
        else:
            await message.channel.send(f'oh ok well guess ill go do something else')
    except asyncio.TimeoutError:
        await message.channel.send('umm i didnt hear anything so ill take that as a no. let me know if you want to try saving again')

async def view_club(message, command_body):
    club_name = command_body.strip()
    clubdata = db.get_club_data(club_name)
    print(clubdata)
    if clubdata is None:
        return await message.channel.send("umm couldnt find a club with that name sorry")

    club = GlolfClubData(*clubdata)
    await message.channel.send(club.printTeamInfo())


# todo
def deleteclub(message):
    pass

def add_player_to_club(message):
    pass

def declare_rival(message):
    pass

def declare_friend(message):
    pass
