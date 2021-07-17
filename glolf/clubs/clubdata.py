from __future__ import annotations
from typing import NamedTuple, Optional

import utils
import data

lame_mottos = (("we're pretty good", "better than the worse guys", "winning > losing", "not THAT bad", "it's Tuesday", "fight like a dodo")) 

class GlolfClubData(NamedTuple):
    name: str
    emoji: str
    motto: str
    cheer: Optional[str]
    
    owner_ids : list[str]
    modifications: list[Modification]

    player_names: list[str] # they're regular players for now
    caddy_names : list[str] # they're regular players for now

    friends: list[str]
    rivals: list[str]
    sponsors: list[str]

    displayed_loft_education: list[str] # a list of academic degrees
    loft_degrees: float = 10

    theme_song = None
    tenacity: float = 0
    weight: float = 0
    musclitude: float = 0
    unworthiness: float = 0
    penalty_strokes: int = 0
    roboticization: float = 0

    #stlats = {wins, losses, tourney_wins, balls_scored, total_strokes, unworthiness}

    def printTeamInfo(self):

        cheer_string = "" if self.cheer is None else f'**Cheer:** {self.cheer}\n'

        player_string = "**Glolfers**\n"
        for player_name in self.player_names:
            player = data.players.get_player_from_name(player_name)

            best_stlat_name, best_stlat = player.get_biggest_stlat_rating()

            player_string += f"{player.get_display_name()} - {best_stlat_name.title()}: {data.playerstlats.format_stlat_display(best_stlat)}\n"

        if len(self.caddy_names) != 0:
            player_string += "\n**Caddies**"
            for player_name in self.caddy_names:
                player = data.players.get_player_from_name(player_name)
                player_string += player.get_display_name() + '\n'
        player_string += '\n'

        loft_section = ''
        if self.loft_degrees != 0:
            loft_section += f'\n**Loft:** {int(self.loft_degrees)} degrees'
            if len(self.displayed_loft_education) > 0:
                loft_section += f' (Most recent: {utils.format_list_with_commas(self.displayed_loft_education)})'

        modification_section = ""
        if len(self.modifications) > 0:
            modification_section = "**Modifications: **\n" + utils.format_list_with_commas([modification.emoji for mod in self.modifications]) + '\n'
        

        relationships_section = ''
        if len(self.rivals) != 0:
            relationships_section += '\n- **Rivals:** ' + utils.format_list_with_commas(self.rivals)
        if len(self.friends) != 0:
            relationships_section += '\n- **Friends:** ' + utils.format_list_with_commas(self.friends)
        if len(self.sponsors) != 0:
            relationships_section += '\n- **Sponsors:** ' + utils.format_list_with_commas(self.sponsors)
        if len(relationships_section) != 0:
            relationships_section = "**Relationships:**"+relationships_section # goes BEFORE relationships

        return f'''
**{self.emoji} {self.name}**
_{self.motto}_
{cheer_string}{loft_section}
{player_string}{modification_section}{relationships_section}
'''.strip()
