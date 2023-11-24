import re
import asyncio
import math
import random
from typing import TypedDict
import time

from commandwrappers import limit_one_game_per_person, disable_if_update_coming, too_many_games_active
from gamecommands import newglolfgame
import db
from data.sponsors import generate_sponsor, apply_corporate_suffix


battleRoyaleTypeRegex = re.compile("1(v1)+")

timeBetweenMatchRegex = re.compile("(\d+)([mh])")
async def parse_tourney_message(message, command_body, debug=False):
    tourneytype = command_body.split("\n")[0].strip()


    if len(tourneytype) == 0:
        return await message.channel.send("What type of tournament? Try 'tourney 1v1'")

    time_between_matches_m = None # 5 minutes default, but you can change that with "60m" for 60 minutes
    minutes_specified = timeBetweenMatchRegex.search(tourneytype)
    if minutes_specified:
        # parse time between matches in minutes or hours
        time_between_matches_m = int(minutes_specified.group(1))
        if minutes_specified.group(2) == "h":
            time_between_matches_m *= 60

    is_battleroyale = battleRoyaleTypeRegex.search(tourneytype)
    if is_battleroyale:
        battletype = is_battleroyale.group(0)

        num_participants_per_game = battletype.count("1")
        if num_participants_per_game > 8:
            return await message.channel.send("umm thats probably too many people")

        is_club_game = False
        if 'club' in tourneytype:
            is_club_game = True

        return await battle_royale_glolftourney(message, num_participants_per_game, is_club_game=is_club_game, time_between_matches_m=time_between_matches_m, debug=debug)

    if tourneytype.startswith("resume"):
        tourney_sponsor_ID = tourneytype[len("resume"):].strip()

        if tourney_sponsor_ID == "":
            return await message.channel.send("Say the tourney's sponsor after 'resume'! Don't include any other words like Inc.")

        return await resume_tourney_command(message, tourney_sponsor_ID, time_between_matches_m, debug=debug)

    return await message.channel.send("umm im not sure what that tourney type means. maybe you could try 'tourney 1v1'")




def biggest_power_of_two_less_than(n):
    return 2 ** math.floor(math.log2(n))

def biggest_power_of_k_less_than(n, k=2):
    return k ** math.floor(math.log2(n)/math.log2(k))

async def tourney_series(message,
                glolfer_names, 
                wins_required=1,
                max_turns=60,
                round_name = 'a round',
                match_name = 'the important game',
                debug=False):

    winningname=None

    win_counts = {name:0 for name in glolfer_names} # todo: handle clones of the same name
    series_over = False

    unexpected_winners = []
    
    game_number = 0
    while not series_over:
        # do a game
        game_number += 1

        header = f"{match_name} of {round_name}!"
        if wins_required > 1:
            header = f"{match_name} of {round_name} - Game {game_number}, {'-'.join(f'{win_counts[name]}' for name in win_counts)} (First to {wins_required})!"
            

        winners = await newglolfgame(message, glolfer_names=glolfer_names, header=header,max_turns=max_turns, is_tournament=True, debug=debug, debug_skip_delays=debug)

        for winner in winners:

            # It's possible someone not in bracket entered the match and won through interdimensional shenanigans.
            # If so, The Manager will get involved.
            if winner.name not in win_counts:
                # the first time it happens, they get kicked out of the course
                win_counts[winner.name] = 0
                unexpected_winners.append(winner.name)
    
                managercomment = random.choice([
''':moneybag: **Oh No! What A Tragedy**
:moneybag: **Without A Winner**
:moneybag: **We Suppose The Match Must be Replayed**''',
''':moneybag: **Oh No! They're Out Of Bounds**
:moneybag: **Now How Will They Advance**
:moneybag: **We Suppose The Match Must be Replayed**''', 
''':moneybag: **We Apologize**
:moneybag: **For This Unsponsored Content**
:moneybag: **We Suppose The Match Must be Replayed**''',
''':moneybag: **As You Can See**
:moneybag: **Nobody Here Won**
:moneybag: **A Shame**
:moneybag: **We Suppose The Match Must be Replayed**'''])
    
                await message.channel.send(f"**Ka-thwhack! The Manager launches {winner.name} into the air and out of the course!**\n{managercomment}")
                await asyncio.sleep(15)
                continue

            if winner.name in unexpected_winners:
                # this happens if an unexpected guest wins for a second time
                managercomment = random.choice([":moneybag: **...**", ":moneybag: **...An Unexpected Chargeback**", ":moneybag: **...**", ":moneybag: **...**"])
                await message.channel.send(managercomment)

            # actual tourney win logic
            win_counts[winner.name] += 1 # also assumes entrant names are unique. and that whoever wins is a Glolfer or thing with a .name
            if win_counts[winner.name] >= wins_required:
                series_over = True

        if wins_required > 1:            
            await message.channel.send(f"The series is now {', '.join([f'{name} {win_counts[name]}' for name in win_counts])}!")

    # find winning names
    winning_names = [name for name in win_counts if win_counts[name] >= wins_required]
    if len(winning_names) == 1:
        await message.channel.send(f"**{winning_names[0]}** wins the series!")
        return winning_names[0]
    else:
        winningname = random.choice(winning_names)
        await message.channel.send(f"Tie game! **{winningname}** wins the tiebreaking duel to advance to the next round!")
        await asyncio.sleep(5)
        return winningname

def compute_round_name(num_matches_this_round, glolfers_per_game, round_num):

        if round_num == 0:
            return "qualifiers"

        if num_matches_this_round == 1:
            return "finals"
        if num_matches_this_round == glolfers_per_game and round_num != 1:
            return "almostfinals"
        if num_matches_this_round == glolfers_per_game**2 and round_num != 1:
            return "nearfinals"

        return f"round {round_num}"



class InProgressTourneyData:
    all_competitors: list[str]
    this_round_competitors_advancing: list[str] = []
    matches_yet_to_be_played = [] # list [a,b] , [c,d] list of people in competitors_this_round
    matches_completed=[] #: list[a,b]
    current_round_number: int = 0 # 0 = not yet started
    glolfers_per_game: int = 2
    wins_required: int = 1
    is_club_game = False
    debug = False
    time_between_matches_m = 5

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_next_match_competitors(self):
        if len(self.matches_yet_to_be_played) == 0:
            return []
        return self.matches_yet_to_be_played[0]

    def is_completed(self):
        if self.current_round_number > 0 and len(self.matches_yet_to_be_played) == 0 and len(self.this_round_competitors_advancing) <= 1:
            return True
        return False


    def process_match_result(self, winner_of_match_name: str):
        assert len(self.matches_yet_to_be_played) != 0 # if so, seed a new round

        current_match = self.get_next_match_competitors()
    
        # record winner
        self.this_round_competitors_advancing.append(winner_of_match_name)
        
        self.matches_yet_to_be_played = self.matches_yet_to_be_played[1:]
        self.matches_completed.append(current_match)

    def to_dict(self):
        # convert player into a dict, for saving in the DB
        return self.__dict__

async def fill_next_round_bracket(message, tourneydata):

    if tourneydata.current_round_number == 0:
        # at the start of a tourney, everyone gets into the first round bracket
        tourneydata.this_round_competitors_advancing = tourneydata.all_competitors[:]

    players_advancing = tourneydata.this_round_competitors_advancing[:]
    random.shuffle(players_advancing)
    tourneydata.this_round_competitors_advancing = []

    competitors_this_round = players_advancing

    # If # of entrants isn't a power of two, we don't have a full bracket, so give some contestants byes
    full_bracket_size = biggest_power_of_k_less_than(len(competitors_this_round), tourneydata.glolfers_per_game)
    if not len(competitors_this_round) == full_bracket_size:
        if tourneydata.glolfers_per_game > 2:
            return await message.channel.send(f"For this type of tourney I need a power-of-{glolfers_per_game} number of people. You have {len(players_advancing)}") # todo: move to main command so the return quits properly
        num_matches_required = len(players_advancing) - full_bracket_size


        # only some of you compete this round
        competitors_this_round = players_advancing[0:num_matches_required*tourneydata.glolfers_per_game]

        # the rest get to advance automatically
        tourneydata.this_round_competitors_advancing = players_advancing[num_matches_required*tourneydata.glolfers_per_game:]

        await message.channel.send(f"{', '.join(tourneydata.this_round_competitors_advancing)} randomly recieve byes and move onto the next round. Let's see who joins them!")

    tourneydata.matches_yet_to_be_played = []
    tourneydata.matches_completed = []

    for i in range(0, len(competitors_this_round), tourneydata.glolfers_per_game):
        tourneydata.matches_yet_to_be_played.append(competitors_this_round[i : i + tourneydata.glolfers_per_game])
    tourneydata.current_round_number += 1


def get_tourney_data(tourney_sponsor_ID):
    tourneydata = db.get_tourney_data(tourney_sponsor_ID)
    if tourneydata is None:
        return None
    return InProgressTourneyData(**tourneydata)

async def one_tourney_series(message, tourney_sponsor_ID, debug=False):

    tourneydata = get_tourney_data(tourney_sponsor_ID)
    
    if len(tourneydata.matches_yet_to_be_played) == 0:
        # end of a round. begin the next round
        if len(tourneydata.this_round_competitors_advancing) != 1:
            await fill_next_round_bracket(message, tourneydata)
            db.set_tourney_data(tourney_sponsor_ID, tourneydata.to_dict())
        else:
            # this tourney is already over. we probably shouldn't be here, but just in case, have this fallback
            await message.channel.send(f"**{tourneydata.this_round_competitors_advancing[0]} wins the tournament!**")
            db.delete_tourney_data(tourney_sponsor_ID)
            return



    current_competitors = tourneydata.get_next_match_competitors()

    # Do one round
    match_number = len(tourneydata.matches_completed)+1
    total_matches = len(tourneydata.matches_completed)+len(tourneydata.matches_yet_to_be_played)

    type_of_round = "Match"
    if tourneydata.wins_required > 1:
        type_of_round = "Series"

    round_name = compute_round_name(total_matches, tourneydata.glolfers_per_game, tourneydata.current_round_number)

    match_name = f"{type_of_round} {match_number}/{total_matches}"
    if match_number == total_matches and round_name != "finals" and total_matches == 1:
        match_name = f"Final {type_of_round.lower()}"

    # compute number of turns for glolf game
    if tourneydata.is_club_game:
        max_turns = 100
    else: # regular people competing
        max_turns = 60
        if total_matches >= 2*tourneydata.glolfers_per_game**3:
            max_turns = 40

    if tourneydata.debug:
        max_turns = 10

    # make club games a best of 3
    if tourneydata.is_club_game and tourneydata.wins_required == 1:
        tourneydata.wins_required = 2
    
    winner_name = await tourney_series(message,
        glolfer_names=current_competitors,
        round_name=round_name,
        match_name=match_name,
        max_turns=max_turns,
        debug=debug,
        wins_required=tourneydata.wins_required)

    tourneydata.process_match_result(winner_name)

    
    if len(tourneydata.matches_yet_to_be_played) == 0:
        # End of round!
        if len(tourneydata.this_round_competitors_advancing) > 1:
            # Announce round results! The new brackets will be computed next time
            await message.channel.send(f"**{round_name.title()} results:** {len(tourneydata.this_round_competitors_advancing)} contestants move on: **{', '.join(tourneydata.this_round_competitors_advancing)}**.")
            await fill_next_round_bracket(message, tourneydata)
        else:
            await message.channel.send(f"**{tourneydata.this_round_competitors_advancing[0]} wins the tournament!**")

    db.set_tourney_data(tourney_sponsor_ID, tourneydata.to_dict())

def relative_discord_timestamp(timestring):
    return f"<t:{timestring}:R>"
def discord_timestamp(timestring):
    return f"<t:{timestring}:f>"


@disable_if_update_coming
@limit_one_game_per_person
async def battle_royale_glolftourney(message, glolfers_per_game=2, time_between_matches_m=None, is_club_game=False, debug=False):

    # a tourney where each game has multiple people, but only one can win each game
    # if glolfers_per_game is 2, it's a 1v1, if glolfers_per_game is 3, each game is a 1v1v1, etc
    assert glolfers_per_game > 1
    arguments = message.content.split("\n") #first line has "!tourney" on it
    glolfer_names = []
    if len(arguments) > 1:
        glolfer_names = arguments[1:]
        num_players = len(glolfer_names)
        if num_players == 1:
            await message.channel.send("That's a short tournament... I guess they win by default!")
            return None
        if num_players < glolfers_per_game:
            await message.channel.send("There aren't enough players for even a single match. Everyone wins!")
            return None
    else: # 0 players
        await message.channel.send("To use, please give a list of competitors after the command, each on a separate line.")
        return


    if time_between_matches_m is None:
        time_between_matches_m = 5 # default value

    if too_many_games_active():
        await message.channel.send("There's too many games going on right now. To avoid lag, please wait a little bit until some games are done and try again later!")
        return
    
    full_bracket_size = biggest_power_of_k_less_than(len(glolfer_names), glolfers_per_game)
    if not len(glolfer_names) == full_bracket_size:
        if glolfers_per_game > 2:
            return await message.channel.send(f"For this type of tourney I need a power-of-{glolfers_per_game} number of people. You have {len(glolfer_names)}")

    tourney_sponsor_ID = generate_sponsor()

    if not is_club_game:
        await message.channel.send(f"{len(glolfer_names)}-person tournament starting, sponsored by {apply_corporate_suffix(tourney_sponsor_ID).title()}...")
    else:
        await message.channel.send(f"{len(glolfer_names)}-club tournament starting, sponsored by {apply_corporate_suffix(tourney_sponsor_ID).title()}...")

    random.shuffle(glolfer_names)

    tourneydata = InProgressTourneyData(all_competitors=glolfer_names[:], glolfers_per_game=glolfers_per_game, current_round_number=0, debug=debug, time_between_matches_m=time_between_matches_m, is_club_game=False)


    db.set_tourney_data(tourney_sponsor_ID, tourneydata.to_dict())
    
    await run_battle_royale(message, tourney_sponsor_ID, time_between_matches_m=time_between_matches_m, debug=debug)


@disable_if_update_coming
@limit_one_game_per_person
async def resume_tourney_command(message, tourney_sponsor_ID, time_between_matches_m=None, debug=False):
    # todo: fix bug where you can resume a tourney multiple times, including while the same tourney is running

    # tourney sponsor IDs are one word, lowercase.
    tourney_sponsor_ID = tourney_sponsor_ID.lower()
    #if they entered "sponsor inc." take the first word, "sponsor"
    if " " in tourney_sponsor_ID:
        tourney_sponsor_ID = tourney_sponsor_ID.split(" ")[0] 
    
    tourneydata = get_tourney_data(tourney_sponsor_ID)
    if tourneydata is None:
        return await message.channel.send("No paused tourney with that sponsor. Maybe it finished?")

    print(time_between_matches_m, tourneydata.time_between_matches_m)
    if time_between_matches_m is None:
        time_between_matches_m = tourneydata.time_between_matches_m

    await run_battle_royale(message, tourney_sponsor_ID, time_between_matches_m=time_between_matches_m, debug=debug)

async def run_battle_royale(message, tourney_sponsor_ID, time_between_matches_m=5, debug=False):
    # repeatedly parse from the DB then run one match/series of a tourney in a loop! 
    #If it's cancelled due to an error, that's okay, because it's saved in the DB

    time_between_matches_s = time_between_matches_m*60 # 5 minutes

    tourneydata = get_tourney_data(tourney_sponsor_ID)
    if tourneydata is None:
        return await message.channel.send("No active tourney with that name. Maybe it finished?")

    if tourneydata.is_completed():
        await message.channel.send(f"Oops, I forgot to announce it. **{tourneydata.this_round_competitors_advancing[0]} wins the tournament!**")

    while not tourneydata.is_completed():
        await one_tourney_series(message, tourney_sponsor_ID, debug)
        tourneydata = get_tourney_data(tourney_sponsor_ID) # reload data so we don't infinite loop

        if tourneydata.is_completed():
            break

        # next, sleep for a while in between the matches
        next_competitors = tourneydata.get_next_match_competitors()
        next_match_time = int(time.time() + time_between_matches_s) # Round to nearest second, otherwise discord timestamp output fails

        # figure out how long to wait in between reminders
        reminder_times_m = [1,5,60]
        reminder_times_deltas = [1,4,55] #time between reminder_times_m[i],reminder_times_m[i+1]

        sleep_deltas_s = []
        remaining_sleep_time_s = time_between_matches_s
        for time_m in reminder_times_deltas:
            if remaining_sleep_time_s > time_m*60:
                remaining_sleep_time_s -= time_m*60
                sleep_deltas_s.append(time_m*60) #time till next reminder, total remaining
        sleep_deltas_s.append(remaining_sleep_time_s)

        # integrate to find out at each reminder time, how much time is left
        sleep_info = [(sleep_deltas_s[i], sum(sleep_deltas_s[0:i+1])) for i in range(len(sleep_deltas_s))]

        for time_till_next_reminder_s, time_till_match_s in sleep_info[::-1]:
            #print(sleep_deltas_s)

            if time_till_match_s > 10*60:
                await message.channel.send(f"The next match, between {' and '.join(next_competitors)}, will begin {relative_discord_timestamp(next_match_time)}, at {discord_timestamp(next_match_time)}.")
            else:
                await message.channel.send(f"The next match, between {' and '.join(next_competitors)}, will begin in {int(time_till_match_s/60)} minute{'' if time_till_match_s <= 60 else 's'}...")
            await asyncio.sleep(time_till_next_reminder_s) 

    db.delete_tourney_data(tourney_sponsor_ID)

