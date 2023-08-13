from courses import WATER_TILES
from entities.eagleentities import FlyingEagle, FlyingAlbatross


class MergedModificationTrigger:
    emoji="?"
    description_firsthalf = "when something mysterious happens"

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
        for tile in trigger_tiles:
            if self.game.course.get_tile_at(glolfer.coordinates) == tile:
                return True
        return False

class TriggerInWind(MergedModificationTrigger):
    # todo
    emoji="🌬️"
    wind_types = (None)

    @randomly_trigger(0.02)
    def should_trigger(self, glolfer, current_glolfer_action):
        if game.wind in self.wind_types:
                return True
        return False


class TriggerNearEntity(MergedModificationTrigger):
    # todo
    emoji=" "
    entity_type=None
    distance_to_trigger=3

    @randomly_trigger(0.3)
    def should_trigger(self, glolfer, current_glolfer_action):
        closest_object = self.game.get_closest_object_to_position(glolfer, object_type=self.entity_type)
        dist = (closest_object.position-glolfer.position).norm()

        if dist < distance_to_trigger:
                return True
        return False



# triggers

class OnSand(TriggerOnATile):
    emoji = "🟨"
    trigger_tiles=["🟨"]
    description_firsthalf="On sand hazards 🟨"

class OnWater(TriggerOnATile):
    emoji="🟦"
    trigger_tiles = WATER_TILES
    description_firsthalf="On water 🟦"

class OnFirstBall:
    emoji="⚪"
    description_firsthalf = "The first time they score"
    def should_trigger(self, glolfer, current_glolfer_action):
        if self.activated:
            return True
            self.activated = False
        return False

    def on_score(self, scoring_player, ball, hole_position):
        # todo: add __init__
        if self.attached_glolfer == scoring_player and self.game.scores[scoring_player].balls_scored == 1:
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
    description_secondhalf="this glolfer gets more Marbles"
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.marbles += 1
        self.game.send_message(f"{glolfer.get_display_name()} picked up an extra Marble!")

class SummonEagle(MergedModificationEffect):
    emoji="🦅"
    description_secondhalf="an eagle might swoop onto the course"
    def apply_effect(self, glolfer, current_glolfer_action):
        game.objects.append(FlyingEagle(glolfer))
        self.game.send_message(f"{glolfer.get_display_name()} attracted an Eagle! The eagle swoops onto the course!")

class SummonAlbatross(MergedModificationEffect):
    emoji="🦢"
    description_secondhalf="an albatross might swoop onto the course"
    def apply_effect(self, glolfer, current_glolfer_action):
        self.game.objects.append(FlyingAlbatross(glolfer))
        self.game.send_message(f"{glolfer.get_display_name()} attracted an Albatross! The albatross swoops onto the course!")

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
        glolfer.stlats.wiggle += 0.2
        self.game.send_message(f"{glolfer.get_display_name()} became more Wiggly!")

class MoreChurly(MergedModificationEffect):
    emoji="🤺"
    description_secondhalf="this glolfer becomes Churlier, increasing 🤺 actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.churliness += 0.5
        self.game.send_message(f"{glolfer.get_display_name()} became Churlier!")

class MoreEarly(MergedModificationEffect):
    emoji="🤸"
    description_secondhalf="this glolfer becomes Earlier, increasing 🤸 actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.earliness += 0.5
        self.game.send_message(f"{glolfer.get_display_name()} became Earlier!")

class MoreTwirly(MergedModificationEffect):
    emoji="🩰"
    description_secondhalf="this glolfer becomes Twirlier, increasing 🩰 actions during Duels"
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.twirliness += 0.5
        self.game.send_message(f"{glolfer.get_display_name()} became Twirlier!")

class Patched(MergedModificationEffect):
    emoji="🪡"
    description_secondhalf="this glolfer crochets, improving their Needlethreadableness and aim."
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.needlethreadableness += 0.4
        self.game.send_message(f"{glolfer.get_display_name()} Patched up their aim!")


class TimeDilation(MergedModificationEffect):
    emoji="🤸"
    description_secondhalf="loses track of time and Earliness, reducing 🤸 actions during Duels."
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.earliness -= 0.5
        if glolfer.stlats.earliness <= 0.0:
            glolfer.stlats.earliness = 0
        self.game.send_message(f"{glolfer.get_display_name()} lost track of time and became less Early!")

class Ironic(MergedModificationEffect):
    emoji="🦾"
    description_secondhalf="boosts this glolfer's Musclitude, increasing their hit power."
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.musclitude += 0.2
        self.game.send_message(f"{glolfer.get_display_name()} ironed out their Musclitude!")

class GravityLensed(MergedModificationEffect):
    emoji="📏"
    description_secondhalf="boosts this glolfer's Estimation, helping them judge distance."
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.musclitude += 0.2
        self.game.send_message(f"{glolfer.get_display_name()} put on some gravitational lenses! Their Estimation got better!")


class LoosenedGrip(MergedModificationEffect):
    emoji="💥"
    description_secondhalf="this glolfer might loosen their Grip, which has only a slight risk of cracking reality"
    def apply_effect(self, glolfer, current_glolfer_action):
        glolfer.stlats.finesse -= 0.1
        if glolfer.stlats.finesse <= 0.1:
            glolfer.stlats.finesse = 0.1
        self.game.send_message(f"{glolfer.get_display_name()} loosened their Grip...")

class Overwhelmed(MergedModificationEffect):
    emoji="😩"
    description_secondhalf="this glolfer gets overwhelmed"
    def apply_effect(self, glolfer, current_glolfer_action):
        if current_glolfer_action["action"] == "move":
            current_glolfer_action["action"] = "stuck"
            self.game.send_message(f"{glolfer.get_display_name()} is too {random.choice(('fearful','tired','lonely','overwhelmed','overwhelmed','hollow'))} to move...")


available_triggers_list = (OnSand, OnWater, OnFirstBall, InElectricWind, InMathematicalWind, InFlavoredWind, InScaryWind)
available_effects_list = (MoreMarbles, SummonEagle, SummonAlbatross, Sticky, 
MoreWiggle, MoreEarly, MoreTwirly, MoreChurly, Patched, TimeDilation, Ironic, GravityLensed, LoosenedGrip, Overwhelmed)

available_triggers = {cls.__name__: cls for cls in available_triggers_list}
available_effects = {cls.__name__: cls for cls in available_effects_list}

def choose_random_trigger_ID():
    return random.choice(available_triggers.keys())

def choose_random_effect_ID():
    return random.choice(available_effects.keys())
