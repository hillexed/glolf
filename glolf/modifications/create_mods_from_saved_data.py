from .modification import PlayerModification
from .merged_modifications import MergedModification

from data.saved_mod_data import SavedModificationDataTemplate

class CosmeticModification(PlayerModification): #ingame version of cosmetic modification
    display_in_mod_list = False

    def __init__(self, game, attached_player, **mod_data_dict):
        super().__init__(game, attached_player)
        self.emoji = mod_data_dict["emoji"]

def create_ingame_mod_from_saved_data(game, attached_player, mod_data_dict: SavedModificationDataTemplate):
    print("Mod created")
    mod_type = mod_data_dict["type"]
    if mod_type == "cosmetic":
        return CosmeticModification(game, attached_player, **mod_data_dict)
    if mod_type == "merged":
        return MergedModification(game, attached_player, **mod_data_dict)

def test_serialization():
    from data.saved_mod_data import championshipJacket

    mod = championshipJacket
    cosmetic_dict = mod.to_dict()
    mod2 = create_mod_from_saved_data(cosmetic_dict)
    assert mod.to_dict() == mod2.to_dict()

def test_merges():
    
    mod = create_ingame_mod_from_saved_data(None, None, {"triggerID": "OnSand", "effectID":"LoosenedGrip", "type": "merged"})


if __name__ == "__main__":
    test_serialization()
    test_merges()
