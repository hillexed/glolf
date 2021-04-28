import random, uuid, math
from typing import NamedTuple

default_player_names = ("Meteor Heartfelt","Razor Defrost","Jasper Groove","Thalia Soliloque","Benedict Dicetower","Bingo Polaroid","Pumpernickel Fan","Baby Bop","Tantalus Chewed","Freddie Missouri")
    


def random_player_emoji(rng):
    humanoid = ["👶","👧","🧒","👦","👩","🧑","👨","👩‍🦱","🧑‍🦱","👨‍🦱","👩‍🦰","🧑‍🦰","👨‍🦰","👱‍♀️",
"👱","👱‍♂️","👩‍🦳","🧑‍🦳","👨‍🦳","👩‍🦲","🧑‍🦲","👨‍🦲","🧔","👵","🧓","👴","👲","👳‍♀️",
"👳","👳‍♂️","🧕","👮‍♀️","👮","👮‍♂️","👷‍♀️","👷","👷‍♂️","💂‍♀️","💂","💂‍♂️","🕵️‍♀️","🕵️",
"🕵️‍♂️","👩‍⚕️","🧑‍⚕️","👨‍⚕️","👩‍🌾","🧑‍🌾","👨‍🌾","👩‍🍳","🧑‍🍳","👨‍🍳","👩‍🎓","🧑‍🎓","👨‍🎓","👩‍🎤",
"🧑‍🎤","👨‍🎤","👩‍🏫","🧑‍🏫","👨‍🏫","👩‍🏭","🧑‍🏭","👨‍🏭","👩‍💻","🧑‍💻","👨‍💻","👩‍💼","🧑‍💼","👨‍💼",
"👩‍🔧","🧑‍🔧","👨‍🔧","👩‍🔬","🧑‍🔬","👨‍🔬","👩‍🎨","🧑‍🎨","👨‍🎨","👩‍🚒","🧑‍🚒","👨‍🚒","👩‍✈️","🧑‍✈️",
"👨‍✈️","👩‍🚀","🧑‍🚀","👨‍🚀","👩‍⚖️","🧑‍⚖️","👨‍⚖️","👰","🏋️","🤵","🤸","👸","🤴","🦸‍♀️","🦸",
"🦸‍♂️","🦹‍♀️","🦹","🦹‍♂️","🤶","🚴","🎅","🧙‍♀️","🧙","🧙‍♂️","🧝‍♀️","🧝","🧝‍♂️","🧛‍♀️","🧛",
"🧛‍♂️","🧟‍♀️","🧟","🧟‍♂️","🧞‍♀️","🧞","🧞‍♂️","🧜‍♀️","🧜","🧜‍♂️","🧚‍♀️","🧚","🧚‍♂️","👼","🤰",
"🤱","🙇‍♀️","🙇","🙇‍♂️","💁‍♀️","💁","💁‍♂️","🙅‍♀️","🙅","🙅‍♂️","🙆‍♀️","🙆","🙆‍♂️","🙋‍♀️","🙋",
"🙋‍♂️","🧏‍♀️","🧏","🧏‍♂️","🤦‍♀️","🤦","🤦‍♂️","🤷‍♀️","🤷","🤷‍♂️","🙎‍♀️","🙎","🙎‍♂️","🙍‍♀️","🙍",
"🙍‍♂️","💇‍♀️","💇","💇‍♂️","💆‍♀️","💆","💆‍♂️","🧖‍♀️","🧖","🧖‍♂️","💅","🤳","💃","🕺","🕴","👩‍🦽",
"🧑‍🦽","👨‍🦽","👩‍🦼","🧑‍🦼","👨‍🦼","🚶‍♀️","🚶","🚶‍♂️","👩‍🦯","🧑‍🦯","👨‍🦯","🧎‍♀️","🧎","🧎‍♂️","🏃‍♀️","🏃",
"🏃‍♂️","🧍‍♀️","🧍","🧍‍♂️","👭","🧑‍🤝‍🧑","👬","👫","👩‍❤️‍👩","💑","👨‍❤️‍👨","👩‍❤️‍👨","👩‍❤️‍💋‍👩","💏","👨‍❤️‍💋‍👨","👩‍❤️‍💋‍👨",
"👪","👨‍👩‍👦","👨‍👩‍👧","👨‍👩‍👧‍👦","👨‍👩‍👦‍👦","👨‍👩‍👧‍👧","👨‍👨‍👦","👨‍👨‍👧","👨‍👨‍👧‍👦","👨‍👨‍👦‍👦","👨‍👨‍👧‍👧","👩‍👩‍👦","👩‍👩‍👧","👩‍👩‍👧‍👦","👩‍👩‍👦‍👦","👩‍👩‍👧‍👧",
"👨‍👦","👨‍👦‍👦","👨‍👧","👨‍👧‍👦","👨‍👧‍👧","👩‍👦","👩‍👦‍👦","👩‍👧","👩‍👧‍👦","👩‍👧‍👧","🗣","👤","👥"]

    nonhumanoid=[
"🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯","🦁","🐮","🐷","🐽","🐸","🐵",
"🙈","🙉","🙊","🐒","🐔","🐧","🐦","🐤","🐣","🐥","🦆","🦅","🦉","🦇","🐺","🐗","🐴","🦄",
"🐝","🐛","🦋","🐌","🐞","🐜","🦟","🦗","🕷️","🦂","🐢","🐍","🦎","🦖","🦕","🐙","🦑","🦐",
"🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐊","🐅","🐆","🦓","🦍","🦧","🐘","🦛","🦏",
"🐪","🐫","🦒","🦘","🐃","🐂","🐄","🐎","🐖","🐏","🐑","🦙","🐐","🦌","🐕","🐩","🦮","🐕‍🦺",
"🐈","🐓","🦃","🦚","🦜","🦢","🦩","🕊️","🐇","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🐿","🦔",
"🐉","🐲","🪐","💫","🌪","🌈","📠","📺"]

    if rng.random() > 0.5:
        return rng.choice(humanoid)
    else:
        return rng.choice(nonhumanoid)

class PlayerStlats(NamedTuple):
    stance: str = "Incredibly boring"
    fav_tea: str = "Iced"
    nyoomability: float = 1.5           # movement speed

    # unused for now except for fun
    tofu: int = 4
    wiggle: int = 3
    ritualism: int = 2
    polkadottedness: int = 0

    # shot power stats
    musclitude: float = 1.0             # how hard you swing
    finesse: float = 1.0                # how consistent your shots are hit with power, higher = better
    estimation: int = 0

    # shot angle stats
    needlethreadableness: float = 0.8   # how well you thread the needle (multiplier for how much angle variance your shots have), lower = better
    left_handedness: float = 0.0        # how biased your shots are to the left or right. can go negative, 0 = best

class Player(NamedTuple):
    name: str
    id: str
    stlats: PlayerStlats 
    emoji:str = "🏌️"
    modifications:list = []

    def driving_rating(self): # "Driving": hitting, and driving a kart
        rating_number = (self.stlats.musclitude + self.stlats.finesse + self.stlats.tofu)*5/3
        return format_stlat_display(rating_number)

    def precision_rating(self):
        rating_number = self.stlats.needlethreadableness * 5 - abs(self.stlats.left_handedness)
        return format_stlat_display(rating_number)

    def aerodynamics_rating(self):
        rating_number = self.stlats.ritualism * 5 #unused for now, need more stlats
        return format_stlat_display(rating_number)

    def self_awareness_rating(self):
        rating_number = (self.stlats.wiggle + self.stlats.estimation) * 5/2 + self.stlats.polkadottedness * 5 #means nothing for now
        return format_stlat_display(rating_number)

    def modifications_string(self):
        if len(self.modifications) == 0:
            return ""
        else:
            return "**Modifications**:\n" + ", ".join(self.modifications)





def generate_random_player_from_name(name="Random Player", emoji="🏌️"):
    """
    Generate a completely random player.
    """

    seed = name.strip().title()

    rng = random.Random(seed)
    if seed:
        id_ = uuid.uuid3(uuid.NAMESPACE_X500, name=str(seed))
    else:
        id_ = uuid.uuid4()

    stlats = generate_random_stlats_from_name(name)

    if emoji is not None:
        emoji = random_player_emoji(rng)

    return Player(name=name, id=id_, stlats=stlats,emoji=emoji)
    


def generate_random_stlats_from_name(name="Random Player"):
    # Generate stlats for a player using their name
    name = name.strip().title() # case insensitive

    rng = random.Random(name) #seed with name

    return PlayerStlats(
        nyoomability = max(rng.gauss(0,0.3),1.4),
        tofu=           rng.random(), # unused
        wiggle=         rng.random(), # unused
        ritualism=   rng.random(), # unused
        musclitude=     rng.random(),
        finesse=        rng.random(),
        needlethreadableness=   rng.random(), 
        left_handedness=        rng.gauss(0,0.3), #how often shots are biased to the left or right of what you want
        stance= rng.choice(["Tricky","Flashy","Aggro","Tanky","Twitchy","Powerful","Wibble","Wobble","Reverse","Feint","Electric","Spicy ","Pomegranate ","Explosive","Cottagecore","Corecore","Hardcore","Softcore","Hand to Hand","Lefty","Pop-Punk","DPS","Repose"]),
        fav_tea= rng.choice(["Iced","Boba","White","Green","Oolong","Pu'erh","Chai","Milk","Neon","Sweet","Void","Tea? ","Caramel","Lightspeed","Time-traveling","Bloody","Black","Miso","Concrete","Hard-boiled egg","Hot Chocolate","Bubble"]),
        estimation= rng.random(),
    )



# Easter egg: polkadot has max stats
known_players = {
    "Polkadot Patterson": Player(name="Polkadot Patterson", id=1, stlats=PlayerStlats(
        stance="Squiddish",
        fav_tea= "Iced",
        nyoomability = 1.5,
        tofu=1, # unused
        wiggle=1, # unused
        ritualism=1, # unused
        musclitude=1,
        finesse=1,
        needlethreadableness=1,
        polkadottedness=1,  
        left_handedness= 0,
        estimation=1,),emoji="😅"),
    "Simulacrum": Player(name="Simulacrum", id=2,emoji="🐂",stlats=generate_random_stlats_from_name("Simulacrum"), modifications=["Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌","😈"]),
    "Solar Dies": Player(name="Solar Dies", id=3,emoji="🦞",stlats=generate_random_stlats_from_name("Solar Dies"), modifications=["Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌","😈","1️"]),
}
known_players["Alto"] = known_players["Polkadot Patterson"]

def get_player_from_name(name):
    # generate a player from their name with random stats
    # ...or if they're polkadot, return a maxed person
    if name.title() in known_players:
        return known_players[name.title()]
    else:
        return generate_random_player_from_name(name)

def format_stlat_display(starcount: float):
    num_stars = math.floor(starcount)
    return_string = "🌕" * num_stars
    remainder = starcount-num_stars
    if remainder > 0.75:
        return return_string + "🌖"
    elif remainder > 0.5:
        return return_string + "🌗"
    elif remainder > 0.25:
        return return_string + "🌘"
    else: #remainder <= 0.25
        return return_string

