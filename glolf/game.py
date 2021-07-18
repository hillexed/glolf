from typing import TypedDict
import numpy as np
import copy
import random
import logging
logger = logging.getLogger(__name__)

import utils
import entities
from data.players import default_player_names
from modifications.current_rules import get_permanent_modifiers
import courses

from data.scorecards import SingleHoleScoresheet, NPCScorecardDummyEntity



class SingleHole:
    def __init__(self, debug=False, glolfer_names=[], max_turns=60, is_tournament=False):
        self.debug = debug
        self.id = random.randrange(1,100000)

        self.objects = []
        self.scores = {} #glolfer : SingleHoleScore(glolfer)
        self.turn_number = 0
        self.max_turns = max_turns

        self.over = False
        self.custom_winner_name = None
        self.is_tournament = is_tournament

        self.wind = random.choice(("Ominous","Pheasant","Fruity","Monsoon","Trade","Purple","Tasteless","Mechanical","Electric","Four-dimensional","Exact","Differential","Manifold","Change","Aggressively Normal")) #purely decorative for now
        self.windDirection = np.random.random(2) # [blah,blah] 0-1 each coord

        # parse course
        self.course = courses.get_random_course(self)
        self.objects += self.course.get_objects()
        self.par=4

        self.modifiers = get_permanent_modifiers(self)

        # place three balls
        self.objects.append(entities.Ball(self, position=self.course.random_position_on_course()))
        self.objects.append(entities.Ball(self, position=self.course.random_position_on_course()))
        self.objects.append(entities.Ball(self, position=self.course.random_position_on_course()))

        self.setup_first_glolfers(glolfer_names)

        self.message_queue = []
        self.messages_to_report_in_summary = []
        self.new_objects = []

    def add_player_by_name(self, starting_position, playername):
        newglolfer = entities.Glolfer(self, position=starting_position, playername=playername)
        self.add_player(newglolfer)

    def add_scorecard_if_doesnt_exist(self, scoring_thing):
        if scoring_thing not in self.scores:
            self.scores[scoring_thing] = SingleHoleScoresheet(scoring_thing)

    def add_player(self, newglolfer):         
        self.objects.append(newglolfer)
        self.add_scorecard_if_doesnt_exist(newglolfer)

    def setup_first_glolfers(self, glolfer_names):
        if len(glolfer_names) == 0:
            logger.info(f"Game {self.id}: No glolfers, choosing random...")
            glolfer_names.append(random.choice(default_player_names))
            glolfer_names.append(random.choice(default_player_names))     

        # place one glolfer at each hole, in order, then any more are random
        placed_glolfers = 0
        flags = [obj for obj in self.objects if type(obj) == entities.Hole]

        for name in glolfer_names:
            if placed_glolfers < len(flags):
                # place glolfer #1 on flag #1, glolfer #2 on flag #2, etc
                new_glolfer_pos = flags[placed_glolfers].position
                placed_glolfers += 1
            else:
                # Out of flags, throw em anywhere
                new_glolfer_pos = self.course.random_position_on_course()         
            self.add_player_by_name(new_glolfer_pos, playername=name)

    def update(self):
        self.message_queue = []

        if self.over:
            return

        # one turn
        for obj in self.objects + self.modifiers:
            obj.update()

        self.windDirection += np.random.random(2) - np.array((0.5,0.5)) # random walk

        # add any new objects
        self.objects += self.new_objects
        self.new_objects = []

        self.objects = [x for x in filter(lambda obj:not obj.isDead, self.objects)]

        self.turn_number += 1
        if self.turn_number >= self.max_turns:
            self.end()
        # todo: count scoring

        delay_time = 2 + min(len(self.message_queue),6) # 2 seconds normally, 0.5 seconds per message, 10 seconds max
        return delay_time

    def add_object(self, obj):
        # add an object to the game, guaranteeing it won't have update() called on it until next turn
        self.new_objects.append(obj)

    def remove_object(self, obj):
        if obj not in self.objects:
            pass # todo: complain
        self.objects.remove(obj)

    def embed_gamestate(self, include_board=True, game_over=False):
        embed=discord.Embed(title="🏌️ Glolf! (alpha)", description="", color=0x50BC43)
        embed.add_field(name="Turn", value=str(self.turn_number), inline=True)
        embed.add_field(name="Wind", value=f"{self.wind} {utils.choose_direction_emoji(self.windDirection)}", inline=True)

        # any status update messages
        if len(self.message_queue) == 0:
            events = "None"
        else:
            events = ""
            for line in self.message_queue:
                events += line + '\n'
        self.message_queue = []
        embed.add_field(name="Events", value=events, inline=False)

        if include_board:
            embed.add_field(name="Course", value=self.printboard(), inline=False)

        if game_over:
            embed.add_field(name="Final Score", value=self.print_score(), inline=False)
        else:
            embed.add_field(name="Scorecard", value=self.print_score(), inline=False)
            

        if game_over:
            embed.add_field(name="Game over!", value=f"🎉 {self.compute_winner_name(include_NPC_scorecards=True)} wins! 🎉")

        embed.set_footer(text="Brought to you by Instigator Hillexed#8194.")
        return embed


    def printgamestate(self, include_board=True, header=None):
        string = ""

        string += "        🏌️** Glolf! (alpha)**🏌️"
        if header is not None:
            string += f" - {header}"
        string += "\n"

        if not self.over:
            string += f"**Turn** {self.turn_number}/{self.max_turns} - **Wind:** {self.wind} {utils.choose_direction_emoji(self.windDirection)} \n"
        else:
            string += f"**Turn** {self.turn_number} - **Wind:** {self.wind} - **Finished**\n"

        # any status update messages
        if include_board:
            if len(self.message_queue) == 0:
                events = ""
            else:
                events = ""
                for line in self.message_queue:
                    events += line + '\n'

            string += events + "\n"

        if self.over and len(self.messages_to_report_in_summary) > 0:
            events = "**Notable Events**:\n"
            for line in self.messages_to_report_in_summary:
                events += line + '\n'

            string += events + "\n"

        if include_board:
            string += "**Course:**\n"
            string += self.printboard()

        if self.over:
            string += "**Final Score:**\n"
            string += self.print_score()
        else:
            string += "**Scorecard:\n**"
            string += self.print_score()
            

        if self.over:
            string += f"Game over! 🎉 **{self.compute_winner_name(include_NPC_scorecards=True)}** wins! 🎉\n_ _"
        return string
        

    def printboard(self):
        # print the board and return a string
        course = copy.deepcopy(self.course.terrain)
        zBuffer = {}
        string = ""
        for obj in self.objects:
            if not obj.showOnBoard:
                continue
            tile = obj.tile_coordinates()
            tile_tuple = (tile[0],tile[1])
            if 0 <= tile[0] < len(course) and 0 <= tile[1] < len(course[tile[0]]):
                if tile_tuple in zBuffer and obj.zIndex < zBuffer[tile_tuple]:  
                    continue
                zBuffer[(tile[0],tile[1])] = obj.zIndex
                course[tile[0]][tile[1]] = obj.displayEmoji

        # board is stored internally as [x][y] but to print it we need to flip that and go [y][x]
        for y in range(self.course.bounds[1]):
            for x in range(self.course.bounds[0]):
                if x < len(course) and y < len(course[x]):
                    string += "".join(course[x][y])   
            string += '\n'  
        return string

    def get_player_scorecard(self, player):
        # this is more useful in a club game, where they're stored elsewhere
        return self.scores[player]

    def compute_winners(self, include_NPC_scorecards = False):
        '''
            The winner is the entity (which might be a player, a club, or an NPCScorecardDummyEntity) who scored the most holes! Otherwise, lowest strokes wins
        '''
        winners = None
        tie = False

        if len(self.scores) == 0:
            raise ValueError("No scorecards means it's impossible to compute a winner!")

        for player in self.scores:
            if (type(player) == NPCScorecardDummyEntity or type(player) == str) and not include_NPC_scorecards: #non-glolfers can't win
                continue
            if winners is None: # start with the first player in the list
                winners = [player]
                tie = False
                continue
            winning_scorecard = self.scores[winners[0]]
            current_player_scorecard = self.scores[player] 
            if current_player_scorecard.balls_scored > winning_scorecard.balls_scored:
                winners = [player] # more holes? winner
                tie = False
            elif current_player_scorecard.balls_scored == winning_scorecard.balls_scored:
                if current_player_scorecard.total_strokes < winning_scorecard.total_strokes:
                    winners = [player] #same holes? lowest strokes wins
                    tie = False
                elif current_player_scorecard.total_strokes == winning_scorecard.total_strokes:
                    winners.append(player) # tie
                    tie = True
        return winners

    def is_tied(self):
        return len(self.compute_winning_players()) > 1

    def compute_winner_name(self, include_NPC_scorecards=False):
        if self.custom_winner_name is not None:
            return self.custom_winner_name

        winners = self.compute_winners(include_NPC_scorecards)
        if winners is None:
            return "nobody?"
        if len(winners) == 1:
            return winners[0].get_display_name()
        return "Everybody"

    def compute_random_current_winner(self):
        # return the winner if one winner exists, or a randomly-chosen winner if there's a tie
        # errors if there's no winner
        return random.choice(self.compute_winners(include_NPC_scorecards = False))

    def compute_random_winning_glolfer_currently_on_field(self):
        # compute_random_current_winner() might not return an entities.Glolfer. This is guaranteed to.
        glolfers = [o for o in self.objects if type(o) == entities.Glolfer]
        winners = None
        for player in glolfers:
            if winners is None: # start with the first player in the list
                winners = [player]
                continue
            winning_scorecard = self.get_player_scorecard(winners[0])
            player_scorecard = self.get_player_scorecard(player) 
            if player_scorecard.balls_scored > winning_scorecard.balls_scored:
                winners = [player] # more holes? winner
            elif player_scorecard.balls_scored == winning_scorecard.balls_scored:
                if player_scorecard.total_strokes < winning_scorecard.total_strokes:
                    winners = [player] #same holes? lowest strokes wins
                elif player_scorecard.total_strokes == winning_scorecard.total_strokes:
                    winners.append(player) # tie
        return random.choice(winners)

        # return the winner if one winner exists, or a randomly-chosen winner if there's a tie
        # errors if there's no winner
        return random.choice(self.compute_winners(include_NPC_scorecards = False))

    def end(self, custom_winner_name=None):
        if not self.over:
            self.over = True
            self.custom_winner_name = custom_winner_name
            self.send_message(f"**Game over! {self.compute_winner_name(include_NPC_scorecards=True)} wins!**")

    def print_score(self):
        string = ""
        current_winners = self.compute_winners()
        for player in self.scores:
            scorecard = self.scores[player]
            scorecard_string = scorecard.printed_representation()
            if player in current_winners and scorecard.total_strokes > 0 and not self.over:
                scorecard_string += " 👀"
            string += f"{scorecard_string} \n"

        return string


    def get_closest_object_to_position(self, position, object_type=None):
        consideredobjects = self.objects
        if object_type is not None:
             consideredobjects = [o for o in self.objects if (type(o) == object_type)]

        objectsSortedByDistance = sorted(consideredobjects, key=lambda object:np.linalg.norm(object.position-position))
        return objectsSortedByDistance[0]

    def object_shares_tile_with(self, target, object_type):
        # returns True if there's an object of type `object_type` on the same tile as `target` 
        for obj in self.objects:
            if type(obj) == object_type and self.on_same_tile(target, obj):
                return True
        return False

    def get_closest_objects(self, target, object_type=None):
        consideredobjects = [o for o in self.objects if o is not target]
        if object_type is not None:
             consideredobjects = [o for o in consideredobjects if type(o) == object_type]

        objectsSortedByDistance = sorted(consideredobjects, key=lambda object:np.linalg.norm(object.position-target.position))
        return objectsSortedByDistance

    def get_closest_object(self, target : entities.Entity, object_type=None):
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

    def send_message(self, message, print_in_summary=False):
        logger.info(f"Game {self.id}: {message}")
        self.message_queue.append(message)
        if print_in_summary:
            self.messages_to_report_in_summary.append(message)

    def on_score(self, scoring_player, ball, hole_position):
        for mod in self.modifiers:
            mod.on_score(scoring_player, ball, hole_position)

    def increase_score(self, scoring_player, added_strokes=0, added_balls_scored=0, added_scored_strokes=0):
        
        self.add_scorecard_if_doesnt_exist(scoring_player)
        self.scores[scoring_player].scored_strokes += added_scored_strokes
        self.scores[scoring_player].balls_scored += added_balls_scored
        self.scores[scoring_player].total_strokes += added_strokes

    def report_hit(self,shooting_player, ball,swing,club,shot_vec):

        if np.linalg.norm(shot_vec) > 6:
            length = "really long"
        elif np.linalg.norm(shot_vec) > 3:
            length = "long"
        elif np.linalg.norm(shot_vec) > 2:
            length = "medium"
        elif np.linalg.norm(shot_vec) > 1:
            length = "short"
        else:
            length = "terribly short"
        

        message = f"{shooting_player.get_display_name()} hits a {length} {swing.name}! {ball.displayEmoji}{utils.choose_direction_emoji(shot_vec)}"
        if self.debug:
            logging.debug(message + f"{shot_vec}")
            message += f"{shot_vec}"

        for obj in self.modifiers:
            obj.on_hit(shooting_player, ball, swing, club, shot_vec)

        self.increase_score(shooting_player, added_strokes=1)

        self.send_message(message)



