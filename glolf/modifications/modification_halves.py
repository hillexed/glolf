from courses import WATER_TILES
from entities import FlyingEagle, FlyingAlbatross, Hole, Glolfer
import random

def increase_stlat_for_rest_of_game(stlats, key, delta):
    stlats._replace(**{key: getattr(stlats, key)+delta})
def decrease_stlat_for_rest_of_game(stlats, key, delta):
    new_val = getattr(stlats, key)+delta
    if new_val < 0:
        new_val = 0.01
    stlats._replace(**{key: new_val})


class MergedModificationTrigger:
    emoji="?"
    description_firsthalf = "When something mysterious happens"

    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player

    def should_trigger(self, glolfer, current_glolfer_action):
        return False

    def on_score(self, scoring_player, ball, hole_position):
        pass

class MergedModificationEffect:
    emoji="?"
    description_secondhalf="something mysterious happens"
    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player

    def apply_effect(self, glolfer, current_glolfer_action):
        pass


# A decorator so you can write triggers that don't always trigger
def randomly_trigger(chance=0.2):
    def created_decorator(func):
        def wrapper(*args, **kwargs):
            should_trigger = func(*args, **kwargs)
            if should_trigger is True and random.random() < chance:
                return True
            return False
        return wrapper
    return created_decorator


class TriggerOnATile(MergedModificationTrigger):
    emoji=" "
    trigger_tiles = []

    @randomly_trigger(chance=0.05)
    def should_trigger(self, glolfer, current_glolfer_action):
        for tile in self.trigger_tiles:
            if self.game.course.get_tile_at(glolfer.position) == tile:
                return True
        return False

class TriggerInWind(MergedModificationTrigger):
    # todo
    emoji="🌬️"
    wind_types = (None)

    @randomly_trigger(0.02) #wind is always active, so very low chance
    def should_trigger(self, glolfer, current_glolfer_action):
        if self.game.wind in self.wind_types:
                return True
        return False


class TriggerNearEntity(MergedModificationTrigger):
    # todo
    emoji=" "
    entity_type=None
    distance_to_trigger=3

    @randomly_trigger(0.3)
    def should_trigger(self, glolfer, current_glolfer_action):
        closest_object = self.game.get_closest_object_to_position(glolfer.position, object_type=self.entity_type)
        dist = (closest_object.position-glolfer.position).norm()

        if dist < self.distance_to_trigger:
                return True
        return False



# triggers

class OnSand(TriggerOnATile):
    emoji = "🟨"
    trigger_tiles=["🟨"]
    description_firsthalf="On sand hazards (🟨)"

class OnWater(TriggerOnATile):
    emoji="🟦"
    trigger_tiles = WATER_TILES
    description_firsthalf="On water (🟦)"

class NearHole(TriggerNearEntity):
    emoji="⛳"
    entity_type=Hole
    distance_to_trigger=2
    description_firsthalf = "Sometimes when near a hole (⛳)"

class NearOtherGlolfer(TriggerNearEntity):
    emoji="🏌️"
    entity_type=Glolfer
    distance_to_trigger=2
    description_firsthalf = "Sometimes when near another glolfer"

class OnFirstBall(MergedModificationTrigger):
    emoji="🟣"
    description_firsthalf = "The first time per game this glolfer scores"

    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player
        self.activated = False

    def should_trigger(self, glolfer, current_glolfer_action): # always activates
        if self.activated:
            return True
            self.activated = False
        return False

    def on_score(self, scoring_player, ball, hole_position):
        if self.attached_glolfer == scoring_player and self.game.scores[scoring_player].balls_scored == 1:
            self.activated = True

class BallScoresItself(MergedModificationTrigger):
    emoji="🟠"
    description_firsthalf = "If the ball scores itself"

    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player
        self.activated = False

    def should_trigger(self, glolfer, current_glolfer_action): # always activates
        if self.activated:
            self.activated = False
            return True
        return False

    def on_score(self, scoring_player, ball, hole_position):
        if scoring_player.name == "The Ball":
            self.activated = True

class Envious(MergedModificationTrigger):
    emoji="🟢"
    description_firsthalf = "Rarely if another glolfer scores"

    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player
        self.activated = False

    @randomly_trigger(0.15) # balanced by not always activating
    def should_trigger(self, glolfer, current_glolfer_action):
        if self.activated:
            return True
            self.activated = False
        return False

    def on_score(self, scoring_player, ball, hole_position):
        if self.attached_glolfer != scoring_player:
            self.activated = True

class OnScore(MergedModificationTrigger):
    emoji="⚪"
    description_firsthalf = "Sometimes when scoring"

    def __init__(self, game, attached_player):
        self.game = game    
        self.attached_player = attached_player
        self.activated = False

    @randomly_trigger(0.25) # balanced by not always activating
    def should_trigger(self, glolfer, current_glolfer_action):
        if self.activated:
            return True
            self.activated = False
        return False

    def on_score(self, scoring_player, ball, hole_position):
        if self.attached_glolfer == scoring_player:
            self.activated = True

class InElectricWind(TriggerInWind):
    emoji="🔌"
    wind_types = ("Mechanical","Electric", "Increased Lightning")
    description_firsthalf = "In various electromagnetic winds"

class InMathematicalWind(TriggerInWind):
    emoji="🧮"
    wind_types = ("Four-Dimensional","Manifold", "Differential")
    description_firsthalf = "In various mathematical winds"

class InFlavoredWind(TriggerInWind):
    emoji="👅"
    wind_types = ("Fruity","Tasteless", "Pheasant")
    description_firsthalf = "In flavor-related winds"

class InScaryWind(TriggerInWind):
    emoji="😱"
    wind_types = ("Ominous","Increased Lightning", "Monsoon")
    description_firsthalf = "In terrifying winds"

# effects

class MoreMarbles(MergedModificationEffect):
    emoji="⚪"
    description_secondhalf="this glolfer picks up more Marbles, helping them survive Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "marbles", 1)
        self.game.send_message(f"{glolfer.get_display_name()} picked up an extra Marble!")

class SummonEagle(MergedModificationEffect):
    emoji="🦅"
    description_secondhalf="an eagle might swoop onto the course"
    def apply_effect(self, glolfer, current_glolfer_action):
        self.game.objects.append(FlyingEagle(self.game, glolfer))
        self.game.send_message(f"{glolfer.get_display_name()} attracted an Eagle (🦅)! The eagle swoops onto the course!")

class SummonAlbatross(MergedModificationEffect):
    emoji="🦢"
    description_secondhalf="an albatross might swoop onto the course"
    def apply_effect(self, glolfer, current_glolfer_action):
        self.game.objects.append(FlyingAlbatross(self.game, glolfer))
        self.game.send_message(f"{glolfer.get_display_name()} attracted an Albatross (🦢)! The albatross swoops onto the course!")

class Sticky(MergedModificationEffect):
    # a bad one
    emoji="🍯"
    description_secondhalf="their club gets sticky, trapping balls"
    def apply_effect(self, glolfer, current_glolfer_action):
        if current_glolfer_action["action"] == "hit" and random.random() < 0.2:
            current_glolfer_action["action"] = "stuck"
            self.game.send_message(f"{glolfer.get_display_name()} swings... but the ball sticks to the club!")

class MoreWiggle(MergedModificationEffect):
    emoji="🪱"
    description_secondhalf="this glolfer becomes more Wiggly, helping them avoid things like Duels and eagles."
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "wiggle", 0.2)
        self.game.send_message(f"{glolfer.get_display_name()} became more Wiggly!")

class MoreChurly(MergedModificationEffect):
    emoji="🤺"
    description_secondhalf="this glolfer becomes Churlier, increasing offensive (🤺) actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "churliness", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} became Churlier!")

class MoreEarly(MergedModificationEffect):
    emoji="🤸"
    description_secondhalf="this glolfer becomes Earlier, increasing defensive (🤸) actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "earliness", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} became Earlier!")

class MoreTwirly(MergedModificationEffect):
    emoji="🩰"
    description_secondhalf="this glolfer becomes Twirlier, increasing acrobatic (🩰) actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "twirliness", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} became Twirlier!")

class Patched(MergedModificationEffect):
    emoji="🪡"
    description_secondhalf="this glolfer crochets, improving their Needlethreadableness and aim"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "needlethreadableness", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} Patched up their aim!")


class TimeDilation(MergedModificationEffect):
    emoji="🤸"
    description_secondhalf="this glolfer loses track of time, reducing their Earliness and defensive (🤸) actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        decrease_stlat_for_rest_of_game(glolfer.stlats, "earliness", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} lost track of time and became less Early!")

class Ironic(MergedModificationEffect):
    emoji="🦾"
    description_secondhalf="this glolfer does pushdowns to boost their Musclitude, increasing their ball-hitting power."
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "musclitude", 0.5)
        self.game.send_message(f"{glolfer.get_display_name()} stopped to do some pushups! Their Musclitude improved!")

class GravityLensed(MergedModificationEffect):
    emoji="📏"
    description_secondhalf="this glolfer measures local gravity to increase their Estimation, helping them judge distance"
    def apply_effect(self, glolfer, current_glolfer_action):
        increase_stlat_for_rest_of_game(glolfer.stlats, "estimation", 0.2)
        self.game.send_message(f"{glolfer.get_display_name()} put on some gravitational lenses! Their Estimation got better!")


class LoosenedGrip(MergedModificationEffect):
    emoji="💥"
    description_secondhalf="this glolfer might loosen their Grip, which has only a slight risk of cracking reality"
    def apply_effect(self, glolfer, current_glolfer_action):
        decrease_stlat_for_rest_of_game(glolfer.stlats, "finesse", 0.1)
        self.game.send_message(f"{glolfer.get_display_name()} loosened their Grip...")

class Overwhelmed(MergedModificationEffect):
    emoji="😩"
    description_secondhalf="this glolfer gets overwhelmed"
    def apply_effect(self, glolfer, current_glolfer_action):
        if current_glolfer_action["action"] in ("move", "hit"):
            current_glolfer_action["action"] = "stuck"
            self.game.send_message(f"{glolfer.get_display_name()} is too {random.choice(('fearful','tired','lonely','overwhelmed','overwhelmed','hollow'))} to move...")


available_triggers_list = (OnSand, OnWater, OnFirstBall, Envious, OnScore, NearOtherGlolfer, NearHole, BallScoresItself, InElectricWind, InMathematicalWind, InFlavoredWind, InScaryWind)
available_effects_list = (MoreMarbles, SummonEagle, SummonAlbatross, Sticky, 
MoreWiggle, MoreEarly, MoreTwirly, MoreChurly, Patched, TimeDilation, Ironic, GravityLensed, LoosenedGrip, Overwhelmed)

available_triggers = {cls.__name__: cls for cls in available_triggers_list}
available_effects = {cls.__name__: cls for cls in available_effects_list}

def choose_random_trigger_ID():
    return random.choice([x for x in available_triggers.keys()])

def choose_random_effect_ID():
    return random.choice([x for x in available_effects.keys()])
