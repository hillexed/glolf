from collections import UserDict

# used in DB
class SavedModificationDataTemplate(UserDict):
    type = "cosmetic"
    emoji = ""
    name="Default Modification"
    description="Does nothing."

    required_fields = ("type", "emoji", "name", "description")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for field in self.required_fields:
            if field not in kwargs:
                self[field] = getattr(self, field)

    def to_dict(self):
        # convert player into a dict, for saving in the DB
        return self.data

class CosmeticModificationData(SavedModificationDataTemplate):
    type = "cosmetic"

class MergedModificationDataTemplate(SavedModificationDataTemplate):
    type = "merged"
    emoji = ""
    name="Default Modificatoin"
    description="does nothing"

    trigger_ID:str
    effect_ID:str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "type" not in kwargs:
            self["type"] = self.type
        if "trigger_ID" not in kwargs:
            raise TypeError
        if "effect_ID" not in kwargs:
            raise TypeError





championshipJacket = CosmeticModificationData(emoji="🧥", name="Championship Jacket", description="Bestowed Upon Glolfers Who Win an Internet Open")
voidTrapped = CosmeticModificationData(emoji="😵‍💫", name="Void-Trapped", description="help me")
spookyGrandUnchipMod = CosmeticModificationData(emoji="😈", name="Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌", description="Long ago, this glolfer got Out.")
foxFriendship = CosmeticModificationData(emoji="🤝💖", name="Accepted Friendship", description="A promise to be a good friend and not cause another Afoxalypse")
buff = CosmeticModificationData(emoji="💪", name="Buff", description="This glolfer is buff")
nutrisocks = CosmeticModificationData(emoji="🧦", name="Sponsored by Nutrisocks", description="Nutrition, for your Sole.")
