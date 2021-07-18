
import random
import logging
logger = logging.getLogger(__name__)

from game import SingleHole, SingleHoleScoresheet
import utils
import entities
from modifications.current_rules import get_permanent_modifiers

from data.scorecards import SingleHoleScoresheet

from clubs.player_subbing_in import SubInNextPlayerOnceSomeoneScoresInAClubGame
from clubs.clubs import create_competing_club, CompetingClub


class ClubGame(SingleHole):
    def __init__(self, debug=False, club_names=[], max_turns=200, is_tournament=False):
        self.player_scorecards = {}

        super().__init__(debug=debug, glolfer_names=club_names, max_turns=max_turns, is_tournament=is_tournament)

        self.modifiers += [SubInNextPlayerOnceSomeoneScoresInAClubGame(self)]


    def setup_first_glolfers(self, club_names):
        if len(club_names) == 0:
            logger.info(f"Game {self.id}: No clubs!")
            raise ValueError("no clubs found in club game")

        # place one glolfer at each hole, in order, then any more are random
        placed_glolfers = 0
        flags = [obj for obj in self.objects if type(obj) == entities.Hole]

        self.clubs = []        
        for club_name in club_names:
            club = create_competing_club(self, club_name) # may raise a NoSuchClubError
            self.clubs.append(club)
            self.add_scorecard_if_doesnt_exist(club)

            first_player = club.choose_first_glolfer()

            # place first player on field
            if placed_glolfers < len(flags):
                # place glolfer #1 on flag #1, glolfer #2 on flag #2, etc
                new_glolfer_pos = flags[placed_glolfers].position
                placed_glolfers += 1
            else:
                # Out of flags, throw em anywhere
                new_glolfer_pos = self.course.random_position_on_course()   
            first_player.set_position(new_glolfer_pos)

            # self.add_player(first_player) # this gives them a scorecard, but we want only the teams to have scorecards.
            self.objects.append(first_player)

        # add a scorecard for every player
        for club in self.clubs:
            for player in club.glolfers:
                self.player_scorecards[player] = SingleHoleScoresheet(player)

    def get_player_scorecard(self, player):
        return self.player_scorecards[player]

    def print_score(self):
        # Prints total team score, then individual player scores
        string = ""
        current_winners = self.compute_winners()

        for scoring_thing in self.scores:
            scorecard = self.scores[scoring_thing]
            scorecard_string = scorecard.printed_representation()
            if scoring_thing in current_winners and self.scores[scoring_thing].total_strokes > 0 and not self.over:
                scorecard_string += " 👀"
            string += f"{scorecard_string} \n"

            if type(scoring_thing) == CompetingClub:
                for player in scoring_thing.glolfers:
                    scorecard = self.player_scorecards[player]
                    scorecard_string = scorecard.printed_representation()
                    string += f"- {scorecard_string} \n"
        return string

    def increase_score(self, scoring_player, added_strokes=0, added_balls_scored=0, added_scored_strokes=0):
        if type(scoring_player) == entities.Glolfer and scoring_player.club is not None:
            # scoring player is in a club. increase score for the club
            super().increase_score(scoring_player.club, added_strokes, added_balls_scored, added_scored_strokes)
            # increase individual player's score too
            if scoring_player in self.player_scorecards:
                self.player_scorecards[scoring_player].scored_strokes += added_scored_strokes
                self.player_scorecards[scoring_player].balls_scored += added_balls_scored
                self.player_scorecards[scoring_player].total_strokes += added_strokes
        else:
            # scoring thing not in a team
            super().increase_score(scoring_player, added_strokes, added_balls_scored, added_scored_strokes)
