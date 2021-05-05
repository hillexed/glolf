import utils
import random
from enum import Enum

class SWORDFIGHT_OPTIONS(Enum):
    offensive=1
    defensive=2
    stylish=3
    kiss=4



def get_swordfight_move(player):

    options = (SWORDFIGHT_OPTIONS.offensive, SWORDFIGHT_OPTIONS.defensive, SWORDFIGHT_OPTIONS.stylish, SWORDFIGHT_OPTIONS.kiss)
    kiss_chance = 0.01
    weights = [player.stlats.churliness, player.stlats.earliness, player.stlats.twirliness, kiss_chance/(player.stlats.aceness+1)]


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
    
def print_swordfight_message(winning_move, losing_move, winner, loser):
    message = choose_swordfight_message(winning_move, losing_move, winner, loser)

    if winning_move != losing_move:
        if winning_move == SWORDFIGHT_OPTIONS.offensive:
            message = "🤺 " + message
        elif winning_move == SWORDFIGHT_OPTIONS.defensive:
            message = "🤸 " + message
        elif winning_move == SWORDFIGHT_OPTIONS.stylish:
            message = "🩰 " + message

        elif winning_move == SWORDFIGHT_OPTIONS.kiss:
            message = "💋 " + message

    if __name__ == "__main__":
        print(message)
        #print("TODO: SEND MESSAGE TO GAME")
    else:
        game.send_message(message)
    return message

pose_adjectives = ('menacing','disgusting','confusing','flat','2D','impressive','unflappable','flappable','owlish','goofy','light-hearted','clever','maniacal','majestic','limp','tight','tall','steel','sawtooth','fluttering','shivering','acidic',
'harsh','envious','slim','spicy','painful','healing','one-of-a-kind','bootleg','bootleg','abhorrent','juicy','clumsy','spectacular','quizzical','breezy','familiar','coordinated','reverse','dimensional',
'floating')
pose_adverbs = ('menacingly','disgustingly','lovingly','owlishly','goofily','light-heartedly','badly','shakily','lazily','frantically','briskly',
'directly','sharply','sheepishly','questionably','unnaturally',
'limply','tightly','promptly','cleverly','cheerfully','majestically')
fancy_attack_names = ("Marrow Parry","Double Jointed Double","Blameslash","reckless swing","Judo Chop","Swear","Propellor Thrust","Delta V","Best Defense","Dimensional Strike","Targeted Flop","Cannonball","Club","Compound Meter","Swingshot","Chelation","Metal Mettle","Cute Animal","Stylish Pose",f"{random.choice(pose_adjectives).title()} Rocket",f"{random.choice(pose_adjectives).title()} Swing","Mindy Wimdy","Bottles Wottles","Mocksicle","Hurdy-Gurdy","Bump","Spike","Hash Set",f"{random.choice(pose_adjectives).title()} Trap","Talk It Out")

def choose_swordfight_message(winning_move, losing_move, winner, loser):
    if winning_move == SWORDFIGHT_OPTIONS.offensive:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: # tie
            if random.random() < 0.8:
                # tie, common message
                messages = (f"{winner.name} {random.choice(('swings','thrusts','strikes'))}! {loser.name} parries! A clang rings out as the clubs clash!",
                            f"{winner.name} and {loser.name} lock eyes!",
                            f"{winner.name} and {loser.name} trade quick swings!",
                            f"{winner.name} and {loser.name} trade quick swings!")

                return random.choice(messages)

            else:
                # rare message
                rare_messages = (f"{winner.name} and {loser.name} Bonk one another back and forth!",
                    f"{winner.name} tries a {random.choice(fancy_attack_names)}! {loser.name} retaliates with a {random.choice(fancy_attack_names)}!")
                


                return random.choice(rare_messages)
        elif losing_move == SWORDFIGHT_OPTIONS.defensive: # should never get here
            return f"{winner.name} {random.choice(('swings','thrusts','strikes'))}! It slips through {loser.name}'s defense! Touché!" 
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: #offensive succeeds

            if random.random() < 0.8:
                # offensive succeeds, common message
                messages = (f"{winner.name} lunges!",
                            f"{winner.name} lands a swing!",
                            f"{winner.name} goes on the offensive!",
                            f"{winner.name} Bonks {loser.name}!")

                return random.choice(messages) + " Touché!"

            else:
                # rare message
                rare_messages = (
                            f"{winner.name} Lands an Ocean!",
                            f"{loser.name} strikes a {random.choice(pose_adjectives)} pose, but {winner.name} out-poses them!",
                            f"{winner.name} Superbonks {loser.name}!", 
                            f"{winner.name} swings! It slips through {loser.name}'s stylish moves!", 
                            f"{winner.name} thrusts! It slips through {loser.name}'s stylish moves!", 
                            f"{winner.name} unleashes their Signature Move!",
                            f"{winner.name} unleashes their {random.choice(pose_adjectives)} Signature Move! It catches {loser.name} by surprise!",
                            f"{winner.name} unleashes their Signature Move! {loser.name} is overwhelmed by handwriting!",
                            f"{winner.name} lunges! It slips through {loser.name}'s defense!")

                return random.choice(rare_messages) + " Touché!"
    # defense wins against stylish, ties defense
    elif winning_move == SWORDFIGHT_OPTIONS.defensive:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: # defensive > offensive
            if random.random() < 0.8:
                # defense succeeds, common message
                messages = (f"{loser.name} tries to Bonk {winner.name}, but it's Blonked!",
                    f"{winner.name} deflects {loser.name}'s efforts and counters!",
                    f"{winner.name} sees {loser.name}'s {random.choice(('strike','attack','advance','flip','wavedash','move','Signature Move','handwriting'))} coming and dodges!",
                    f"{loser.name} dodges {winner.name}'s {random.choice(fancy_attack_names)}!",)

                return random.choice(messages)
            else:
                acrobatic_actions = ((f"{winner.name} backflips out of the way!",
                        f"{winner.name} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.name} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.name} dodges with a {random.choice(pose_adjectives)} backflip!",
                        f"{winner.name} wavedashes away!",
                        f"{winner.name} sidesteps the issue.",
                        f"{winner.name} cartwheels out of the way",
                        f"{winner.name} dodges with a scissors leap!",
                        f"{winner.name} dodges with a back handspring!",
                        f"{winner.name} dodges with a front handspring!",
                        f"{winner.name} throws the attack aside!",))

                rare_messages = (
                    f"{loser.name} swings! {random.choice(acrobatic_actions)}",
                    f"{loser.name} lunges! {random.choice(acrobatic_actions)}",
                    f"{winner.name} sees {winner.name}'s advance coming! {random.choice(acrobatic_actions)}",
                    f"{winner.name} talks {loser.name} out of attacking for a second!",
                    f"{winner.name} takes a yummy snack break!"
                )

                return random.choice(rare_messages)
            
        elif losing_move == SWORDFIGHT_OPTIONS.defensive: # tie
            messages = (
                f"{winner.name} stares {loser.name} down {random.choice(pose_adverbs)}.",
                f"{winner.name} readies themselves! {loser.name} also readies themselves! They're both very ready.",
                f"{winner.name} and {loser.name} {random.choice(('backflip','wavedash','handspring','cartwheel','somersault'))} across the course!",
                f"{winner.name} and {loser.name} wavedash back and forth!",
                f"{random.choice((winner.name,loser.name))} fidgets {random.choice(pose_adverbs)}.",
                f"{random.choice((winner.name,loser.name))} polishes their glolf club.",
                f"{random.choice((winner.name,loser.name))} takes a moment to make sure the glolf ball hasn't {random.choice(('exploded','disappeared','become a player','eaten anything','been popsicled','become sentient','retired'))}."
                )

            return random.choice(messages)
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: # should never get here
            return f"{winner.name} defensives!"

    # stylish wins against defense, ties stylish
    elif winning_move == SWORDFIGHT_OPTIONS.stylish:
        if losing_move == SWORDFIGHT_OPTIONS.offensive: #shouldnt get here
            return "{loser.name} pulls off a stylish pose! It doesn't affect {winner.name} at all!"

        elif losing_move == SWORDFIGHT_OPTIONS.defensive:

            if random.random() < 0.8:
                messages = (
                    f"Despite {loser.name}'s {random.choice(('best','half-hearted','desperate'))} efforts, there's no stopping {winner.name}'s moves!",
                    f"{winner.name} does a {random.choice(('wavedash','backflip','therapy','wealth redistribution'))}! {loser.name} is {random.choice(('impressed','afraid','excited'))}!",
                    f"{winner.name} shows off their style! It's too much for {loser.name}!",
                    f"{winner.name} pulls off a stylish pose!"
                )

                return random.choice(messages) + " Touché!"
            else:
                rare_messages = (
                f"{loser.name} poses {random.choice(pose_adverbs)}!",
                f"{loser.name} strikes a {random.choice(pose_adjectives)} pose!",
                f"{winner.name} does a {random.choice(('wavedash','backflip','therapy','wealth redistribution'))}! {loser.name} is {random.choice(('impressed!','afraid','excited'))}!"
                )

                return random.choice(rare_messages) + " Touché!"
        elif losing_move == SWORDFIGHT_OPTIONS.stylish: # tie
            messages=(f"{winner.name} and {loser.name} pose {random.choice(pose_adverbs)} at one another!",
                f"{winner.name} and {loser.name} trade {random.choice(('phone numbers','blows','hits','digimon cards','souls','advice','taunts','jeers','tea packets'))}!",
                f"{winner.name} talks about their hobbies!",
                f"{winner.name} and {loser.name} take a moment to bond over shared interests!",
                f"{loser.name} infodumps excitedly to {winner.name}! {winner.name} listens intently!",
            )
            return random.choice(messages)

    # game immediately ends
    elif winning_move == SWORDFIGHT_OPTIONS.kiss:

        kiss_string = f"{winner.name} asks if they can kiss {loser.name}!"

        if random.random() < loser.stlats.aceness:
            rejection_messages = (f"{loser.name} isn't interested right now! {winner.name} understands and backs off.",
                f"{loser.name} is caught off guard! {winner.name} understands and backs off.",
                f"{loser.name} suggests maybe sometime later!",
                f"{loser.name}, flustered, asks to wait until after the game's over!")
            kiss_string += " "+random.choice(rejection_messages)
        else:
            # game.end(winner="Love") # "Love wins!" ######### TODO ###########
            acceptance_messages = (f"{loser.name} blushes and leans in!",f"{loser.name} is flustered but leans in!",f"{loser.name} raises an eyebrow and moves in!")
            kiss_string += " "+random.choice(acceptance_messages)
        return kiss_string
            
    

def swordfight(player1, player2):
    # if we're not in a duel:
    # game.send_message("X and Y begin to Duel! En garde!")



    # see who loses
    #if player1.hp < 0:
    #    return lose_swordfight(player1,winner=player2)

    #elif player2.hp < 0:
    #    return lose_swordfight(player2,winner=player1)
        # yes that does mean if p1 and p2 both have 0 hp at the same time for some reason, p1 dies from port priority.


    p1move = get_swordfight_move(player1)
    p2move = get_swordfight_move(player2)

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

        print_swordfight_message(p1move, p2move, player1, player2)
        # player2.hp -= 1

    # p2 wins
    elif (p2move, p1move) in winning_combos:
        # p1 lost the point!

        print_swordfight_message(p2move, p1move, player2, player1)
        # player1.hp -= 1
    else: # tie
        
        print_swordfight_message(p1move, p2move, player1, player2)

def lose_swordfight(loser, winner):

    first_message = random.choice((
        "{winner.name} sees their chance! They wind up... and swing!"
        "{loser.name} is out of motivation! {winner.name} winds up... and swings!"
        "{winner.name} siezes the moment! They wind up... and swing!"))
    next_message = random.choice((
        f"{loser.name} is sent flying!",
        f"{loser.name} flies into the air!"
        f"{loser.name} is launched into the air!"))

    game.send_message(f"{first_message} {next_message}! Hole in one!")

    # the winner already has access to a ball now, so they don't need an extra hole    
    #game.scores[winner].scored_strokes += 1
    #game.scores[winner].balls_scored += 1

    # loser.position = farthest hole's position


if __name__ == "__main__":
    import players
    for i in range(10):
        swordfight(players.generate_random_player_from_name("Accc"),players.generate_random_player_from_name("Bc"))

