from data.players import get_player_from_name
import db
from .clubdata import GlolfClubData
from NPCglolfer import AIGlolfer
import random

class CompetingClub:
    # ingame version
    def __init__(self, game, data: GlolfClubData):
        self.data = data
        self.name = self.data.name

        self.glolfers = [AIGlolfer(game, playername=player_name, club=self) for player_name in self.data.player_names]

    def choose_first_glolfer(self):
        return random.choice(self.glolfers)

    def get_next_glolfer(self, glolfer):
        #if glolfer not in self.glolfers:
        #    return self.glolfers[0]
        index = self.glolfers.index(glolfer) # raises ValueError if not found
        next_index = (index+1) % len(self.glolfers)
        return self.glolfers[next_index]

    def get_display_name(self, with_mods_in_parens=True):
        # This shows up on the scoresheet. with_mods_in_parens ignored
        return f"{self.data.emoji} {self.name}"

class NoSuchClubError(ValueError):
    pass

def create_competing_club(game, club_name):
    # given a club name and a SingleHole, fetch the data from the DB and create a CompetingClub to compete in this game
    club_dict = db.get_club_data(club_name)
    if club_dict is None:
        raise NoSuchClubError(club_name)

    clubdata = GlolfClubData(*club_dict)
    return CompetingClub(game, clubdata)


