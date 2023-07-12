from .playerstlats import generate_player_from_name, Player, PlayerStlats
import db

default_player_names = ("Meteor Heartfelt","Razor Defrost","Jasper Groove","Thalia Soliloque","Benedict Dicetower","Bingo Polaroid","Pumpernickel Fan","Baby Bop","Tantalus Chewed","Freddie Missouri","Load Bearing Coconut", "Frankle Knives", "Spooks Mcgee", "Line Cook")

def get_player_from_name(name):
    # Get a player from the database.
    # if they're not there, generate a player from their name with random stats
    # or, if it's a known player, 
    playerdata = db.get_player_data(name)
    if playerdata is not None:
        try:
            return Player.from_dict(playerdata) # could error if playerdata has extra data that doesn't fit into stlats
        except TypeError as e:
            raise e
    return generate_player_from_name(name)

def is_player_in_db(name):
    # See whether a player is in the database.
    playerdata = db.get_player_data(name)
    if playerdata is not None:
        return True
    return False

def regenerate_player(name):
    # Delete a player if they're in the DB
    playerdata = db.get_player_data(name)
    if playerdata is not None:
        db.delete_player_data(name)
        return True
    return False

def add_permanent_modification_to_player(name, modification):
    #Adds a modification to a player. Also saves them in the DB.
    player = get_player_from_name(name)
    player.modifications.append(modification)
    save_playerdata(name, player)

def save_playerdata(name, player: Player):
    data = player.to_dict()
    playerdata = db.set_player_data(name, data)

def test_serialization():
    # test whether a player can be serialized and deserialized
    player = generate_player_from_name("1")
    print(player)
    data = player.to_dict()
    assert type(data) == dict
    player2 = Player.from_dict(data)

    assert type(player2.stlats) == PlayerStlats
    assert player.stlats == player2.stlats

    # player == player2 is False though :(
