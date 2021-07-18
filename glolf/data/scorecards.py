class SingleHoleScoresheet:
    def __init__(self, player):
        self.player = player
        self.scored_strokes = 0
        self.total_strokes = 0
        self.balls_scored = 0

    def printed_representation(self):
        return f"{self.player.get_display_name(with_mods_in_parens=True)}: {self.balls_scored} holes, {self.total_strokes} strokes"


class NPCScorecardDummyEntity:
    '''
    A class that acts like a Glolfer() to allows arbitrary strings to show up in a scoresheet. 
    '''
    # in the future i should probably change these to specific Glolfers so that it doesn't mess things up in a callback if they're handed one of these instead of a Glolfer
    # These players show up in the scorecard, and can win games, but can't advance in a tourney setting
    def __init__(self, name, emoji=""):
        self.name = name
        self.displayEmoji = emoji
        self.club = None

    def get_display_name(self, with_mods_in_parens = False):
        if self.displayEmoji == "":
            return self.name
        return f"{self.name} {self.displayEmoji}"


NPC_cache = {}
def get_NPC_dummy_player(name, emoji = ""):
    if name not in NPC_cache:
        NPC_cache[name] = NPCScorecardDummyEntity(name, emoji)
    return NPC_cache[name]


