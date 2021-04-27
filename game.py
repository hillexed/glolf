from typing import TypedDict
import glolfer
import numpy as np
import copy
import random
import glolfcourses
from players import default_player_names

class SingleHoleScoresheet:
    def __init__(self, player):
        self.player = player
        self.scored_strokes = 0
        self.total_strokes = 0
        self.balls_scored = 0

class SingleHole:
    def __init__(self, debug=False, glolfer_names=[]):
        self.debug = debug

        self.objects = []
        self.scores = {} #glolfer : SingleHoleScore(glolfer)

        # parse course
        self.course = self.parse_course(glolfcourses.get_random_course())
        self.par=3

        # place one glolfer on each hole
        random_position = lambda: [random.random()*self.course_bounds[0], random.random()*self.course_bounds[1]]

        # place three balls
        self.objects.append(glolfer.Ball(self, position=random_position()))
        self.objects.append(glolfer.Ball(self, position=random_position()))
        self.objects.append(glolfer.Ball(self, position=random_position()))

        if len(glolfer_names) == 0:
            glolfer_names.append(random.choice(default_player_names))
            glolfer_names.append(random.choice(default_player_names))     

        # place one glolfer at each hole, in order, then any more are random
        placed_glolfers = 0
        flags = [obj for obj in self.objects if type(obj) == glolfer.Hole]

        for name in glolfer_names:
            if placed_glolfers < len(flags):
                # place glolfer #1 on flag #1, glolfer #2 on flag #2, etc
                new_glolfer_pos = flags[placed_glolfers].position
                placed_glolfers += 1
            else:
                # Out of flags, throw em anywhere
                new_glolfer_pos = random_position()            
            newglolfer = glolfer.Glolfer(self, position=new_glolfer_pos)
            self.objects.append(newglolfer)
            self.scores[newglolfer] = SingleHoleScoresheet(newglolfer)

        self.message_queue = []
        self.new_objects = []
        

    def parse_course(self, course_string):
        lines = course_string.strip().split("\n")
        lines = [[c for c in line.strip() if c != '\ufe0f'] for line in lines]

        # remove unicode \ufe0f, variation selector, so it doesn't mess up the grid

        # turn this y,x array into an x,y array

        self.num_holes = 0

        course = [[] for line in lines]
        for y, line in enumerate(lines):
            #print((repr(y),line))
            for x,terrain in enumerate(line):
                if x == len(course):
                    course.append([])
                course[x].append(terrain)
                if terrain == "⛳":
                    self.objects.append(glolfer.Hole(self, id=self.num_holes,position=[x,y]))     
                    self.num_holes += 1  

        self.course = course
        self.course_bounds = [len(self.course),len(self.course[0])]
        return course

    def update(self):
        # one turn
        for obj in self.objects:
            obj.update()

        # add any new objects
        self.objects += self.new_objects
        self.new_objects = []

        self.objects = [x for x in filter(lambda obj:not obj.isDead, self.objects)]

        # todo: count scoring

    def add_object(self, obj):
        # add an object to the game, guaranteeing it won't have update() called on it until next turn
        self.new_objects.append(obj)


    def printboard(self):
        string = ""

        # any status update messages
        for line in self.message_queue:
            string += line + '\n'
        self.message_queue = []

        # print the board and return a string
        course = copy.deepcopy(self.course)
        for obj in self.objects:
            if not obj.showOnBoard:
                continue
            tile = obj.tile_coordinates()
            if 0 <= tile[0] < len(course) and 0 <= tile[1] < len(course[tile[0]]):
                course[tile[0]][tile[1]] = obj.displayEmoji

        # board is stored internally as [x][y] but to print it we need to flip that and go [y][x]
        for y in range(self.course_bounds[1]):
            for x in range(self.course_bounds[0]):
                if x < len(course) and y < len(course[x]):
                    string += "".join(course[x][y])   
            string += '\n'     

        string += self.print_score()
        return string

    def compute_winner(self):
        '''
            The winner is the player who scored the most holes! Otherwise, lowest strokes wins
        '''
        winner = None
        for player in self.scores:
            if winner is None:
                winner = player
                continue
            if self.scores[player].balls_scored > self.scores[winner].balls_scored:
                winner = player
            elif self.scores[player].balls_scored == self.scores[winner].balls_scored:
                if self.scores[player].total_strokes < self.scores[winner].total_strokes:
                    winner = player
        return winner

    def compute_winner_name(self):
        winner = self.compute_winner()
        if winner is not None:
            return winner.name
        return "Everybody"
            

    def print_score(self):
        string = ""
        for player in self.scores:
            scorecard = self.scores[player]
            string += f"{scorecard.player.displayEmoji} {scorecard.player.name}: {scorecard.balls_scored} holes, {scorecard.total_strokes} strokes \n"

        return string


    def get_closest_object_to_position(self, position, object_type=None):
        consideredobjects = self.objects
        if object_type is not None:
             consideredobjects = [o for o in self.objects if (type(o) == object_type)]

        objectsSortedByDistance = sorted(consideredobjects, key=lambda object:np.linalg.norm(object.position-position))
        return objectsSortedByDistance[0]

    def get_closest_objects(self, target, object_type=None):
        consideredobjects = self.objects
        if object_type is not None:
             consideredobjects = [o for o in self.objects if (type(o) == object_type and o != target)]

        objectsSortedByDistance = sorted(consideredobjects, key=lambda object:np.linalg.norm(object.position-target.position))
        return objectsSortedByDistance

    def get_closest_object(self, target : glolfer.Entity, object_type=None):
        objects = self.get_closest_objects(target, object_type)
        if len(objects) > 0:
            return objects[0]
        else:
            return None

    def on_same_tile(self, obj1,obj2):

        c1 = obj1.tile_coordinates()
        c2 = obj2.tile_coordinates()

        if c1[0] == c2[0] and c1[1] == c2[1]:
            return True
        return False

    def has_ball_on_tile(tile_coordinates):
        ball = get_closest_object_to_position(tile_coordinates + np.array([0.5,0.5]), glolfer.Ball)
        if ball is None:
            return False

        ballcoords = ball.tile_coordinates()

        if ballcoords[0] == tile_coordinates[0] and ballcoords[1] == tile_coordinates[1]:
            return True
        return False

    def send_message(self, message):
        self.message_queue.append(message)

    def report_hit(self,shooting_player, ball,swing,club,shot_vec):
        length = "short"
        if np.linalg.norm(shot_vec) > 2:
            length = "medium"
        if np.linalg.norm(shot_vec) > 3:
            length = "long"
        if np.linalg.norm(shot_vec) > 6:
            length = "really long"

        message = f"{shooting_player.name} {shooting_player.displayEmoji} hits a {length} {swing.name}!"
        if self.debug:
            message += f"{shot_vec}"
        print(message)

        self.scores[shooting_player].total_strokes += 1

        self.message_queue.append(message)


    def score_name(self, strokes,par):
        if strokes == 1:
            return "hole in one"

        if strokes-par == -4:
            return "condor"
        elif strokes-par == -3:
            return "albatross"
        elif strokes-par == -2:
            return "eagle"
        elif strokes-par == -1:
            return "birdie"
        elif strokes-par == 0:
            return "par"
        if strokes-par == 1:
            return "bogey"
        elif strokes-par == 2:
            return "double bogey"
        elif strokes-par == 3:
            return "triple bogey"
        else:
            return str(strokes-par) + " over par"
