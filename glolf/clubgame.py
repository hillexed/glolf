
import random
import logging
logger = logging.getLogger(__name__)

from game import SingleHole
import utils
import entities
from modifications.current_rules import get_permanent_modifiers
from modifications.modification import Modification

from clubs.player_subbing_in import GlolferInGlolfCartSubbingIn

class NeedsToTagIn(Modification):
    def __init__(self, target_cart):
        self.target = target_cart

    def on_glolfer_update(self, current_action):
        current_action["action"] = "move"

    def on_glolfer_move(self, target):
        return self.target


class SubInNextPlayerOnceSomeoneScoresInAClubGame(Modification):
    def __init__(self, game):
        self.game = game

    def on_score(scoring_player, ball, hole_position):
        scoring_team = scoring_player.team
        if scoring_team is not None:
            
            next_player = scoring_player.get_next_player(playerdata)

            cart = GlolferInGlolfCartSubbingIn(scoring_player, next_player)
            self.game.add_object(cart)

            scoring_player.modifications += NeedsToTagIn(cart)


class ClubGame(SingleHole):
    def __init__(self, debug=False, club_names=[], max_turns=60, is_tournament=False):
        super().__init__(self, debug, glolfer_names=club_names, max_turns, is_tournament)

        self.modifications += [SubInNextPlayerOnceSomeoneScoresInAClubGame(self)]


    def setup_first_glolfers(self, club_names):
        if len(glolfer_names) == 0:
            logger.info(f"Game {self.id}: No clubs!")
            raise ValueError("no clubs found in club game")

        # place one glolfer at each hole, in order, then any more are random
        placed_glolfers = 0
        flags = [obj for obj in self.objects if type(obj) == entities.Hole]

        for club_name in club_names:

            club = get_club(club_name)
            new_playername = club.player_names[0]

            if placed_glolfers < len(flags):
                # place glolfer #1 on flag #1, glolfer #2 on flag #2, etc
                new_glolfer_pos = flags[placed_glolfers].position
                placed_glolfers += 1
            else:
                # Out of flags, throw em anywhere
                new_glolfer_pos = self.course.random_position_on_course()   
            newglolfer = entities.Glolfer(self, position=starting_position, playername=playername)      
            self.add_player_by_name(new_glolfer_pos, playername=name)

    def print_score(self):
        string = ""
        current_winners = self.compute_winners()

        for team in self.scores:
            scorecard = self.scores[player]
            scorecard_string = scorecard.printed_representation()
            if team in current_winners and self.scores[team].total_strokes > 0 and not self.over:
                team_scorecard_string += " 👀"

            player_scorecard_string = ''
            #for player in current_active_player(team):
            #    player_scorecard_string += self.player.get_display_name(with_mods_in_parens=True) + '\n'

            string += f"{team_scorecard_string} \n"

        return string

    def increase_score(self, scoring_player, added_strokes=0, added_balls_scored=0, added_scored_strokes=0):
        if scoring_player not in self.scores: 
            self.scores[scoring_player] = SingleHoleScoresheet(scoring_player.team.name)
        self.scores[scoring_player].scored_strokes += added_scored_strokes
        self.scores[scoring_player].balls_scored += added_balls_scored
        self.scores[scoring_player].total_strokes += added_strokes
