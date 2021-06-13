import db
import asyncio

from .clubs import GlolfClubData

async def save_club(message, command_body, client):
    template='''!saveclub <Club Name>
<team emoji> "<motto here>"
Cheer: "We're cool!" (optional)
player1
player2
player3

caddy1
caddy2
'''
    if len(command_body) == 0:
        return message.channel.send("Usage: \n" + template)

    lines = command_body.split("\n")

    club_name = lines[0].strip()
    if command_body.count("\n") < 2:
        return message.channel.send('On a new line, please fill out emoji and motto! They should look like this:\n<team emoji> "<motto here>"')

    line2words = lines[1].split(" ")
    emoji = line2words[0]
    motto = " ".join(line2words[1:])

    if len(emoji) == 0:
        return message.channel.send("On line 2, please provide an emoji at the start of the line!")
    if len(motto) == 0:
        return message.channel.send("On line 2, please provide a club motto after the emoji!")
    if (len(emoji) > 5 and ":" not in emoji) or len(emoji) > 40:
        if len(motto) == 0:
            return await message.channel.send(f"{emoji} as an emoji? That doesn't look right...")
        else:
            return await message.channel.send(f"Er, was that a team with emoji {emoji} and motto {motto}? I don't think I understood that correctly...") 

    if command_body.count("\n") <= 2:
        return await message.channel.send("This club has no players in it! Name each player in the club on its own new line.")

    cheer = None
    friends = []
    rivals = []

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
            

    if len(player_names) > 12:
        return await message.channel.send("oh umm wow thats too many players to keep track of. can you stick to umm 12 or less")

    if len(caddy_names) > 12:
        return await message.channel.send("oh umm wow thats too many caddies to keep track of. can you stick to umm 12 or less")
        
    if len(motto) > 80:
        return await message.channel.send("umm thats a really long motto can you choose something shorter and easier to remember")
    

    new_club_data = GlolfClubData(name=club_name, emoji=emoji, motto=motto, player_names=player_names, cheer=cheer, caddy_names=caddy_names,
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



def deleteclub(message):
    pass
    

def add_player_to_club(message):
    pass




def declare_rival(message):
    pass

def declare_friend(message):
    pass
