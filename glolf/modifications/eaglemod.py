import random

import utils
from .modification import PlayerModification, GameModification
import entities

class EagleMaker(GameModification):
    def on_score(self, scoring_player, ball, score_position):
        score_name = utils.score_name(ball.strokes,self.game.par) 
        if score_name == "Eagle":
            self.game.send_message("The eagle swoops onto the course!")
            self.game.add_object(entities.FlyingEagle(self.game, triggering_player=scoring_player)) 
        elif score_name == "Albatross":
            self.game.send_message("The albatross swoops onto the course!")
            self.game.add_object(entities.FlyingAlbatross(self.game, triggering_player=scoring_player))

class GrabbedByEagle(PlayerModification):
    displayEmoji = "🦅"
    isDead = False
    type = "temporary"
    def __init__(self, game):
        self.game = game

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        current_glolfer_action["action"] = "nothing you're grabbed lol"


class AlbatrossAroundNeck(PlayerModification):
    displayEmoji = "🦢"
    isDead = False
    type = "temporary"

    def __init__(self, game, attached_player):
        self.game = game
        self.player = attached_player
        # reduce speed
        old_nyoomability = self.player.stlats.nyoomability
        self.player.stlats._replace(nyoomability= old_nyoomability-0.5)

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        if random.random() < 0.33:
            current_glolfer_action["action"] = "nothing you're grabbed lol"
            self.game.send_message(f"{self.player.get_display_name()} pets the albatross around their neck!")

        elif random.random() < 0.25:
            # todo: remove modification from player
            self.isDead = True
            self.game.send_message(f"The albatross lets go of {self.player.get_display_name()} and flies away!") 

            # bring speed back to normal
            # need to do it this way because namedtuples are immutable
            old_nyoomability = self.player.stlats.nyoomability
            self.player.stlats._replace(nyoomability= old_nyoomability+0.5)

