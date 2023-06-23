from .swordfighting import SwordfightingDecree
from .eaglemod import EagleMaker
from .interesting_offscreen_thing import InterestingOffscreenThing

def get_permanent_modifiers(game):
    return [SwordfightingDecree(game), EagleMaker(game), InterestingOffscreenThing(game)]

descriptions = '''
:crossed_swords: : Glolfers on the same tile have a chance of Dueling, sending the loser flying into the glolf hole.*
:eagle: : Celebrate the unforgettable feeling of scoring under par! Scoring an Eagle or Albatross attracts an Eagle or Albatross. 
:eyes: : Sometimes Glolfers take interest in something weird they can see conveniently offscreen. * 

* This Unsponsored Content violates our Brand Guidelines. We apologize for the inconvenience. By reading this message you agree the IGA is not responsible for spontaneous and dangerously unsponsored glolfer conduct.
'''.strip()
