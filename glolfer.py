import numpy as np
import math
import random

from entities import *

class Glolfer(Entity):
    type = "player"
    def __init__(self, game, position = [0,0]):
        self.game = game
        self.position = np.array(position).astype(float)
        self.displayEmoji = "🏌️"
        self.name = random.choice(("Meteor Heartfelt","Razor Defrost","Jasper Groove","Thalia Soliloque","Benedict Dicetower","Bingo Polaroid","Pumpernickel Fan","Baby Bop","Tantalus Chewed","Freddie Missouri"))
        self.team = "Undefined Team"
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
        Decide what to do each turn!
        Currently the logic is "Move towards the nearest ball - or if you're on the same tile as a ball, hit that ball"
        '''
        ball = self.game.get_closest_object(self, Ball)
        if self.game.on_same_tile(self, ball):
            self.hit(ball)
        else: #attempt to move to ball
            self.move_somewhere()

    def move_somewhere(self):
        '''
        If this glolfer has decided to move, choose what direction to move in.
        Todo: imagine if this took terrain into account, and slowed you down on sand or used A* pathfinding
        ''' 
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
        '''
        Swing at a glolf ball and hit it! Right now they will always hit the blall.
        '''
        # aim directly at the closest hole
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

        # to do: wind and weather

        self.game.report_hit(self, ball,swing,club,shot_vec) 
        ball.hit(shot_vec,player_to_take_credit=self)
        self.game.objects.append(HittingArrow(self.game, self.position, shot_vec)) #show where you hit

    def choose_shot_target_tile():
        # ideally this would involve fancy A* pathfinding and avoiding hazards
        # right now it involves aiming directly at the flag instead.

        target = self.game.get_closest_object(self, Hole) #aim directly at the nearest flag
        return enemy_hole #todo: pathfind

    def choose_club(self):
        return {"power_boost":0,"angle_variance":0} #todo: implement clubs

    def choose_swing_type(self, target_vector):
        # currently very simple. swing types defined in entities.py
        
        if np.linalg.norm(target_vector) > 3:
            return SwingTypes["chip"]
        else:
            return SwingTypes["putt"]
        # drive, pitch, hook (curve), punch,flop
        # also need to add weather
        return putt
