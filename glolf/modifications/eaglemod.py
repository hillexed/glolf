import utils
from .modification import Modification

import entities

class EagleMaker(Modification):
    def on_score(self, scoring_player, ball, score_position):
        score_name = utils.score_name(ball.strokes,self.game.par) 
        if score_name == "Eagle":
            self.game.send_message("The eagle swoops onto the course!")
            self.game.add_object(entities.FlyingEagle(self.game, triggering_player=scoring_player)) 
        elif score_name == "Albatross":
            self.game.send_message("The albatross swoops onto the course!")
            self.game.add_object(entities.FlyingAlbatross(self.game, triggering_player=scoring_player))


class GrabbedByEagle:
    def __init__(self, game):
        self.game = game

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        current_glolfer_action["action"] = "nothing you're grabbed lol"


class AlbatrossAroundNeck:
    def __init__(self, game):
        self.game = game
        self.player.stlats.nyoomability -= 0.5

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        if random.random() < 0.33:
            current_glolfer_action["action"] = "nothing you're grabbed lol"
            game.send_message(f"{} pets the albatross around their neck!") 

    def update():
        if random.random() < 0.25:
            # todo: remove modification from player
            self.isDead = True
            game.send_message(f"The albatross lets go of {} and flies away!") 
            self.player.stlats.nyoomability += 0.5

