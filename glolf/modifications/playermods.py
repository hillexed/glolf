from .modification import PlayerModification
# good mods

class Attractor(PlayerModification):
    displayEmoji = "🦅"
    isDead = False
    description = "This player will sometimes Attract balls."

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        if random.random() < 0.1:
            current_glolfer_action["action"] = "attracting"
            ball = get current ball
            move ball closer to self.player.position
                self.game.send_message(f"{self.player.get_display_name()} Attracts a ball towards them!")

class BurstOfSpeed(PlayerModification):
    # jet engine?
    displayEmoji = "🦅"
    description="This player sometimes bursts forwards in a straight line."

    # make nyoomability temporarily 10 every random.randrange((10,14)) turns


# Lent a Hand: this player isn't very left-handed
# Flat Earther: Balls hit out of bounds fall off the course and respawn. 
# Detachable Tail (mermaid emoji): <seashells LLSea> brand! Travel faster in water.
# 

# bad mods

class Sticky(PlayerModification):
    # disadvantage
    displayEmoji = ":honey_pot:"
    description = "When this player hits a ball, the ball might stick to the club."

    def __init__(self, game, attached_player):
        self.game = game
        self.player = attached_player

    def on_attempted_hit(self, glolfer, current_glolfer_action):
        if random.random() < 0.1:
            current_glolfer_action["action"] = "no hit"
            self.game.send_message(f"{self.player.get_display_name()} hits a drive... but the ball sticks to the club!")

class Repeller(PlayerModification):
    displayEmoji = "🦅"
    isDead = False

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        if random.random() < 0.1:
            current_glolfer_action["action"] = "repelling"
            ball = get current ball
            move ball away from self.player.position
                self.game.send_message(f"{self.player.get_display_name()} Repels a ball!")


# Friend of Eagles: eagles will never target this player
# Run Away: during duels this player has a chance to Run Away
class ChampionshipJacket(PlayerModification):
    displayEmoji = "🧥"
    description = "This player has won an Internet Open."

class Out(PlayerModification):
    displayEmoji = "🦢"
    description = "Spacetime stares back."

class Diamonds(PlayerModification):
    displayEmoji = "♦️"
    description = "This player uses Diamonds instead of Clubs."

class OnARoll(PlayerModification):
    displayEmoji = "🧻"
    description = "This player is On a Roll!"

class Friendship(PlayerModification):
    displayEmoji = "🤝💖"
    description = "This player is learning the banned art of Friendship."


# emojis for fear


class TwoChampionshipJackets(PlayerModification):
    displayEmoji = "🧥🧥"
    description = "This player has won two Internet Opens and a Hangar."

class ThreeChampionshipJackets(PlayerModification):
    displayEmoji = "🧥🧥🧥"
    description = "This player has won three Internet Opens and a Hangar."

class Buzzword(PlayerModification):
    displayEmoji = ":bee:"
    description = "This player has become a Buzzword."

class LegallyDistinctNutritionalSocks(PlayerModification):
    displayEmoji = ":socks:"
    description = "[Description removed per pending copyright litigation]"


# lookup table for eventual command use
# todo: use this to make a command that lets you look up mods
# include eagle mods too
mods_by_emoji = {}
for mod in (Attractor, BurstOfSpeed Out, Diamonds, Friendship, OnARoll):
    if mod.displayEmoji in mods_by_emoji:
        raise ValueError("Two mods have the same {} emoji!".format(mod.displayEmoji))
    mods_by_emoji[mod.displayEmoji] = mod
