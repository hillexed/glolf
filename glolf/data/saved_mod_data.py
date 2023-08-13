from typing import TypedDict

class SavedModificationDataTemplate(TypedDict):
    type = "cosmetic"
    emojis = ""
    name="Default Modificatoin"
    description="does nothing"

class CosmeticModificationData(TypedDict):
    type = "cosmetic"


class MergedModificationDataTemplate(SavedModificationDataTemplate):
    type = "cosmetic"
    emojis = ""
    name="Default Modificatoin"
    description="does nothing"

    triggerID:str
    effectID:str


championshipJacket = CosmeticModificationData(emojis="🧥", name="Championship Jacket", description="Bestowed Upon Glolfers Who Win an Internet Open")
voidTrapped = CosmeticModificationData(emojis="😵‍💫", name="Void-Trapped", description="help me")

spookyGrandUnchipMod = CosmeticModificationData(emojis="😈", name="Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌", description="Long ago, this glolfer got Out.")
foxFriendship = CosmeticModificationData(emojis="🤝💖", name="Accepted Friendship", description="A promise not be a good friend and not cause another Afoxalypse")
buff = CosmeticModificationData(emojis="💪", name="Buff", description="This glolfer is buff")
nutrisocks = CosmeticModificationData(emojis="🧦", name="Sponsored by Nutrisocks", description="Nutrition, for your Sole.")

