NPC_cache = {}
def get_NPC_scorecard(name, emoji = ""):
    if name not in NPC_cache:
        NPC_cache[name] = NPCScorecardEntry(name, emoji)
    return NPC_cache[name]

class NPCScorecardEntry:
    # in the future i should probably change these to specific Glolfers so that it doesn't mess things up in a callback if they're handed one of these instead of a Glolfer
    # These players show up in the scorecard, and can win games, but can't advance in a tourney setting
    def __init__(self, name, emoji=""):
        self.name = name
        self.displayEmoji = emoji

    def get_display_name(self, with_mods_in_parens = False):
        if self.displayEmoji == "":
            return self.name
        return f"{self.name} {self.displayEmoji}"
