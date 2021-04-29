import numpy as np
import math
import random

import players
import utils

from entities import *

class Glolfer(Entity):
    type = "player"
    displayEmoji = "🏌️" # will be overwritten
    zIndex = 10 # show below players
    def __init__(self, game, position = [0,0], playername=None):
        self.game = game
        self.position = np.array(position).astype(float)

        if playername is None:
            self.name = random.choice(players.default_player_names)
        else:
            self.name = playername

        # get stlats
        self.player_data = players.get_player_from_name(self.name)
        self.displayEmoji = self.player_data.emoji
        self.stlats = self.player_data.stlats

        self.team = "Undefined Team"

    def get_display_name(self):
        return f"{self.name} {self.displayEmoji}"

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

        # create a vector in the direction of the target that's `move_speed` long
        move_speed = self.stlats.nyoomability
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
        min_speed = club["power_boost"] + swing.min_power + self.stlats.musclitude
        strength_variance = swing.power_variance / self.stlats.finesse
        attempted_shot_power = swing.mean_power

        # estimation stlat helps glolfers adjust their shot power slightly to match the distance to the hole
        estimationFactor = min(self.stlats.estimation * 0.2,1)
        attempted_shot_power = utils.lerp(swing.mean_power, target_distance, estimationFactor)

        whack_strength = np.random.normal(attempted_shot_power,strength_variance)
        whack_strength = max(0, whack_strength) #can't have negative power

        # ok take a swing!
        # todo: compute topspin and backspin and stuff
        shot_speed = np.random.normal(whack_strength,strength_variance)
        shot_speed = max(shot_speed, min_speed)
        # max power isn't actually capped because shots overshooting is funny

        # shot angle
        target_angle -= self.stlats.left_handedness
        angle_variance = swing.angle_variance*self.stlats.needlethreadableness
        angle_variance = max(0, angle_variance) 
        shot_angle = np.random.normal(target_angle, angle_variance)   
        
        shot_direction = np.array([math.cos(shot_angle), math.sin(shot_angle)])
        shot_vec = shot_direction * shot_speed

        # to do: wind and weather

        if ball.last_hit_by is not None and ball.last_hit_by != self:            
            self.game.send_message(f"{self.get_display_name()} Possesses {ball.last_hit_by.get_display_name()}'s ball {ball.displayEmoji}!")


        self.game.report_hit(self, ball,swing,club,shot_vec) 
        ball.hit(shot_vec,player_to_take_credit=self)
        self.game.add_object(HittingArrow(self.game, self.position, shot_vec)) #show where you hit

        if shot_speed > 20:
            # REALLY LONG SHOT ALERT
            self.game.send_message(f"💥 {self.get_display_name()}'s stroke tears a crack in spacetime! The ball disintegrates! 3-stroke penalty! 💥!")
            for i in range(25):
                self.game.add_object(RealityCrack(self.game, self.game.course.random_position_on_course())) #show where you hit
            self.game.scores[self].total_strokes += 3
            ball.reset_at_random_point()

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
