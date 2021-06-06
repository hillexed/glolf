import numpy as np
import random, math
import logging
logger = logging.getLogger(__name__)


from .entity import Entity
from .glolfer import Glolfer
from modifications import eaglemod
import utils


class FlyingEagle(Entity):
    displayEmoji = "🦅"
    showOnBoard = True
    type = "eagle"
    zIndex = 12
    def __init__(self, game, triggering_player):
        self.game = game
        self.target = self.choose_target(triggering_player)

        # all the way at the right side of the screen, at a random y
        position = [self.game.course.bounds[0]-1, random.randint(0,self.game.course.bounds[1])]

        self.position = np.array(position).astype(float)

        self.grabbed_thing = None

        self.swooped = False
        

    def choose_target(self, triggering_player):
        player_in_lead = self.game.compute_winner()
        if player_in_lead is not None:
            return player_in_lead
        else:
            # game's tied
            return triggering_player

    def update(self):

        if self.position[0] < 0 or self.position[1] < 0:
            self.isDead = True
            self.release_grabbed_thing() # todo: consequences
            return

        if self.grabbed_thing is None:
            self.position[0] -= 1 # fly left

            # fly up/down towards target
            if self.target.position[1] < self.position[1]-0.5:
                self.position[1] -= 1
            elif self.target.position[1] > self.position[1]+0.5:
                self.position[1] += 1

            if self.game.object_shares_tile_with(self, Glolfer):
                # hit!
                grabbed_glolfer = self.game.get_closest_object(self, Glolfer)

                self.attempt_to_grab(grabbed_glolfer)

            if not self.swooped and abs(self.target.position[0] - self.position[0]) < 0.5:
                self.grab_but_theyre_far_away()

        else:
            # we've grabbed someone
            self.grabbed_thing.position = self.position
            self.position[1] -= 1 # fly upwards

            self.see_if_grabbed_player_frees_themself()

    def see_if_grabbed_player_frees_themself():
        if random.random() < self.grabbed_thing.stlats.wiggle/3:

            release_message = random.choice( [
                f"{self.grabbed_thing.get_display_name()} breaks free of the eagle's grasp!",
                f"{self.grabbed_thing.get_display_name()} distracts the eagle long enough to escape!",
                f"{self.grabbed_thing.get_display_name()} convinces the eagle to run an errand instead!",
                f"The eagle lets go of {self.grabbed_thing.get_display_name()}!",
                f"{self.grabbed_thing.get_display_name()} befriends the eagle! The eagle flies {self.grabbed_thing.get_display_name()} back down to the course!",
                f"{self.grabbed_thing.get_display_name()} befriends the eagle! They land safely!",
            ])

            self.game.send_message(release_message)
            self.release_grabbed_thing()

    def grab_but_theyre_far_away()
        self.game.send_message("The eagle swoops! It comes up empty-clawed!")
        self.swooped = True

    def attempt_to_grab(self, glolfer)
        # don't grab an already grabbed player
        if not any([type(mod) == eaglemod.GrabbedByEagle for mod in grabbed_glolfer.modifiers]):
            self.grab_player(grabbed_glolfer)
            self.game.send_message(f"The eagle swoops! It grabs {self.grabbed_thing.get_display_name()}!")
            self.swooped = True

    def grab_player(self, player):
        self.grabbed_thing = player
        player.modifiers.append(eaglemod.GrabbedByEagle(self.game))

    def release_grabbed_thing(self):
        # removed grabbed modifier
        if self.grabbed_thing is not None:
            self.grabbed_thing.modifiers = [x for x in filter( lambda mod: type(mod) != eaglemod.GrabbedByEagle, self.grabbed_thing.modifiers)]
            self.grabbed_thing = None



class FlyingAlbatross(FlyingEagle):
    # flies onto the course and tries to grab a person
    # then hangs on their neck
    displayEmoji = "🦅"
    showOnBoard = True
    type = "albatross"

    bird_name = "albatross"

    def grab_but_theyre_far_away()
        self.game.send_message("The albatross swoops! It comes up empty-clawed!")
        self.swooped = True

    def attempt_to_grab(self, glolfer)
        # don't grab an already grabbed player
        if not any([type(mod) == eaglemod.GrabbedByEagle for mod in grabbed_glolfer.modifiers]):
            self.game.send_message(f"The albatross swoops! It hugs {self.grabbed_thing.get_display_name()}'s neck!")
            self.swooped = True
            self.grab_player(grabbed_glolfer)

    def grab_player(self, player):
        self.grabbed_thing = player
        player.modifiers.append(eaglemod.AlbatrossAroundNeck(self.game))
        self.isDead = True

todo: way for modifications to go away

