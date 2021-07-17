from data.players import get_player_from_name
import db

class Club:
    # ingame version
    def __init__(self, data: GlolfClubData):
        self.data = data
        self.name = self.data.name

        self.players = [get_player_from_name(player_name) for player_name in self.data.player_names]

    def get_next_player(self, player_name)
        index = self.data.player_names.index(playername) # raises ValueError if not found
        next_index = (index+1) % len(self.data.player_names)
        return self.data.players[next_index]


class NoSuchClubError(ValueError):
    pass

def get_club(club_name):
    clubdata = db.get_club_data(club_name)
    if clubdata is None:
        return NoSuchClubError()

    club = GlolfClubData(*clubdata)
    return Club(clubdata)


