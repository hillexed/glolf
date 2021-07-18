import asyncio
import logging
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
        

    await newglolfgame(message, glolfer_names,debug=debug)

async def newglolfgame(message, glolfer_names, header=None, max_turns=60, is_tournament=False, debug=False):
    # start a round of glolf and return the winning players's names

    glolfgame = await message.channel.send("Beginning game...")
    logger.info(f"Starting game between {glolfer_names} in channel #{message.channel} in server '{message.channel.guild.name}'")
    try:
        if "club" in message.content.split("\n")[0]:
            if max_turns == 60:
                max_turns = 120
            game = ClubGame(debug=debug,club_names=glolfer_names,max_turns=max_turns,is_tournament=is_tournament)
        else:
            game = SingleHole(debug=debug,glolfer_names=glolfer_names,max_turns=max_turns,is_tournament=is_tournament)
        await asyncio.sleep(2)
        await glolfgame.edit(content=game.printgamestate(header=header))
        await asyncio.sleep(2)

        while not game.over:
            delay = game.update()
            await glolfgame.edit(content=game.printgamestate(header=header))
            await asyncio.sleep(delay)

        await glolfgame.edit(content=game.printgamestate(include_board=True,header=header))
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
