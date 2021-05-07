import math
import random
import numpy as np

def copyvec(vec):
    return np.copy(vec)

def lerp(start,finish,t):
    return start*(1-t) + finish*t

def tile_coordinates(position):
    return [int(position[0]), int(position[1])] #if our position is 5.6,5.2, return [5,5]

def choose_direction_emoji(velocityVector):
    angle = math.atan2(velocityVector[1],velocityVector[0])
    emojis = ['➡️','↘️','⬇️','↙️','⬅️','↖️','⬆️','↗️']
    fraction_of_full_revolution = angle/(2*math.pi) % 1 #an angle of 0 means pointing right
    emoji_number = round(fraction_of_full_revolution * 8) % 8
    return emojis[emoji_number]



def random_weighted_choice(options, weights=None):
    # like random.choice(options), but each choice has a different chance of being selected
    # so random_weighted_choice(['a','b','c'],[1,1,2]) has a 2/(1+1+2) = 50% chance of choosing 'c', and a 25% chance of choosing 'a' or 'b'.
    return random.choices(options, weights=weights)[0]

def glolfify(name):
    #turn "golf" into "glolf"
    # could be used in a modification called Take The L
    vowels = 'aeiou'
    index = min([name.index(v) for v in vowels if v in name])
    return name[0:index] + 'l' + name[index:]


def score_name(strokes,par):
    if strokes == 1:
        return "Hole in one"

    if strokes-par == -4:
        return "Condor"
    elif strokes-par == -3:
        return "Albatross"
    elif strokes-par == -2:
        return "Eagle"
    elif strokes-par == -1:
        return "Birdie"
    elif strokes-par == 0:
        return "Par"
    if strokes-par == 1:
        return "Bogey"
    elif strokes-par == 2:
        return "Double bogey"
    elif strokes-par == 3:
        return "Triple bogey"
    else:
        return str(strokes-par) + " over par"
