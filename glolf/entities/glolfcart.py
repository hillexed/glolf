import numpy as np
import random, math
import logging
logger = logging.getLogger(__name__)


from .entity import Entity
from .glolfer import Glolfer
#from modifications import eaglemod
import utils


class GlolfCart(Entity):
    displayEmoji = "🦅"
    showOnBoard = True
    type = "cart"
    zIndex = 12
    def __init__(self, game, position, driving_player=None):
        self.game = game

        self.position = np.array(position).astype(float)

        self.velocity = np.array([0,0])
        self.driver = driving_player
        self.passengers = []        

    def has_driver(self, triggering_player):
        return (self.driver is not None)

    def update(self):
        if not self.driver:
            return 
        self.driver.drivecart(self)
        '''
        target = choosetarget(driver) # choose to go offscreen if they're subbing out, choose to tag in their partner if they're subbing in
        acceleration = choose()
        self.velocity += acceleration / 5
        self.position += velocity

        # friction if driving in water?

        if self.shares_position_with_something(Glolfer):
            if the driver and the rammed player share the same club:
                get in
            else    
                ram(glolfer) 
        '''

    

