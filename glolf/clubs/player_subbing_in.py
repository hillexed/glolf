import entities
import numpy as np

from utils import random_seeded_choice
from modifications.modification import GameModification, PlayerModification
import random


class NeedsToTagIn(PlayerModification):
    # will move towards the target 
    # display_in_mod_list = False
    displayEmoji = "move"
    def __init__(self, target_cart):
        self.target_cart = target_cart

    def on_glolfer_update(self, glolfer, current_action):
        current_action["action"] = "move"
        # ensure they cannot hit the ball

    def on_glolfer_move(self, glolfer, target):
        return self.target_cart


class SubInNextPlayerOnceSomeoneScoresInAClubGame(GameModification):
    def __init__(self, game):
        self.game = game

    def on_score(self, scoring_player, ball, hole_position):
        scoring_club = scoring_player.club
        if scoring_club is not None:
            
            next_player = scoring_club.get_next_glolfer(scoring_player)

            cart = GlolferInGlolfCartSubbingIn(self.game, 
                subbing_in_player=next_player,
                subbing_out_player=scoring_player)
            self.game.add_object(cart)

            scoring_player.modifiers.append(NeedsToTagIn(cart))


class GlolferInGlolfCartSubbingIn(entities.Entity):
    type = "cart"
    displayEmoji = "🛺" # will be overwritten
    zIndex = 11
    def __init__(self, game, subbing_in_player, subbing_out_player, position=[0,0]):
        self.game = game
        self.currently_driving_player = subbing_in_player
        self.target = subbing_out_player

        if random.random() < 0.5:
            # can't come from the right wall because the emoji always faces left and it looks better this way
            #if random.random() < 0.5:
            #    position = [0,random.randint(self.game.course.bounds[0],self.game.course.bounds[1])] # right wall
            #else:
            position = [0,random.randint(0,self.game.course.bounds[1])] # left wall
        else:
            if random.random() < 0.5:
                position = [random.randint(0,self.game.course.bounds[0]), 0] # top wall
            else:
                position = [random.randint(0,self.game.course.bounds[0]), self.game.course.bounds[1]] # bottom wall

        self.position = np.array(position).astype(float)

        self.has_subbed_in = False

        self.movement_speed = self.currently_driving_player.stlats.nyoomability

        self.game.send_message(f"{self.displayEmoji}  {self.currently_driving_player.get_display_name()} drives onto the course to tag in!")

    def update(self):
        if self.game.on_same_tile(self, self.target):
            if not self.has_subbed_in:
                self.sub_in() # reached our target, sub in
            else:
                self.isDead = True # we've driven off the field, delete ourselves
            return
        
        otherplayer = self.game.get_closest_object(self, entities.Glolfer) #head to whatever's closest
        if self.game.on_same_tile(self, self.target) and otherplayer != target:
            self.game.send_message(f"🛺 {self.currently_driving_player.get_display_name()} rams {otherplayer.get_display_name()}!")

    def move_somewhere(self):
        '''
        If this glolfer has decided to move, choose what direction to move in.
        Todo: imagine if this took terrain into account, and slowed you down on sand or used A* pathfinding
        ''' 
        target = self.target

        target_vec = target.position - self.position #todo: pathfinding

        if np.linalg.norm(target_vec) < 0.01:
            return #we're on the target, don't move or we might divide by 0

        # create a vector in the direction of the target that's `move_speed` long
        move_speed = self.stlats.nyoomability
        move_speed = min(move_speed, np.linalg.norm(target_vec)) #don't overshoot the target
        move_vector = target_vec / np.linalg.norm(target_vec) * move_speed

        # here's where various different type of movements would go

        self.attempt_move(move_vector)

    def sub_in(self):
        # add self.cur player to game
        subbing_in = self.currently_driving_player
        subbing_out = self.target

        emerging_verb = random_seeded_choice([
            "jumps out","jumps out","slithers out","hops out","hops out",
            "jumps out","jumps out","slithers out","hops out","hops out",
            "slides out","slides out","scurries out","scurries out",
            "slides out","slides out","scurries out","scurries out",
            "tumbles out","oozes out", "steps out","backflips out","wheels out","crawls out","climbs out","glides out","roams out","saunters out","dashes out", "charges out","staggers out","totters out","trudges out","strides out","strides out"],subbing_in.name)

        self.game.send_message(f"{subbing_in.get_display_name()} {emerging_verb} of the glolf cart! {subbing_out.get_display_name()} hands the club off to them and gets in!")
        self.has_subbed_in = True

        subbing_in.set_position(self.position)
        self.game.add_object(subbing_in)
        self.game.remove_object(subbing_out)
        self.currently_driving_player = subbing_out

        # player no longer needs to tag in
        for mod in subbing_out.modifiers[:]:
            if type(mod) == NeedsToTagIn:
                subbing_out.modifiers.remove(mod)

        self.target = entities.Entity(self.game, position=[-5,-5]) # drive towards dummy target
