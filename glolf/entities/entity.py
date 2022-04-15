from utils.vecmath import Vector
class Entity():
    displayEmoji = "❓"
    showOnBoard = True
    isDead = False
    zIndex = 0
    def __init__(self, game, position = [0.0,0.0]):
        self.position = Vector(position)
        self.game = game

    def update(self):
        pass

    def tile_coordinates(self):
        return [int(self.position[0]), int(self.position[1])]

    def attempt_move(self, direction):
        self.position += direction
