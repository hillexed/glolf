from typing import NamedTuple
import random
import re
from math import floor


from data import course_data
import entities

def get_random_course(game):
    return Course(game, course_data.get_random_course())

VEHICLES = ("🚗","🚙","🚕","🚌","🚚","🚙")

# 🌌🟩 = normal

FLOWERS=("🌹","🌷")
ANIMALS=("🦆","🐟") # the salmon swim upstream! Inning -1 begins!

FOLIAGE_TILES = ("🌲","🌳","🌲","🌵")
TRAP_BALLS = ("🟨","🕸️", "🌵")

WATER_TILES = ("🟦","🌊")
FIRE_TILES = ("🔥","🟧")


HARD_TO_HIT_OUT_OF_TILES = TRAP_BALLS + WATER_TILES # 50% chance of not getting it out
SLOW_PLAYERS = TRAP_BALLS + FOLIAGE_TILES
VEHICLES_CANT_PASS_THROUGH = WATER_TILES + FIRE_TILES + ("🟨","⭐", "🌎","🏢","🌕")

def cost_of_moving_through_tile(tiletype, is_vehicle=False):
    cost = 1
    if is_vehicle:
        if tiletype in VEHICLES_CANT_PASS_THROUGH:
            cost = 50
    else: # isnt a vehicle
        if tiletype in SLOW_PLAYERS:
            cost = 1.5
    return cost

class TerrainModifier:
    def before_swing():
        pass
    def after_hit(result):
        pass


class HardToHitOutTerrain(TerrainModifier):
    def __init__(self, failpercent, message):
        self.failpercent = failpercent
        self.message = message

    def before_swing(): #does nothing right now
        pass
    def after_hit(result): #does nothing right now
        if math.random() < self.failpercent:
            result.clear()
            result.message = self.message.format(result.player)


terrainTypes = {
    "🟦": HardToHitOutTerrain(0.3, "The water churns. {} can't hit it out! "),
    "🌊": HardToHitOutTerrain(0.3, "The wave catches the ball! {} can't hit it out!"),
    "🟨": HardToHitOutTerrain(0.3, "The sand grabs the ball! {} can't hit it out! "),
    "🕸️": HardToHitOutTerrain(0.3, "{} is stuck in the web! ")
}

emoji_to_leave_together = [ # emoji which display as one character on discord
'1️⃣'
]
# todo: leave these together

def split_counting_discord_emoji(line): # unused for now
    # parse "abc:one:" into ['a','b','c',':one']
    if line.count(":") % 2 == 1:
        raise ValueError("unmatched : for emoji!")
    index = 0
    arr = []
    while index < len(line):
        newchar = line[index]
        if newchar == ":":
            # emoji detected
            endindex = line.find(":",index+1)
            if endindex == -1:
                raise ValueError              
            arr.append(line[index:endindex+1])
            index = endindex+1
        else:              
            arr.append(line[index])
            index += 1
    return arr


class Course:
    terrain = [[]]
    bounds = [0,0]
    course_objects = []

    def __init__(self, game, course_string):
        self.course_objects = []
        self.terrain = [[]]
        self.bounds = [0,0]
        self.game = game
        self.parse_course_string(course_string)

    def random_position_on_course(self):
        return [random.random()*(self.bounds[0]-0.6), random.random()*(self.bounds[1]-0.6)]

    def is_on_course(self, position):
        if 0 < position[0] and position[0] < len(self.terrain):
            if 0 < position[1] and position[1] < len(self.terrain[floor(position[0])]):
                return True
        return False
        

    def get_tile_at(self, position):
        if self.is_on_course(position): 
            return self.terrain[floor(position[0])][floor(position[1])]

    def parse_course_string(self, course_string):
        lines = course_string.strip().split("\n")
        lines = [[c for c in line.strip() if c != '\ufe0f'] for line in lines]

        # turn this y,x array into an x,y array
        self.num_holes = 0

        terrain = [[] for line in lines]
        for y, line in enumerate(lines):
            for x,tileEmoji in enumerate(line):
                if x == len(terrain):
                    terrain.append([])

                centerOfTile = [x+0.5,y+0.5]
                if tileEmoji == "⛳":
                    self.course_objects.append(entities.Hole(self.game,position=centerOfTile))     
                    self.num_holes += 1  
                    tileEmoji = "🟩"
                if tileEmoji == "💥":
                    self.course_objects.append(entities.RealityCrack(self.game,position=centerOfTile,life=999))
                    tileEmoji = "⬛"
                terrain[x].append(tileEmoji)

        self.terrain = terrain
        self.bounds = [len(self.terrain),len(self.terrain[0])]

    def get_objects(self):
        return self.course_objects
