import numpy as np
import math
import collections
import random

class Entity():
    displayEmoji = "❓"
    showOnBoard = True
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


    def hit(self, vector):
        self.position += vector
        self.times_hit += 1
        self.strokes += 1
        # todo: model bouncing, rolling, gravity, sand traps, etc


class Hole(Entity):
    displayEmoji = "⛳"
    type = "hole"
    showOnBoard = False
    def __init__(self, game, id, position = [0,0]):
        self.position = np.array(position)
        self.game = game
        self.id = id


SwingType = collections.namedtuple("SwingType",[
    "mean_power", # thwackability, the average number of squares this swing will send a ball
    "min_power", # the minimum number of squares this swing will send a ball
    "max_power", # the minimum number of squares this swing will send a ball
    "power_variance", # the variance in power from this swing
    "angle_variance", # angle variance, how much a swing's angle will differ from intended
])

class Glolfer(Entity):
    type = "player"
    def __init__(self, game, position = [0,0]):
        self.game = game
        self.position = np.array(position).astype(float)
        self.displayEmoji = "🏌️"
        self.team = "definedun Team"
        self.stlats = {
            "stance": random.choice(["Tricky ","Flashy ","Aggro ","Tanky ","Twitchy ","Powerful ","Wibble ","Wobble ","Reverse ","Feint ","Electric ","Spicy ","Pomegranate ","Explosive"]),
            "fav_tea":"Iced",
            "tofu":4,
            "wiggle":3,
            "nyoomability":1.5, # movement speed
            "aerodynamics":3,
            "musclitude":1.0, # how hard you hit the ball
            "finesse": 1.0, # how consistent your shots are hit with power
            "needlethreadableness":0.8, # how well you thread the needle (multiplier for how much angle variance your shots have)
            "left-handedness":np.random.normal(0,0.3) #how often shots are biased to the left or right of what you want
        }

    def update(self):
        '''
        if there's a ball close to you:
            move towards that ball
        if you're on a ball:
            self.hit_ball()
        if the ball's far away and there's a caddy:
            move towards your caddy
        '''
        ball = self.game.get_closest_object(self, Ball)
        if self.game.on_same_tile(self, ball):
            self.hit(ball)
        else: #attempt to move to ball
            self.move_somewhere()

    def move_somewhere(self):
            target = self.game.get_closest_object(self, Ball)
            if target is None:
                target = self.game.get_closest_object(self) #head to whatever's closest
            target_vec = target.position - self.position #todo: pathfinding

            move_speed = self.stlats["nyoomability"]
            move_speed = min(move_speed, np.linalg.norm(target_vec)) #don't overshoot the ball
            move_vector = target_vec / np.linalg.norm(target_vec) * move_speed

            # here's where various different type of movements would go

            self.attempt_move(move_vector)

    def hit(self, ball):
        target = self.game.get_closest_object(self, Hole)
        target_vector = (target.position - self.position)

        target_distance = np.linalg.norm(target_vector)
        target_angle = math.atan2(target_vector[1],target_vector[0])

        # choose your shot (todo)
        club = self.choose_club()
        swing = self.choose_swing_type(target_vector)

        #how far the shot goes
        min_speed = club["power_boost"] + swing.min_power + self.stlats["musclitude"]
        strength_variance = swing.power_variance / self.stlats["finesse"]
        attempted_shot_power = swing.mean_power
        whack_strength = np.random.normal(attempted_shot_power,strength_variance)
        whack_strength = max(0, whack_strength) #can't have negative power

        # ok take a swing!
        # todo: compute topspin and backspin and stuff
        shot_speed = np.random.normal(whack_strength,strength_variance)
        shot_speed = max(shot_speed, min_speed)
        # max power isn't actually capped because shots overshooting is funny


        # shot angle
        target_angle -= self.stlats["left-handedness"]
        angle_variance = swing.angle_variance*self.stlats["needlethreadableness"]
        angle_variance = max(0, angle_variance) 
        shot_angle = np.random.normal(target_angle, angle_variance)   
        
        shot_direction = np.array([math.cos(shot_angle), math.sin(shot_angle)])
        shot_vec = shot_direction * shot_speed
        print(shot_direction)

        # to do: wind and weather

        ball.hit(shot_vec)
        self.game.report_hit(ball,swing,club,shot_vec) 

    def choose_shot_target_tile():
        return enemy_hole #todo: pathfind

    def choose_club(self):
        return {"power_boost":0,"angle_variance":0} #todo: implement clubs

    def choose_swing_type(self, target_vector):
        
        putt = SwingType(mean_power=1,min_power=0,max_power=2,power_variance=0.5,angle_variance=0.04)
        chip = SwingType(mean_power=6,min_power=2,max_power=3,power_variance=2,angle_variance=0.1)
        if np.linalg.norm(target_vector) > 3:
            return chip
        else:
            return putt
        # drive, pitch, hook (curve), punch,flop
        # also need to add weather
        return putt
