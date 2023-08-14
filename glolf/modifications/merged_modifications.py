from .modification import PlayerModification
from .modification_halves import available_triggers, available_effects

def merge_descriptions(triggerclass, effectclass):

    last_punctuation = "."

    secondhalf = effectclass.description_secondhalf
    if secondhalf[-1] in (".", "!"):
        last_punctuation = "" # don't add an extra period if it's not needed

    return f"{triggerclass.description_firsthalf}, {effectclass.description_secondhalf}{last_punctuation}"

def merge_emojis(triggerclass, effectclass):
    return f"{triggerclass.emoji}+{effectclass.emoji}"

class MergedModification(PlayerModification):
    display_in_mod_list = False # otherwise it would show up in parentheses all the time
    isDead = False
    type = "permanent"

    def __init__(self, game, attached_player, **mod_data_dict):
        super().__init__(game, attached_player)
        self.trigger_ID = mod_data_dict["trigger_ID"]
        self.effect_ID = mod_data_dict["effect_ID"]

        if self.trigger_ID not in available_triggers:
            raise ValueError(f"Creating a merged modification failed: {attached_player.name}'s data {mod_data_dict} doesn't contain a valid trigger_ID!")
        if self.effect_ID not in available_effects:
            raise ValueError(f"Creating a merged modification failed: {attached_player.name}'s data {mod_data_dict} doesn't contain a valid effect_ID!")
        self.trigger = available_triggers[self.trigger_ID](game, attached_player)
        self.effect = available_effects[self.effect_ID](game, attached_player)

        self.description = merge_descriptions(self.trigger, self.effect)
        self.displayEmoji = merge_emojis(self.trigger, self.effect)

    def on_glolfer_update(self, attached_player, current_glolfer_action):
        if self.trigger.should_trigger(attached_player, current_glolfer_action):
            self.effect.apply_effect(attached_player, current_glolfer_action)

    def on_score(self, scoring_player, ball, hole_position):
        self.trigger.on_score(scoring_player, ball, hole_position)
