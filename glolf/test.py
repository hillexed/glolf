import game
from clubs.clubgame import ClubGame
# glolfgame = game.SingleHole()
glolfgame = ClubGame(club_names=['a','b']) # won't work unless a and b are in the DB as created clubs
glolfgame.send_message = print

def testgame():
    i = 0
    while not glolfgame.over:
        print(f"####### Turn {i}:")
        print(glolfgame.printgamestate())
        glolfgame.update()
        i += 1
        if i > 1000:
            raise ValueError("Game went on too long!")

for i in range(50):
    testgame()
