import collections, random, math
import numpy as np
import utils

import logging
logger = logging.getLogger(__name__)

class Entity():
    displayEmoji = "❓"
    showOnBoard = True
    isDead = False
    zIndex = 0
    def __init__(self, game, position = [0.0,0.0]):
        self.position = np.array(position).astype(float)
        self.game = game

    def update(self):
        pass

    def tile_coordinates(self):
        return [int(self.position[0]), int(self.position[1])]

    def attempt_move(self, direction):
        self.position += direction

class Ball(Entity):
    displayEmoji = "⚪"
    showOnBoard = True
    type = "ball"
    zIndex = 1 
    def __init__(self, game, position = [0.0,0.0]):
        self.position = np.array(position).astype(float)
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
                self.game.send_message(f"**{self.last_hit_by.get_display_name()} scores 🎊! {utils.score_name(self.strokes,self.game.par)}!**")
                self.game.scores[self.last_hit_by].scored_strokes += self.strokes
                self.game.scores[self.last_hit_by].balls_scored += 1
            else:
                self.game.send_message(f"**The ball scores itself 🎊! {utils.score_name(self.strokes,self.game.par)}!**")

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
        self.position = np.array(position).astype(float)
        self.game = game


class OneTurnParticle(Entity):
    # displayEmoji = "🎊" # override this in a subclass
    showOnBoard = True
    isDead = False
    zIndex = 20
    def __init__(self, game, position):
        self.position = np.array(position).astype(float)
        self.game = game
        self.isDead = False

    def update(self):
        self.isDead = True

class HittingArrow(OneTurnParticle):
    def __init__(self, game, position, velocityVec):
        super().__init__(game, position)
        self.displayEmoji = utils.choose_direction_emoji(velocityVec)

class ScoreConfetti(OneTurnParticle):
    displayEmoji = "🎊"

class SwordfightIndicator(OneTurnParticle):
    displayEmoji = "⚔️"

class RealityCrack(Entity):
    displayEmoji = "💥"
    showOnBoard = True
    isDead = False
    def __init__(self, game, position, life=None):
        self.position = np.array(position).astype(float)
        self.game = game
        if life is None:
            self.life = random.randrange(5,10)
        else:
            self.life = life

        self.timeBeforeCanTeleport = 0 
        self.showOnBoard = True

    def update(self):
        self.life -= 1
        if self.life <= 0:
            self.isDead = True

        if self.timeBeforeCanTeleport > 0:
            self.timeBeforeCanTeleport -= 1
            self.showOnBoard = False
            return
        else:
            self.showOnBoard = True
    
        obj = self.game.get_closest_object(self)
        if obj is not None and self.game.on_same_tile(obj, self) and self is not obj and type(obj) != RealityCrack:
            # teleport that object to a different flicker tile
            otherflickers = self.game.get_closest_objects(self, RealityCrack)
            if len(otherflickers) > 0:
                otherflicker = random.choice(otherflickers)
                obj.position = utils.copyvec(otherflicker.position)
                otherflicker.timeBeforeCanTeleport = 3
                otherflicker.showOnBoard = False
                self.game.send_message(f"{obj.displayEmoji} falls through a crack in spacetime to somewhere else!")


SwingType = collections.namedtuple("SwingType",[
    "name",
    "mean_power", # thwackability, the average number of squares this swing will send a ball
    "min_power", # the minimum number of squares this swing will send a ball
    "max_power", # the minimum number of squares this swing will send a ball
    "power_variance", # the variance in power from this swing
    "angle_variance", # angle variance, how much a swing's angle will differ from intended
])

SwingTypes = {
    "drive": SwingType(name="drive",mean_power=6,min_power=2,max_power=7,power_variance=1,angle_variance=0.15),
    "chip": SwingType(name="chip",mean_power=3,min_power=2,max_power=3,power_variance=1,angle_variance=0.1),
    "putt":SwingType(name="putt",mean_power=1,min_power=0.5,max_power=2,power_variance=0.3,angle_variance=0.04),
}
    

