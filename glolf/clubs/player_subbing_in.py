import entities
import numpy as np

from utils import random_seeded_choice, copyvec
from modifications.modification import GameModification, PlayerModification
from entities import GlolfCartExhaust, Entity
import random

class InGlolfCart(PlayerModification):
    type = "cart"
    displayEmoji = "🛺" # will be overwritten
    zIndex = 11
    def __init__(game=None):
        pass


class NeedsToTagOut(PlayerModification):
    # will move towards the target 
    display_in_mod_list = False
    displayEmoji = "must tag out"
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

            scoring_player.modifiers.append(NeedsToTagOut(cart))


class GlolferInGlolfCartSubbingIn(entities.Entity):
    type = "cart"
    displayEmoji = "🛺" # will be overwritten
    zIndex = 11
    def __init__(self, game, subbing_in_player, subbing_out_player, position=[0,0]):
        self.game = game
        self.currently_driving_player = subbing_in_player
        self.currently_driving_player.modifiers.append(InGlolfCart())
        self.target = subbing_out_player

        # appear at a random edge
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
                position = [random.randint(0,self.game.course.bounds[0]), self.game.course.bounds[1]-1] # bottom wall
        self.position = np.array(position).astype(float)

        self.has_subbed_in = False

        self.game.send_message(f"{self.displayEmoji} {self.currently_driving_player.get_display_name()}, the next member of the {self.currently_driving_player.club.name} drives onto the course to tag in!")

    def update(self):
        if self.game.on_same_tile(self, self.target):
            if not self.has_subbed_in:
                self.sub_in() # reached our target, sub in
            else:
                self.isDead = True # we've driven off the field, delete ourselves
                self.currently_driving_player.remove_modifiers_of_type(InGlolfCart)
            return

        self.move_somewhere()
        
        otherplayer = self.game.get_closest_object(self, entities.Glolfer) #head to whatever's closest
        if self.game.on_same_tile(self, self.target) and otherplayer != self.target:
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
        if not self.has_subbed_in:
            move_speed = self.currently_driving_player.stlats.ritualism + 2
        else:
            move_speed = self.currently_driving_player.stlats.ritualism + 3
            
        move_speed = min(move_speed, np.linalg.norm(target_vec)) #don't overshoot the target
        move_vector = target_vec / np.linalg.norm(target_vec) * move_speed

        # here's where various different type of movements would go


        self.old_position = copyvec(self.position)
        self.attempt_move(move_vector)
        self.draw_dust_trail(self.old_position, self.position)

    def check_if_anything_rammed(self, int_position):

        checklocation = entities.Entity(self.game, int_position + np.array([0.5,0.5]))

        otherplayer = self.game.get_closest_object(checklocation, entities.Glolfer)
        if self.game.on_same_tile(checklocation, self.target) and otherplayer != self.target:
            
            self.game.send_message(f"**🛺 {self.currently_driving_player.get_display_name()} rams {otherplayer.get_display_name()}!**", True)
            otherplayer.displayEmoji = '🐏'

    def draw_dust_trail(self, start, finish):
        # Bresenham's line drawing algorithm, taken from wikipedia
        x0,y0 = start
        x1,y1 = finish

        x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)

        dx =  abs(x1-x0)
        xstep = -1
        if x0<x1:
            xstep = 1
        dy = -abs(y1-y0)
        ystep = -1
        if y0<y1:
            ystep = 1
        err = dx+dy
        while x0 != x1 or y0 != y1:
            self.game.add_object(GlolfCartExhaust(self.game, [x0,y0]))
            self.check_if_anything_rammed([x0,y0])
            twoerror = 2*err
            if (twoerror >= dy):
                err += dy
                x0 += xstep
            if (twoerror <= dx):
                err += dx
                y0 += ystep

            if abs(x0) > 500 or abs(y0) > 500:
                raise ValueError(start, finish, x0,y0,x1,y1)

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

        subbing_in.set_position(self.position + [0,1])
        subbing_in.remove_modifiers_of_type(InGlolfCart)
        self.game.add_object(subbing_in)

        self.game.remove_object(subbing_out)
        self.currently_driving_player = subbing_out
        self.currently_driving_player.modifiers += [InGlolfCart()]
        subbing_out.remove_modifiers_of_type(NeedsToTagOut)

        self.target = entities.Entity(self.game, position=[-5,-5]) # drive towards dummy target
