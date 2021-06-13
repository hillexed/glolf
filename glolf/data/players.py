from .playerstlats import generate_player_from_name, PlayerStlats
import db

default_player_names = ("Meteor Heartfelt","Razor Defrost","Jasper Groove","Thalia Soliloque","Benedict Dicetower","Bingo Polaroid","Pumpernickel Fan","Baby Bop","Tantalus Chewed","Freddie Missouri","Load Bearing Coconut", "Frankle Knives", "Spooks Mcgee", "Line Cook")

def get_player_from_name(name):
    # Get a player from the database.
    # if they're not there, generate a player from their name with random stats
    # or, if it's a known player, 
    playerdata = db.get_player_data(name)
    if playerdata is not None:
        try:
            return PlayerStlats(**playerdata) # could error if playerdata has extra data that doesn't fit into stlats
        except TypeError as e:
            raise e
    return generate_player_from_name(name)
