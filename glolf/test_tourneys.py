from tourneycommands import InProgressTourneyData, fill_next_round_bracket, parse_tourney_message, battle_royale_glolftourney, run_battle_royale
import asyncio



async def mocksendmessage(blah):
    print(blah)
    return editablemessage()

class editablemessage:
    async def add_reaction(self, content):
        print(f"Reaction added: {content}")
    async def edit(self, content):
        print(f"Edited: {content}")

async def addreact(react):
    pass

class message:
    class channel:
        send = mocksendmessage
        class guild:
            name = "server"
    author = "me"
    add_reaction = addreact
    content = '''1v1 1m
a
b
c
d'''


async def dostuff():
    x = InProgressTourneyData(all_competitors=['a','b','c','d','e'])
    x.this_round_competitors_advancing = x.all_competitors[:] # everyone gets to be seeded at first
    print(x.this_round_competitors_advancing)
    await fill_next_round_bracket(message, x)
    print(x.matches_yet_to_be_played)

asyncio.run(dostuff())


asyncio.run(battle_royale_glolftourney(message, glolfers_per_game=2, time_between_matches_m=20, is_club_game=False, debug=False))

#asyncio.run(run_battle_royale(message, "test"))
