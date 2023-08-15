import game
from clubs.clubgame import ClubGame

from modifications.create_mods_from_saved_data import MergedModificationDataTemplate
from modifications.modification_halves import available_triggers, available_effects
import data.players

from inventory import generate_random_trigger, generate_random_effect, merge

glolfgame = game.SingleHole()
#glolfgame = ClubGame(club_names=['a','b']) # won't work unless a and b are in the DB as created clubs
glolfgame.send_message = print


def verify_cosmetic_mod():
    championshipJacket = CosmeticModificationData(emojis="🧥", name="Championship Jacket", description="Bestowed Upon Glolfers Who Win an Internet Open")
    assert "type" in championshipJacket

def verify_mod_halves_descriptions():
    for mod in available_triggers:
        first_letter = mod.description_firsthalf[0]
        assert first_letter.upper() == first_letter
        assert mod.emoji != "?"

    for mod in available_effects:
        last_letter = mod.description_secondhalf[-1]
        assert last_letter != "."
        assert mod.emoji != "?"

def merge_mod_data():
    trigger_ID = random.choice([x for x in available_triggers.keys()])
    effect_ID = random.choice([x for x in available_effects.keys()])

    trigger = available_triggers[trigger_ID]
    effect = available_effects[effect_ID]
    
    merged_mod_data = MergedModificationDataTemplate(name="Joint Stock Venture", description=merge_descriptions(trigger, effect), emojis=merge_emojis(trigger, effect), trigger_ID=trigger_ID, effect_ID = effect_ID)
    return merge_mod_data


def verify_serialization():

    from data.saved_mod_data import championshipJacket

    mod = championshipJacket
    cosmetic_dict = mod.to_dict()
    mod2 = create_mod_from_saved_data(cosmetic_dict)
    assert mod.to_dict() == mod2.to_dict()



def testgame():
    i = 0
    while not glolfgame.over:
        print(f"####### Turn {i}:")
        print(glolfgame.printgamestate())
        glolfgame.update()
        i += 1
        if i > 1000:
            raise ValueError("Game went on too long!")
    print(glolfgame.printgamestate())



def test_many_mods():
    tester1 = "a"
    tester2 = "b"

    #todo: clear modifications
    data.players.regenerate_player(tester1)
    data.players.regenerate_player(tester2)

    for i in range(30):
        # note: the more you run this, the m
        mod = merge(generate_random_trigger(), generate_random_effect())
        data.players.add_permanent_modification_to_player(tester1, mod)
        data.players.add_permanent_modification_to_player(tester2, mod)

    for i in range(50):
        glolfgame = game.SingleHole(glolfer_names=[tester1,tester2])
        while not glolfgame.over:
            print(f"####### Turn {i}:")
            print(glolfgame.printgamestate())
            glolfgame.update()
            i += 1
            if i > 1000:
                raise ValueError("Game went on too long!")
        print(glolfgame.printgamestate())


test_many_mods()
