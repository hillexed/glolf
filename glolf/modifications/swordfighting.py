
import random
from enum import Enum

import utils
from .modification import Modification
from entities import Entity, Hole, Glolfer, HittingArrow, ScoreConfetti, SwordfightIndicator

class SWORDFIGHT_OPTIONS(Enum):
    offensive=1
    defensive=2
    stylish=3
    kiss=4

pose_adjectives = ('menacing','disgusting','confusing','flat','2D','impressive','unflappable','flappable','owlish','goofy','light-hearted','clever','maniacal','majestic','limp','tight','tall','steel','sawtooth','fluttering','shivering','acidic',
'harsh','dreaded','slim','spicy','painful','healing','one-of-a-kind','bootleg','bootleg','abhorrent','juicy','clumsy','spectacular','quizzical','breezy','familiar','coordinated','reverse','dimensional',
'floating','invisible','compound','cute','socialist','dramatic')
pose_adverbs = ('menacingly','disgustingly','lovingly','owlishly','goofily','light-heartedly','badly','shakily','lazily','frantically','briskly',
'directly','sharply','sheepishly','questionably','unnaturally',
'limply','tightly','promptly','cleverly','cheerfully','majestically','dramatically')
fancy_attack_names = ("Marrow Parry","Double Jointed Double","Blameslash","reckless swing","Judo Chop","Swear","Propellor Thrust","Delta V","Best Defense","Dimensional Strike","Targeted Flop","Cannonball","Club","Compound Meter","Swingshot","Chelation","Metal Mettle","Cute Animal","Stylish Pose",f"{random.choice(pose_adjectives).title()} Rocket",f"{random.choice(pose_adjectives).title()} Swing","Mindy Wimdy","Bottles Wottles","Mocksicle","Hurdy-Gurdy","Bump","Spike","Hash Set",f"{random.choice(pose_adjectives).title()} Trap","Talk It Out","Paper Plane","Root Around","Crime",f"{random.choice(pose_adjectives).title()} Poke", "Garbage Fling", "Gunk Shot", "Animal Assist", "Hunk Shot", "Jillywam", "Measure Zero", "Mandelbonk","Diffeomorphism","Pathological Example","Taken Limit","Broken Limit","See-no-blade","Outer Mild","Infinite Sum","False False Swipe","Backhanded Compliment","Apprentice Spark"
)

def choose_swordfight_message(winning_move, losing_move, winner, loser):
    if winning_move == SWORDFIGHT_OPTIONS.offensive:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: # tie
            if random.random() < 0.8:
                # tie, common message
                messages = (f"{loser.get_display_name()} {random.choice(('swings','thrusts','strikes'))}! {winner.get_display_name()} parries! A clang rings out as the clubs clash!",
                            f"{winner.get_display_name()} and {loser.get_display_name()} lock eyes!",
                            f"{winner.get_display_name()} and {loser.get_display_name()} trade quick swings!",
                            f"{winner.get_display_name()} and {loser.get_display_name()} trade quick swings!")

                return random.choice(messages)

            else:
                # rare message
                rare_messages = (f"{winner.get_display_name()} and {loser.get_display_name()} Bonk one another back and forth!",
                    f"{winner.get_display_name()} tries a {random.choice(fancy_attack_names)}! {loser.get_display_name()} retaliates with a {random.choice(fancy_attack_names)}!")
                


                return random.choice(rare_messages)
        elif losing_move == SWORDFIGHT_OPTIONS.defensive: # should never get here
            return f"{winner.get_display_name()} {random.choice(('swings','thrusts','strikes'))}! It slips through {loser.get_display_name()}'s defense! Touché!" 
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: #offensive succeeds

            if random.random() < 0.8:
                # offensive succeeds, common message
                messages = (f"{winner.get_display_name()} lunges!",
                            f"{winner.get_display_name()} thrusts!",
                            f"{winner.get_display_name()} lands a swing!",
                            f"{winner.get_display_name()} goes on the offensive!",
                            f"{winner.get_display_name()} Bonks {loser.get_display_name()}!",
                            f"{winner.get_display_name()} tries a {random.choice(fancy_attack_names)}!")

                return random.choice(messages) + " Touché!"

            else:
                # rare message
                rare_messages = (
                            f"{winner.get_display_name()} Lands an Ocean!",
                            f"{loser.get_display_name()} strikes a {random.choice(pose_adjectives)} pose, but {winner.get_display_name()} out-poses them!",
                            f"{winner.get_display_name()} Superbonks {loser.get_display_name()}!", 
                            f"{winner.get_display_name()} swings! It slips through {loser.get_display_name()}'s stylish moves!", 
                            f"{winner.get_display_name()} thrusts! It slips through {loser.get_display_name()}'s stylish moves!", 
                            f"{winner.get_display_name()} unleashes their Signature Move!",
                            f"{winner.get_display_name()} unleashes their {random.choice(pose_adjectives)} Signature Move! It catches {loser.get_display_name()} by surprise!",
                            f"{winner.get_display_name()} unleashes their Signature Move! {loser.get_display_name()} is overwhelmed by handwriting!",
                            f"{winner.get_display_name()} lunges! It slips through {loser.get_display_name()}'s defense!",
                            f"{winner.get_display_name()} tries a {random.choice(fancy_attack_names)}!",
                            f"{winner.get_display_name()} tries a {random.choice(fancy_attack_names)}!",
                            f"{winner.get_display_name()} tries a {random.choice(fancy_attack_names)}!")

                return random.choice(rare_messages) + " Touché!"
    # defense wins against stylish, ties defense
    elif winning_move == SWORDFIGHT_OPTIONS.defensive:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: # defensive > offensive
            if random.random() < 0.8:
                # defense succeeds, common message
                messages = (f"{loser.get_display_name()} tries to Bonk {winner.get_display_name()}, but it's Blonked!",
                    f"{winner.get_display_name()} deflects {loser.get_display_name()}'s efforts and counters!",
                    f"{winner.get_display_name()} sees {loser.get_display_name()}'s {random.choice(('strike','attack','advance','flip','club','move','Signature Move','handwriting'))} coming and dodges!",
                    f"{winner.get_display_name()} dodges {loser.get_display_name()}'s {random.choice(fancy_attack_names)}!",)

                return random.choice(messages)
            else:
                acrobatic_actions = ((f"{winner.get_display_name()} backflips out of the way!",
                        f"{winner.get_display_name()} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.get_display_name()} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.get_display_name()} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.get_display_name()} wavedashes away!",
                        f"{winner.get_display_name()} sidesteps the issue.",
                        f"{winner.get_display_name()} cartwheels out of the way!",
                        f"{winner.get_display_name()} dodges with a {random.choice(pose_adjectives)} scissors leap!",
                        f"{winner.get_display_name()} dodges with a back handspring!",
                        f"{winner.get_display_name()} dodges with a front handspring!",
                        f"{winner.get_display_name()} throws the attack aside!",))

                rare_messages = (
                    f"{loser.get_display_name()} swings! {random.choice(acrobatic_actions)}",
                    f"{loser.get_display_name()} lunges! {random.choice(acrobatic_actions)}",
                    f"{winner.get_display_name()} sees {loser.get_display_name()}'s advance coming! {random.choice(acrobatic_actions)}",
                    f"{winner.get_display_name()} talks {loser.get_display_name()} out of attacking for a second!",
                    f"{winner.get_display_name()} takes a yummy snack break!",
                    f"{winner.get_display_name()} {random.choice(pose_adverbs)} blocks all damage!",       
                )

                return random.choice(rare_messages)
            
        elif losing_move == SWORDFIGHT_OPTIONS.defensive: # tie
            messages = (
                f"{winner.get_display_name()} stares {loser.get_display_name()} down {random.choice(pose_adverbs)}.",
                f"{winner.get_display_name()} readies themselves! {loser.get_display_name()} also readies themselves! They're both very ready.",
                f"{winner.get_display_name()} and {loser.get_display_name()} {random.choice(('backflip','wavedash','handspring','cartwheel','somersault'))} across the course!",
                f"{winner.get_display_name()} and {loser.get_display_name()} wavedash back and forth!",
                f"{random.choice((winner.get_display_name(),loser.get_display_name()))} fidgets {random.choice(pose_adverbs)}.",
                f"{random.choice((winner.get_display_name(),loser.get_display_name()))} polishes their glolf club.",
                f"{random.choice((winner.get_display_name(),loser.get_display_name()))} takes a moment to make sure the glolf ball hasn't {random.choice(('exploded','disappeared','become a player','eaten anything','been popsicled','become sentient','retired'))}."
                )

            return random.choice(messages)
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: # should never get here
            return f"{winner.get_display_name()} defensives!"

    # stylish wins against defense, ties stylish
    elif winning_move == SWORDFIGHT_OPTIONS.stylish:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: #shouldnt get here
            return "{loser.get_display_name()} pulls off a stylish pose! It doesn't affect {winner.get_display_name()} at all!"

        elif losing_move == SWORDFIGHT_OPTIONS.defensive:

            if random.random() < 0.8:
                messages = (
                    f"Despite {loser.get_display_name()}'s {random.choice(('best','half-hearted','desperate'))} efforts, there's no stopping {winner.get_display_name()}'s moves!",
                    f"{winner.get_display_name()} does a {random.choice(('speedpaint','jig','crime','side flip','backwards high jump','backflip','therapy','wealth redistribution'))}! {loser.get_display_name()} is {random.choice(('impressed','afraid','excited'))}!",
                    f"{winner.get_display_name()} shows off their style! It's too much for {loser.get_display_name()}!",
                    f"{winner.get_display_name()} expresses themself through {random.choice(pose_adjectives)} {random.choice(('dance','poetry','song','sculpture','interpretive dance','naps','creation','words','photography','art','incoherent yelling'))}!",
                )

                return random.choice(messages) + " Touché!"
            else:
                rare_messages = (
                f"{loser.get_display_name()} tries to sketch {winner.get_display_name()} but {random.choice(('gets the details wrong','has trouble drawing hands','has trouble drawing their features','has trouble matching the image in their head','drops it halfway through'))}!",
                f"{winner.get_display_name()} poses {random.choice(pose_adverbs)}!",
                f"{winner.get_display_name()} strikes a {random.choice(pose_adjectives)} pose!",
                f"{winner.get_display_name()} does a {random.choice(('wavedash','backflip','therapy','wealth redistribution'))}! {loser.get_display_name()} is {random.choice(('impressed!','afraid','excited'))}!"
                )

                return random.choice(rare_messages) + " Touché!"
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: # tie
            messages=(f"{winner.get_display_name()} and {loser.get_display_name()} pose {random.choice(pose_adverbs)} at one another!",
                f"{winner.get_display_name()} and {loser.get_display_name()} trade {random.choice(('phone numbers','blows','hits','digimon cards','souls','advice','taunts','jeers','tea packets'))}!",
                f"{winner.get_display_name()} talks about their hobbies!",
                f"{winner.get_display_name()} and {loser.get_display_name()} take a moment to bond over shared interests!",
                f"{loser.get_display_name()} infodumps excitedly to {winner.get_display_name()}! {winner.get_display_name()} listens {random.choice(('intently','excitedly'))}!",
            )
            return random.choice(messages)

    # game immediately ends
    elif winning_move == SWORDFIGHT_OPTIONS.kiss:

        kiss_string = f"{winner.get_display_name()} asks if they can kiss {loser.get_display_name()}!"

        if losing_move != SWORDFIGHT_OPTIONS.kiss: #consent is important!
            rejection_messages = (f"{loser.get_display_name()} isn't interested right now! {winner.get_display_name()} understands and backs off.",
                f"{loser.get_display_name()} is caught off guard! {winner.get_display_name()} understands and backs off.",
                f"{loser.get_display_name()} suggests maybe sometime later!",
                f"{loser.get_display_name()}, flustered, asks to wait until after the game's over!")
            kiss_string += " "+random.choice(rejection_messages)
        else:
            acceptance_messages = (f"{loser.get_display_name()} blushes and leans in!",f"{loser.get_display_name()} is flustered but leans in!",f"{loser.get_display_name()} raises an eyebrow and moves in!",f"{loser.get_display_name()} smiles and moves in!")
            kiss_string += " "+random.choice(acceptance_messages)
        return kiss_string


class SwordfightingDecree(Modification):
    # handles all logic for swordfights, including inserting into glolfer.update()

    starting_hp = 3
    players_in_interdimensional_void = [] # shared among all games
    dimensional_travel_chance = 0.05 # TODO: CHANGE


    def __init__(self, game):
        self.game = game
        self.current_swordfights = []
        self.new_swordfights = []
        self.stunned_from_swordfight = []
        self.player_hp = {}

    def get_current_duel(self, glolfer):

        for fight in self.current_swordfights:
            if glolfer in fight:
                return fight

        for fight in self.new_swordfights:
            if glolfer in fight:
                return fight

        return None

    def is_in_a_duel(self, glolfer):
        if self.get_current_duel(glolfer) is not None:
            return True
        return False



    def get_swordfight_move(self, player):

        options = (SWORDFIGHT_OPTIONS.offensive, SWORDFIGHT_OPTIONS.defensive, SWORDFIGHT_OPTIONS.stylish, SWORDFIGHT_OPTIONS.kiss)
        kiss_chance = 0.01 * 2 / len(self.game.scores)

        if self.game.turn_number < self.game.max_turns/3:
            kiss_chance = 0.00

        weights = [player.stlats.churliness, player.stlats.earliness, player.stlats.twirliness, kiss_chance/(player.stlats.aceness+1)]

        if self.game.turn_number < 10:
            weights[3] = 0 # no kissing until at least a little game has passed


        # churliness-boosting stances
        if player.stlats.stance in ("Aggro","Powerful","Hand to Hand","DPS","Explosive","Hardcore", "Wibble","Electric"): #offense-boosting stances
            weights[0] += 0.5
        # earliness-boosting stances
        elif player.stlats.stance in ("Tanky","Twitchy","Repose","Reverse","Softcore",  "Cottagecore","Pomegranate"): # defense-boosting stances
            weights[1] += 0.5
        #twirliness-boosting stances
        if player.stlats.stance in ("Feint","Tricky","Pop-Punk","Flashy","Spicy",       "Corecore","Wobble","Lefty"): # style-boosting stances
            weights[2] += 0.5

        return utils.random_weighted_choice(options, weights)
        

    def on_glolfer_move(self, glolfer, target):

        # glolfers actively avoid joining duels if they have high wiggle
        if not self.is_in_a_duel(glolfer):
            if self.game.object_shares_tile_with(target, SwordfightIndicator):
                # if your wiggle is high enough, you don't join the swordfight
                if random.random() - 0.5 < glolfer.stlats.wiggle:
                    return glolfer # change target to your current position. stay in place
        return None # don't change the target

    def on_glolfer_update(self, glolfer, current_glolfer_action):

        in_swordfight = self.is_in_a_duel(glolfer)
            
        if not in_swordfight:
            # should we start a swordfight?
            target_glolfer = self.game.get_closest_object(glolfer, Glolfer)
            a_hole = self.game.get_closest_object(glolfer, Hole)
            if target_glolfer is not None and self.game.on_same_tile(target_glolfer, glolfer) and not self.game.on_same_tile(glolfer, a_hole) and random.random() < 0.5:
                self.start_swordfight(glolfer, target_glolfer)
                in_swordfight = True

        if in_swordfight:
            current_glolfer_action["action"] = "swordfighting" #stop the player from moving or hitting balls

        # make players stay in place for one turn after losing a swordfight and being launched into the hole
        if glolfer in self.stunned_from_swordfight:
            current_glolfer_action["action"] = "stunned" #stop the player from moving or hitting balls
            self.stunned_from_swordfight.remove(glolfer)

    def start_swordfight(self, initiating_glolfer, glolfer2):
        # start a swordfight
        # this means if there's 3 players on the same tile there'll be one player facing two swordfights
        if initiating_glolfer not in self.player_hp:
            self.player_hp[initiating_glolfer] = initiating_glolfer.stlats.marbles
        if glolfer2 not in self.player_hp:
            self.player_hp[glolfer2] = glolfer2.stlats.marbles

        current_duel = self.get_current_duel(glolfer2) # a 'duel' is a list of multiple Players all dueling

        if current_duel is None:
            self.game.send_message(f"⚔️ {initiating_glolfer.get_display_name()} challenges {glolfer2.get_display_name()} to a Duel! En garde!")
            self.new_swordfights.append((initiating_glolfer, glolfer2))
            self.game.add_object(SwordfightIndicator(self.game, initiating_glolfer.position))
        else:
            # join the duel that glolfer2 is in
            self.remove_duel(current_duel)
            self.new_swordfights.append(current_duel + (initiating_glolfer,))
            self.game.send_message(f"⚔️ {initiating_glolfer.get_display_name()} joins the Duel between {self.format_participant_names(current_duel)}! En garde!")

    def remove_duel(self, duel):
        if duel in self.current_swordfights:
            self.current_swordfights.remove(duel)
        if duel in self.new_swordfights:
            self.new_swordfights.remove(duel)

    def update(self):

        for duel in self.current_swordfights[:]:
            glolfer1, glolfer2 = random.sample(duel, 2) 
            self.swordfight(duel, glolfer1, glolfer2)

        self.current_swordfights = self.current_swordfights + self.new_swordfights
        self.new_swordfights = []

        if len(self.players_in_interdimensional_void) > 0:
            player_name, source_game_id = random.choice(self.players_in_interdimensional_void)
            if self.game.turn_number == 5 and self.game.id != source_game_id:
                self.game.add_player(self.game.course.random_position_on_course(), player_name)
                self.game.send_message(f"**💥 {player_name} tumbles out of a crack in reality onto the course!**", print_in_summary=True)

    def format_participant_names(self, duelist_list):
        return utils.format_list_with_commas([p.get_display_name() for p in duelist_list])

    def swordfight(self, current_duelists_list, glolfer1, glolfer2):

        # if one of the players got moved, stop fighting
        if not self.game.on_same_tile(glolfer1, glolfer2):
            if current_duelists_list in self.current_swordfights:
                self.remove_duel(current_duelists_list)   
                self.game.send_message(f"⚔️ The Duel between {self.format_participant_names(current_duelists_list)} is called off!")
                # todo: if a 3-player duel loses one of its members, don't cancel the entire duel, but start a new one with just the remaining valid players 
                return 

        # see who loses
        if self.player_hp[glolfer1] <= 0:
            return self.lose_swordfight(current_duelists_list, loser=glolfer1,winner=glolfer2)

        elif self.player_hp[glolfer2] <= 0:
            return self.lose_swordfight(current_duelists_list, loser=glolfer2,winner=glolfer1)
            # yes that does mean if p1 and p2 both have 0 hp at the same time for some reason, p1 dies from port priority.


        self.game.add_object(SwordfightIndicator(self.game, glolfer1.position))

        p1move = self.get_swordfight_move(glolfer1)
        p2move = self.get_swordfight_move(glolfer2)

        winning_combos = (# move 1, the thing move 1 beats
            (SWORDFIGHT_OPTIONS.defensive,SWORDFIGHT_OPTIONS.offensive),
            (SWORDFIGHT_OPTIONS.stylish,SWORDFIGHT_OPTIONS.defensive),
            (SWORDFIGHT_OPTIONS.offensive,SWORDFIGHT_OPTIONS.stylish),

            (SWORDFIGHT_OPTIONS.kiss,SWORDFIGHT_OPTIONS.offensive), # kiss beats everything
            (SWORDFIGHT_OPTIONS.kiss,SWORDFIGHT_OPTIONS.defensive),
            (SWORDFIGHT_OPTIONS.kiss,SWORDFIGHT_OPTIONS.stylish),
            (SWORDFIGHT_OPTIONS.kiss,SWORDFIGHT_OPTIONS.kiss),
        )

        # p1 wins
        if (p1move, p2move) in winning_combos:
            # p1 won the point!
            self.handle_swordfight_result(current_duelists_list, p1move, p2move, glolfer1, glolfer2)
            self.player_hp[glolfer2] -= 1

        # p2 wins
        elif (p2move, p1move) in winning_combos:
            # p1 lost the point!
            self.handle_swordfight_result(current_duelists_list, p2move, p1move, glolfer2, glolfer1)
            self.player_hp[glolfer1] -= 1
        else: # tie
            
            self.handle_swordfight_result(current_duelists_list, p1move, p2move, glolfer1, glolfer2)


    def get_emoji(self, movetype):
            if movetype == SWORDFIGHT_OPTIONS.offensive:
                return "🤺"
            elif movetype == SWORDFIGHT_OPTIONS.defensive:
                return "🤸"
            elif movetype == SWORDFIGHT_OPTIONS.stylish:
                return "🩰"
            elif movetype == SWORDFIGHT_OPTIONS.kiss:
                return "💋"
            else:
                return ""



    def handle_swordfight_result(self, current_duelists_list, winning_move, losing_move, winner, loser):

        print_in_summary = False
        if winning_move == SWORDFIGHT_OPTIONS.kiss:
            print_in_summary = True
            if losing_move != SWORDFIGHT_OPTIONS.kiss: 
                # one side asks to kiss. roll to see if the other one accepts

                if random.random() > loser.stlats.aceness:
                    # asked to kiss, passed the ace check, partner reciprocates
                    losing_move = SWORDFIGHT_OPTIONS.kiss

        message = choose_swordfight_message(winning_move, losing_move, winner, loser)

        if winning_move == losing_move:
            message = "    " + self.get_emoji(winning_move) + "  " + message
        else:
            message = "    " + self.get_emoji(winning_move) + "  " + message

        self.game.send_message(f"⚔️ {self.format_participant_names(current_duelists_list)} are Dueling! ⚔️")
        self.game.send_message(message, print_in_summary)

        # love wins
        if winning_move == losing_move and winning_move == SWORDFIGHT_OPTIONS.kiss:
            self.game.end(custom_winner_name="Love")

        return message

    def lose_swordfight(self, current_duelists_list, loser, winner):

        first_message = random.choice((
            f"{winner.get_display_name()} sees their chance! They wind up... and swing!",
            f"{loser.get_display_name()} is out of motivation! {winner.get_display_name()} winds up... and swings!",
            f"{winner.get_display_name()} siezes the moment! They wind up... and swing!"))
        next_message = random.choice((
            f"{loser.get_display_name()} is sent flying",
            f"{loser.get_display_name()} flies into the air",
            f"{loser.get_display_name()} is launched into the air"))

        self.player_hp[loser] = loser.stlats.marbles

        # the winner already has access to a ball now, so they don't need an extra hole    
        #game.scores[winner].scored_strokes += 1
        #game.scores[winner].balls_scored += 1


        # the loser is hit into the farthest hole
        holes = self.game.get_closest_objects(winner, Hole)
        if len(holes) > 0:
            farthesthole = holes[-1]
            loser.position = utils.copyvec(farthesthole.position)

            hitvec = farthesthole.position - winner.position
            self.game.add_object(HittingArrow(self.game, utils.copyvec(winner.position), hitvec))
            self.game.add_object(ScoreConfetti(self.game, utils.copyvec(farthesthole.position)))

            self.game.send_message(f"⚔️ **{first_message} {next_message} {utils.choose_direction_emoji(hitvec)}! Hole in one!**")

        else:
            self.game.send_message("Wait. There's... no holes? {winner.get_display_name()} is a bit confused.")

        if not self.game.is_tournament and random.random() < self.dimensional_travel_chance:
            if self.game.scores[loser].balls_scored - self.game.scores[winner].balls_scored > 2 and random.random() > winner.stlats.needlethreadableness: #low-needlethreadableness players who are losing
                # knocked into another game
                self.players_in_interdimensional_void.append((loser.name, self.game.id))
                self.game.objects.remove(loser)
                self.game.send_message(f"💥 **Reality cracks! {winner.get_display_name()} knocks {loser.get_display_name()} out of reality!**", print_in_summary=True)

        self.remove_duel(current_duelists_list)

        # just in case
        for fight in self.current_swordfights:
            if loser in fight:
                self.current_swordfights.remove(fight)

        self.stunned_from_swordfight.append(loser)



if __name__ == "__main__":
    import players
    from game import SingleHole
    mockgame = SingleHole()
    d = SwordfightingDecree(mockgame)
    mockgame.send_message = print
    glolfer1 = Glolfer(mockgame, position = [0,0], playername="Pikachu")
    glolfer2 = Glolfer(mockgame, position = [0,0], playername="Eevee")
    d.start_swordfight(glolfer1,glolfer2)
    for i in range(10):
        d.update()

