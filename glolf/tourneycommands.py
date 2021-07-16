import re
import asyncio
import math
import random

from commandwrappers import limit_one_game_per_person, disable_if_update_coming, too_many_games_active
from gamecommands import newglolfgame

async def parse_tourney_message(message, command_body, debug=False):
    tourneytype = command_body.split("\n")[0].strip()

    if len(tourneytype) == 0:
        return await message.channel.send("What type of tournament? Try 'tourney 1v1'")

    is_battleroyale = battleRoyaleTypeRegex.match(tourneytype)
    if is_battleroyale:
        battletype = is_battleroyale.group(0)

        num_participants_per_game = battletype.count("1")
        if num_participants_per_game > 8:
            return await message.channel.send("umm thats probably too many people")
        return await battle_royale_glolftourney(message, num_participants_per_game, debug=debug)

    return await message.channel.send("umm im not sure what that tourney type means. maybe you could try 'tourney 1v1'")




def biggest_power_of_two_less_than(n):
    return 2 ** math.floor(math.log2(n))

def biggest_power_of_k_less_than(n, k=2):
    return k ** math.floor(math.log2(n)/math.log2(k))

async def tourney_series(message, 
                wins_required=1,
                glolfer_names=glolfers,
                max_turns=max_turns,
                round_name = 'a round',
                match_name = 'the important game',
                debug=False):

    winningname=None

    win_counts = {name:0 for name in glolfer_names} # todo: handle clones of the same name
    series_over = False
    
    game_number = 0
    while not series_over:
        # do a game
        game_number += 1

        header = f"{match_name} of {round_name}!"
        if wins_required > 1:
            header = f"Game {game_number} (First to {wins_required}) - {match_name} of {round_name}!"
            

        winners = await newglolfgame(message, glolfer_names=glolfers, header=header,max_turns=max_turns, is_tournament=True, debug=debug)
        for winner in winners:
            win_counts[winner.name] += 1 # also assumes entrant names are unique. and that whoever wins is a Glolfer or thing with a .name
            if win_counts[winner.name] >= wins_required:
                series_over = True

    # find winning names
    winning_names = [name for name in win_counts if win_counts[name] >= wins_required]
    if len(winning_names) == 1:
        return winning_names[0]
    else
        winningname = random.choice(winning_names)
        await message.channel.send(f"Tie game! **{winningname.name}** wins the tiebreaking duel to advance to the next round!")
        await asyncio.sleep(5)
        return winningname

def compute_round_name(competitors_this_round, move_onto_next_round, glolfers_per_game, round_num):

        total_competitors = len(competitors_this_round) + len(move_onto_next_round) # not sure this is needed

        if len(move_onto_next_round) > 0:
            # this is right after move_onto_next_round should be []
            # if it isn't [], we're in the first round of a tourney with a non-power-of-two number of entrants
            return "qualifiers"

        if total_competitors == glolfers_per_game:
            return "the finals"
        if total_competitors == glolfers_per_game**2 and round_num != 1:
            return "the almostfinals"
        if total_competitors == glolfers_per_game**3 and round_num != 1:
            return "the nearfinals"

        return f"round {round_num}"


battleRoyaleTypeRegex = re.compile("1(v1)+")

@disable_if_update_coming
@limit_one_game_per_person
async def battle_royale_glolftourney(message, glolfers_per_game=2, debug=False):
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

    if too_many_games_active():
        await message.channel.send("There's too many games going on right now. To avoid lag, please wait a little bit till some games are done and try again later!")
        return


    await message.channel.send(f"{len(glolfer_names)}-person tournament starting...")
    move_onto_next_round = []

    random.shuffle(glolfer_names)

    competitors_this_round = glolfer_names[:]

    # If # of entrants isn't a power of two, we don't have a full bracket, so give some contestants byes
    full_bracket_size = biggest_power_of_k_less_than(len(glolfer_names), glolfers_per_game)
    if not len(glolfer_names) == full_bracket_size:
        if glolfers_per_game > 2:
            return await message.channel.send(f"For this type of tourney I need a power-of-{glolfers_per_game} number of people. You have {len(glolfer_names)}")
        num_matches_required = len(glolfer_names) - full_bracket_size

        competitors_this_round = glolfer_names[0:num_matches_required*glolfers_per_game]
        move_onto_next_round = glolfer_names[num_matches_required*glolfers_per_game:]

        print(len(competitors_this_round)/glolfers_per_game + len(move_onto_next_round))
        await message.channel.send(f"{', '.join(move_onto_next_round)} randomly recieve byes and move onto the next round. Let's see who joins them!")

    # actual tourney time!
    round_num = 0
    while len(competitors_this_round) > 1:
        round_num+= 1

        max_turns = 60
        if len(competitors_this_round) >= 2*glolfers_per_game**3:
            max_turns = 40
        if debug:
            max_turns = 3

        round_name = compute_round_name(competitors_this_round, move_onto_next_round, glolfers_per_game, round_num)

        for index in range(0,len(competitors_this_round)-1,glolfers_per_game):
            # go down the bracket
            # competitors
            glolfers = [competitors_this_round[index+i] for i in range(glolfers_per_game) if index+i < len(competitors_this_round)]
            await asyncio.sleep(2)

            match_number = int(index/glolfers_per_game)+1
            total_matches = int(len(competitors_this_round)/glolfers_per_game)

            match_name = f"Match {match_number}/{total_matches}"
            if match_number == total_matches and round_name != "the finals" and total_matches == 1:
                match_name = "Final match"
            
            winning_name = await tourney_series(message, wins_required=1,
                glolfer_names=glolfers,
                round_name=round_name,
                match_name=match_name,
                max_turns=max_turns,
                debug=debug,
                wins_required=1)
            move_onto_next_round.append(winningname.name)

        if len(move_onto_next_round) > 1:

            round_descriptor = f"Round {round_num} results:"
            if len(move_onto_next_round) == glolfers_per_game and round_num != 1:
                round_descriptor = "Almostfinals results:"
            if len(move_onto_next_round) == glolfers_per_game**2 and round_num != 1:
                round_descriptor = "Nearfinals results:"

            await message.channel.send(f"**{round_descriptor}** {len(move_onto_next_round)} contestants move on: **{', '.join(move_onto_next_round)}**. Next round starts in five minutes...")
            await asyncio.sleep(60*5)

        competitors_this_round = move_onto_next_round
        move_onto_next_round = []

    await message.channel.send(f"**{competitors_this_round[0]} wins the tournament!**")


