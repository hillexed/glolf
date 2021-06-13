class Modification:
    def __init__(self, game):
        self.game = game

    def on_glolfer_move(self, glolfer, target): #return a new target to move towards if needed
        return None # don't change the target

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        pass

    def on_hit(self, shooting_player, ball, swing, club, shot_vec):
        pass

    def on_score(self, scoring_player, ball, score_position):
        pass

    def update(self):
        pass
