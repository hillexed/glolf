class Modification:
    def __init__(self, game):
        self.game = game

    def on_glolfer_move(self, glolfer, target): #return a new target to move towards if needed
        return None # don't change the target

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        # called every glolfer.update()
        pass

    def on_hit(self, shooting_player, ball, swing, club, shot_vec):
        pass

    def on_score(self, scoring_player, ball, score_position):
        pass

class GameModification(Modification):
    def update(self):
        # called once every turn, after everything else has updated
        pass
    

class PlayerModification(Modification):
    displayEmoji = "?"
    type = "permanent"
    isDead = False
    display_in_mod_list = True
    def __init__(self, game, attached_player):
        self.game = game
        self.player = attached_player
