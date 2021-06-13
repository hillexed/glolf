import entities

class GlolferInGlolfCartSubbingIn(entities.Entity):
    type = "cart"
    displayEmoji = "🛺" # will be overwritten
    zIndex = 11
    def __init__(self, subbing_in_player, subbing_out_player):
        self.currently_driving_player = subbing_in_player
        self.target = subbing_out_player

        self.has_subbed_in = False

        self.movement_speed = self.currently_driving_player.stlats.nyoomability

    def update(self):
        if self.game.on_same_tile(self, self.target):
            self.sub_in()
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
        subbing_into_game = self.currently_driving_player
        subbing_out = self.target
        self.game.send_message(f"{self.target.get_display_name()} hands the club off to {self.currently_driving_player.get_display_name()}!")
        self.has_subbed_in = True

        self.game.add_object(
            Glolfer(subbing_into_game.name, position=self.position)
        )

        self.currently_driving_player = subbing_out
        subbing_out.isDead = True
        self.target = [-5,-5]
