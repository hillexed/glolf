import collections, random, math
import numpy as np

class Entity():
    displayEmoji = "❓"
    showOnBoard = True
    isDead = False
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
    def __init__(self, game, position = [0.0,0.0]):
        self.position = np.array(position).astype(float)
        self.game = game
        self.times_hit = 0
        self.strokes = 0
        self.last_hit_by = "Nobody"
        self.displayEmoji = random.choice(("⚪","🔴","⚽","🟣","🟢","🟤","🟡","🔵","🟠"))

    

    def update(self):
        self.check_if_ball_scored()
          
    def check_if_ball_scored(self):
        flag = self.game.get_closest_object(self, Hole)
        if self.game.on_same_tile(flag, self):
            # Score!
            print("Score!")

            self.game.send_message(f"{self.last_hit_by} scores! {self.game.score_name(self.strokes,self.game.par)}!")
            self.times_hit = 0
            self.strokes = 0
            self.last_hit_by = "Nobody"
            self.position=[random.randrange(1,9),random.randrange(1,9)]

    def hit(self, vector, player_to_take_credit=None):
        self.position += vector
        self.times_hit += 1
        self.strokes += 1
        self.last_hit_by = player_to_take_credit.name
        self.check_if_ball_scored()
        # todo: model bouncing, rolling, gravity, sand traps, etc


class Hole(Entity):
    displayEmoji = "⛳"
    type = "hole"
    showOnBoard = False
    def __init__(self, game, id, position = [0,0]):
        self.position = np.array(position)
        self.game = game
        self.id = id



class HittingArrow(Entity):
    displayEmoji = "X"
    showOnBoard = True
    def __init__(self, game, position, velocityVec):
        self.position = np.array(position)
        self.game = game
        self.id = id
        self.isDead = False
        self.displayEmoji = self.choose_direction_emoji(velocityVec)

    def update(self):
        self.isDead = True
        

    def choose_direction_emoji(self, velocityVector):
        angle = math.atan2(velocityVector[1],velocityVector[0])
        emojis = ['➡️','↗️','⬆️','↖️','⬅️','↙️','⬇️','↘️']
        fraction_of_full_revolution = angle/(2*math.pi) % 1 #an angle of 0 means pointing right
        emoji_number = round(fraction_of_full_revolution * 8) % 8
        return emojis[emoji_number]



SwingType = collections.namedtuple("SwingType",[
    "name",
    "mean_power", # thwackability, the average number of squares this swing will send a ball
    "min_power", # the minimum number of squares this swing will send a ball
    "max_power", # the minimum number of squares this swing will send a ball
    "power_variance", # the variance in power from this swing
    "angle_variance", # angle variance, how much a swing's angle will differ from intended
])

SwingTypes = {
    "chip": SwingType(name="chip",mean_power=3,min_power=2,max_power=3,power_variance=1,angle_variance=0.1),
    "putt":SwingType(name="putt",mean_power=1,min_power=0,max_power=2,power_variance=0.3,angle_variance=0.04),
}
    

