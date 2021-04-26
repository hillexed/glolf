from typing import TypedDict
import glolfer
import numpy as np
import copy
import random


class SingleHole:
    def __init__(self):
        self.objects = []

        self.course = self.parse_course('''
        🕸️🟩🟩🟩🟩🟩🟩🟩🟩🕸️🕸️
        🕸️🟩🟩🟩🟩🟩🟩🌻🌻🟩🕸️
        🟩🟩🟩🟩🟩🟩🟩🌻🌻🟩🟩
        🟩🟩🟩🟩🟩🟨🟩🟩🟩🟩🟩
        🟩🟩🟩🟩🟨🟨🟨🟩🟩🟩🟩
        🟩⛳🟩🟩🟨🟨🟨🟩🟩⛳🟩
        🟩🟩🟩🟩🟨🟨🟨🟩🟩🟩🟩
        🟩🟩🟩🟩🟩🟨🟩🟩🟩🟩🟩
        🟩🟩🌻🌻🟩🟩🟩🟩🟩🟩🟩
        🕸️🟩🌻🌻🟩🟩🟩🟩🟩🟩🕸️
        🕸️🕸️🟩🟩🟩🟩🟩🟩🟩🕸️🕸️
        ''')

        # place one glolfer on each hole
        self.objects.append(glolfer.Ball(self, position=[5,2]))
        self.objects.append(glolfer.Ball(self, position=[6,9]))
        self.objects.append(glolfer.Ball(self, position=[9,9]))
        self.objects.append(glolfer.Glolfer(self, position=[1,6]))
        self.objects.append(glolfer.Glolfer(self, position=[9,6]))

        self.debug = False

        self.par=3

        self.message_queue = []
        

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

        self.objects = [x for x in filter(lambda obj:not obj.isDead, self.objects)]

                    # todo: actually do something, like count par
                #winning team = glolfball.last_hit_by.team
                #winning team += glolfball.score


    def printboard(self):
        course = copy.deepcopy(self.course[:])
        for obj in self.objects:
            if not obj.showOnBoard:
                continue
            tile = obj.tile_coordinates()
            if 0 <= tile[0] < len(course) and 0 <= tile[1] <= len(course[0]):
                course[tile[0]][tile[1]] = obj.displayEmoji

        # board is stored internally as [x][y] but to print it we need to flip that and go [y][x]
        string = ""
        for y in range(self.course_bounds[1]):
            for x in range(self.course_bounds[0]):
              string += "".join(course[x][y])   
            string += '\n'     

        for line in self.message_queue:
            string += line + '\n'
        self.message_queue = []
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

        message = f"{shooting_player.name} hits a {length} {swing.name}!"
        if self.debug:
            message += "f{shot_vec}"
        print(message)

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
