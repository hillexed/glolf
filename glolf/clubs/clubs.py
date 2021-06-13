from data.players import get_player_from_name

class Club:
    # ingame version
    def __init__(self, club_name):
        club_name = command_body.strip()
        clubdata = db.get_club_data(club_name)
        if clubdata is None:
            raise ValueError("No club named {} found".format(club_name))

        self.data = GlolfClubData(*clubdata)
        self.name = self.data.name

        self.players = [get_player_from_name(player_Name) for player_name in self.data.player_names]

    def get_next_player(self, player_name)
        index = self.data.player_names.index(playername) # raises ValueError if not found
        next_index = (index+1) % len(self.data.player_names)
        return self.data.players[next_index]



