import random

import utils
from .modification import PlayerModification, GameModification
from entities import Entity
import random
from data.scorecards import NPCScorecardDummyEntity

class InterestingOffscreenThing(GameModification):

    def __init__(self, game):
        self.isDead = False
        self.game = game
    
        self.interdimensional_void = Entity(game, position=[int(game.course.bounds[0]/2),-2])
        self.interdimensional_void.displayEmoji = "🌀"
        

        self.game.add_object(self.interdimensional_void)

    def on_score(self, scoring_player, ball, score_position):
        #if not self.game.is_tournament: return
        if isinstance(scoring_player,NPCScorecardDummyEntity):
            return

        if self.game.get_player_scorecard(scoring_player).balls_scored == 1 and random.random() < 0.2:
            messages = ("{} takes Interest in something crackling...","{} takes Interest in something off the course...", "Something off-course catches {}'s eye...", "{} seems distracted by something Interesting...")
            self.game.send_message(random.choice(messages).format(scoring_player.name))
            scoring_player.modifiers.append(DistractedByFearsomeShiny(self.game, self.interdimensional_void))


class DistractedByFearsomeShiny(PlayerModification):
    displayEmoji = "👀"
    isDead = False
    type = "temporary"
    display_in_mod_list = False

    # force players to move towards the offscreen shiny, then say an ominous message

    def __init__(self, game, shiny):
        self.game = game
        self.shiny = shiny

    def on_glolfer_move(self, game, current_target):
        return self.shiny 

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        
        current_glolfer_action["action"] = "move"

        target_vec = self.shiny.position - glolfer.position
        if target_vec.norm() < 0.5:
            # reached shiny location
            self.isDead = True

            message = random.choice(("{} beheld something.", "{} beheld something.", "{} saw something big.","{} saw something big.", "{} is full of awe.", "{} trembled in fear.", "{} felt the flashes.", "{} saw something undescribable.", "{} stared into something fascinating.","{} doesn't know how to help.", "{} beheld something thunderous."))
            self.game.send_message(message.format(glolfer.name), True)
            if self in glolfer.modifiers:        
                glolfer.modifiers.remove(self)
