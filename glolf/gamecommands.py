import asyncio
import logging
import random
logger = logging.getLogger(__name__)

from commandwrappers import disable_if_update_coming, limit_one_game_per_person, too_many_games_active
from game import SingleHole
from clubs.clubgame import ClubGame
from clubs.clubs import NoSuchClubError

@disable_if_update_coming
@limit_one_game_per_person
async def glolfcommand(message, message_body, debug=False):
    # parse a glolf command

    arguments = message_body.split("\n") #first line has "!glolf" on it
    glolfer_names = []
    if len(arguments) > 1: # 0 players is fine
        glolfer_names = arguments[1:]
        if len(glolfer_names) == 1:
            await message.channel.send("It's too dangerous to glolf alone. Bring an opponent.")
            return

    if too_many_games_active():
        await message.channel.send("There's too many games going on right now. To avoid lag, please wait a little bit till some games are done and try again later!")
        return
    print(arguments)
    if 'bo3' in arguments[0]:
        return await best_of_n_glolfgame(message, glolfer_names, wins_required=2, debug=debug)
    if 'bo5' in arguments[0]:
        return await best_of_n_glolfgame(message, glolfer_names, wins_required=3, debug=debug)
    if 'bo7' in arguments[0]:
        return await best_of_n_glolfgame(message, glolfer_names, wins_required=4, debug=debug)
    return await newglolfgame(message, glolfer_names,debug=debug)

async def best_of_n_glolfgame(message, glolfer_names, wins_required=3, max_turns=60, debug=False):

    winningname=None

    win_counts = {name:0 for name in glolfer_names} # todo: handle clones of the same name
    series_over = False
    
    game_number = 0
    while not series_over:
        # do a game
        game_number += 1

        header = ""
        if wins_required > 1:
            header = f"Game {game_number}, {'-'.join(f'{win_counts[name]}' for name in win_counts)} (First to {wins_required})!"

        winners = await newglolfgame(message, glolfer_names=glolfer_names, header=header,max_turns=max_turns, is_tournament=True, debug=debug)

        for winner in winners:
            win_counts[winner.name] += 1 # also assumes entrant names are unique. and that whoever wins is a Glolfer or thing with a .name
            if win_counts[winner.name] >= wins_required:
                series_over = True
        if wins_required > 1:            
            await message.channel.send(f"The series is now {', '.join([f'{name} {win_counts[name]}' for name in win_counts])}!")

    # find winning names
    winning_names = [name for name in win_counts if win_counts[name] >= wins_required]

    if len(winning_names) > 1:
        random_winner = random.choice(winning_names)
        await message.channel.send(f"**{random_winner} wins the tiebreaking duel to win the series!**")
        return random_winner
    else:
        winning_name = winning_names[0]
        await message.channel.send(f"**{winning_name} wins the series!**")
        return winning_name

async def newglolfgame(message, glolfer_names, header=None, max_turns=60, is_tournament=False, debug=False, debug_skip_delays=False):
    # start a round of glolf and return the winning players's names

    glolfgame = await message.channel.send("Beginning game...")

    if message.guild is not None:
        logger.info(f"Starting game between {glolfer_names} in channel #{message.channel.name if message.channel is not None else message.channel} in server '{message.guild.name if message.guild is not None else message.guild}'")
    try:
        if "club" in message.content.split("\n")[0]:
            if max_turns == 60:
                max_turns = 120
            game = ClubGame(debug=debug,club_names=glolfer_names,max_turns=max_turns,is_tournament=is_tournament)
        else:
            game = SingleHole(debug=debug,glolfer_names=glolfer_names,max_turns=max_turns,is_tournament=is_tournament)
    
        if not debug_skip_delays:
            await asyncio.sleep(2)
        await glolfgame.edit(content=game.printgamestate(header=header))
        if not debug_skip_delays:
            await asyncio.sleep(2)

        while not game.over:
            delay = game.update()
            await glolfgame.edit(content=game.printgamestate(header=header))
            if not debug_skip_delays:
                await asyncio.sleep(delay)

        await glolfgame.edit(content=game.printgamestate(include_board=True,header=header))
        if not debug_skip_delays:
            await asyncio.sleep(10)
        await glolfgame.edit(content=game.printgamestate(include_board=False,header=header))
        return game.compute_winners()

    except NoSuchClubError as e:
        await glolfgame.add_reaction('⚠️')
        logger.exception(e)
        await message.channel.send(f"umm i phoned around but i couldnt find the club named {e.args[0]}. sorry")
        raise e
    except (Exception, KeyboardInterrupt) as e:
            await glolfgame.add_reaction('⚠️')
            logger.exception(e)
            raise e
