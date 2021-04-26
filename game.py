from typing import TypedDict
import glolfer
import numpy as np
import copy

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
        self.objects.append(glolfer.Glolfer(self, position=[1,6]))
        self.objects.append(glolfer.Glolfer(self, position=[9,6]))
        

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
            
            if type(obj) == glolfer.Ball:
                flag = self.get_closest_object(obj, glolfer.Hole)
                if self.on_same_tile(flag, obj):
                    # Score!
                    print("Score!")
                    # todo: actually do something, like count par
                #winning team = glolfball.last_hit_by.team
                #winning team += glolfball.score
        #if no glolf balls left:
        #    hole over    

    def printboard(self):
        course = copy.deepcopy(self.course[:])
        for obj in self.objects:
            if not obj.showOnBoard:
                continue
            tile = obj.tile_coordinates()
            if 0 <= tile[0] < len(course) and 0 <= tile[1] <= len(course[0]):
                course[tile[0]][tile[1]] = obj.displayEmoji

        string = ""
        for line in course:
            string += "".join(line)   
            string += '\n'     

        #for obj in self.objects:
        #    string += f"{obj.type} {obj.position}," #debug output
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

    def report_hit(self,ball,shot,club,shot_vec):
        print("The ball is hit! {} {} {} {}".format(ball,shot,club,shot_vec))
