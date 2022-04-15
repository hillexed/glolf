import random, math
import logging
logger = logging.getLogger(__name__)


from .entity import Entity
from data.scorecards import get_NPC_dummy_player
from .misc import ScoreConfetti
import utils
from utils.vecmath import Vector

class Ball(Entity):
    displayEmoji = "⚪"
    showOnBoard = True
    type = "ball"
    zIndex = 1 
    def __init__(self, game, position = [0.0,0.0]):
        self.position = Vector(position)
        self.game = game
        self.times_hit = 0
        self.strokes = 0
        self.last_hit_by = None
        self.displayEmoji = random.choice(("⚪","🔴","⚽","🟣","🟢","🟤","🟡","🔵","🟠"))

    

    def update(self):
        self.check_if_ball_scored()

    def reset_at_random_point(self):
        self.times_hit = 0
        self.strokes = 0
        self.last_hit_by = None

        #make this ball appear in a random location
        self.position=self.game.course.random_position_on_course()
          
    def check_if_ball_scored(self):
        if self.game.object_shares_tile_with(self, Hole):
            # Score!
            logger.debug("Score!")
            if self.last_hit_by is not None:
                scoring_player = self.last_hit_by
                self.game.send_message(f"**{scoring_player.get_display_name()} scores 🎊! {utils.score_name(self.strokes,self.game.par)}!**")
            else:
                scoring_player = get_NPC_dummy_player("The Ball")
                self.game.send_message(f"**The ball scores itself 🎊! {utils.score_name(self.strokes,self.game.par)}!**")

            self.game.increase_score(scoring_player, added_balls_scored=1, added_scored_strokes=self.strokes)
            self.game.on_score(scoring_player, self, self.position)

            self.game.add_object(ScoreConfetti(self.game, self.position))
            self.reset_at_random_point()

    def hit(self, vector, player_to_take_credit=None):
        self.position += vector
        self.times_hit += 1
        self.strokes += 1
        self.last_hit_by = player_to_take_credit
        self.check_if_ball_scored()
        # todo: model bouncing, rolling, gravity, sand traps, etc


class Hole(Entity):
    displayEmoji = "⛳"
    type = "hole"
    showOnBoard = True
    def __init__(self, game, position = [0,0]):
        self.position = Vector(position)
        self.game = game
