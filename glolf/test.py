import game
glolfgame = game.SingleHole()
glolfgame.send_message = print

def testgame():
    i = 0
    while not glolfgame.over:
        print(glolfgame.printboard())
        print(glolfgame.update())
        i += 1
        if i > 1000:
            raise ValueError("Game went on too long!")

for i in range(50):
    testgame()
