from .modification import PlayerModification
from data.modification_halves import available_triggers, available_effects

# halves in data.modification_halves

class MergedModification(PlayerModification):
    display_in_mod_list = False # otherwise it would show up in parentheses all the time
    isDead = False
    type = "permanent"

    def __init__(self, game, attached_player, **mod_data_dict):
        super().__init__(game, attached_player)
        self.triggerID = mod_data_dict["triggerID"]
        self.effectID = mod_data_dict["effectID"]

        if self.triggerID not in available_triggers:
            raise ValueError(f"Creating a merged modification failed: {attached_player.name}'s data {mod_data_dict} doesn't contain a valid triggerID!")
        if self.effectID not in available_effects:
            raise ValueError(f"Creating a merged modification failed: {attached_player.name}'s data {mod_data_dict} doesn't contain a valid effectID!")
        self.trigger = available_triggers[self.triggerID](game, attached_player)
        self.effect = available_effects[self.effectID](game, attached_player)

        self.displayEmoji = self.trigger.emoji + self.effect.emoji
        self.description = f"{self.trigger.description_firsthalf}, {self.effect.description_secondhalf}."

    def on_glolfer_update(self, attached_player, current_glolfer_action):
        if self.trigger.should_trigger(attached_player, current_glolfer_action):
            self.effect.apply_effect(attached_player, current_glolfer_action)

    def on_score(self, scoring_player, ball, hole_position):
        self.trigger.on_score(scoring_player, ball, hole_position)

