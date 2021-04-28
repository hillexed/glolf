import random
import emoji

courses = [
#The Llawn
'''
        🕸️🕸️🟩🟩🟩🟩🟩🟩🟩🕸️🕸️
        🕸️🟩🟩🟩🟩🟩🟩🌻🌻🟩🕸️
        🟩🟩🟩🟩🟩🟩🟩🌻🌻🟩🟩
        🟩🟩🟩🟩🟩🟨🟩🟩🟩🟩🟩
        🟩🟩🟩🟩🟨🟨🟨🟩🟩🟩🟩
        🟩⛳🟩🟩🟨🟨🟨🟩🟩⛳🟩
        🟩🟩🟩🟩🟨🟨🟨🟩🟩🟩🟩
        🟩🟩🟩🟩🟩🟨🟩🟩🟩🟩🟩
        🟩🟩🌻🌻🟩🟩🟩🟩🟩🟩🟩
        🕸️🟩🌻🌻🟩🟩🟩🟩🟩🟩🕸️
        🕸️🕸️🟩🟩🟩🟩🟩🟩🟩🕸️🕸️
        '''
,
#2Fort, by davee
'''
:green_square::green_square::green_square::green_square::green_square::blue_square::blue_square::green_square::green_square::green_square::green_square:
:yellow_square::green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::golf::green_square:
:yellow_square::yellow_square::green_square::green_square::blue_square::blue_square::green_square::green_square::green_square::green_square::green_square:
:yellow_square::green_square::green_square::green_square::blue_square::blue_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::bridge_at_night::bridge_at_night::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::blue_square::blue_square::green_square::green_square::green_square::yellow_square::yellow_square::green_square:
:green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::yellow_square::yellow_square::yellow_square:
:green_square::green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::yellow_square::yellow_square:
:green_square::golf::green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::blue_square::blue_square::green_square::green_square::green_square:
''',
# fish pond by davee
'''
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::evergreen_tree::evergreen_tree::green_square::green_square:
:green_square::green_square::green_square::golf::green_square::green_square::green_square::green_square::evergreen_tree::evergreen_tree::green_square:
:green_square::yellow_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:yellow_square::yellow_square::yellow_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:yellow_square::yellow_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::blue_square::green_square::green_square:
:green_square::green_square::evergreen_tree::evergreen_tree::green_square::green_square::green_square::blue_square::fish::blue_square::green_square:
:green_square::evergreen_tree::evergreen_tree::green_square::green_square::green_square::green_square::green_square::blue_square::blue_square::green_square:
:green_square::evergreen_tree::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::golf::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
''',

'''
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::blue_square:
:white_large_square::evergreen_tree::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::blue_square::blue_square::blue_square:
:white_large_square::evergreen_tree::evergreen_tree::white_large_square::white_large_square::golf::white_large_square::white_large_square::blue_square::blue_square::blue_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::blue_square::blue_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::evergreen_tree::christmas_tree::evergreen_tree::white_large_square::white_large_square::white_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:blue_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:blue_square::blue_square::blue_square::white_large_square::white_large_square::golf::white_large_square::white_large_square::evergreen_tree::evergreen_tree::white_large_square:
:blue_square::blue_square::blue_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::evergreen_tree::white_large_square:
:blue_square::blue_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
''',
# glolf in SPACE by hal 2000
'''
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
:milky_way::golf::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::star::milky_way::milky_way:
:milky_way::milky_way::milky_way::star::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
:milky_way::milky_way::star::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::earth_americas::milky_way::milky_way::full_moon::milky_way::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::star::milky_way::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::star::milky_way::milky_way::milky_way:
:milky_way::milky_way::star::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::golf::milky_way:
:milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way::milky_way:
''',
# day at the park by cabbage
''':green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::tulip:
:green_square::green_square::yellow_square::green_square::green_square::golf::green_square::green_square::green_square::rose::rose:
:green_square::yellow_square::yellow_square::yellow_square::green_square::green_square::green_square::green_square::green_square::green_square::tulip: 
:green_square::green_square::yellow_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:rose::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:rose::tulip::blue_square::blue_square::blue_square::bridge_at_night::bridge_at_night::blue_square::blue_square::green_square::green_square:
:blue_square::blue_square::blue_square::green_square::green_square::green_square::green_square::green_square::blue_square::blue_square::blue_square: 
:blue_square::blue_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::blue_square::swan:
:blue_square::blue_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::blue_square: 
:duck::blue_square::golf::green_square::green_square::green_square::green_square::green_square::yellow_square::yellow_square::green_square:
:blue_square::blue_square::green_square::green_square::green_square::green_square::green_square::yellow_square::yellow_square::yellow_square::yellow_square:
''',
# desert by davee
'''
:yellow_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::cactus::yellow_square::yellow_square::yellow_square:
:yellow_square::blue_square::yellow_square::yellow_square::cactus::yellow_square::yellow_square::yellow_square::yellow_square::golf::yellow_square:
:yellow_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:
:yellow_square::yellow_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:
:yellow_square::yellow_square::yellow_square::blue_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:
:cactus::yellow_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square:
:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::yellow_square::cactus::yellow_square:
:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::cactus::yellow_square::blue_square::yellow_square::yellow_square::yellow_square:
:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::yellow_square::yellow_square:
:yellow_square::golf::yellow_square::yellow_square::yellow_square::yellow_square::cactus::yellow_square::blue_square::blue_square::blue_square:
:yellow_square::yellow_square::yellow_square::cactus::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square:
''',
#whirlpool by cheshirecat
'''
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::golf::green_square::green_square::green_square::green_square::green_square::green_square::green_square::evergreen_tree::green_square:
:green_square::green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::blue_square::blue_square::blue_square::blue_square::blue_square::green_square::green_square::green_square:
:green_square::green_square::blue_square::blue_square::blue_square::ocean::blue_square::blue_square::blue_square::green_square::green_square:
:green_square::green_square::blue_square::blue_square::ocean::black_circle::ocean::blue_square::blue_square::green_square::green_square:
:green_square::green_square::blue_square::blue_square::blue_square::ocean::blue_square::blue_square::blue_square::green_square::green_square:
:green_square::green_square::green_square::blue_square::blue_square::blue_square::blue_square::blue_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::blue_square::blue_square::blue_square::green_square::green_square::green_square::green_square:
:green_square::evergreen_tree::green_square::green_square::green_square::green_square::green_square::green_square::green_square::golf::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
''',
# park by syl
# it would be cool if the terrain could move and the cars could travel down the street as hazards
'''
:office::office::office::office::office::office::office::office::office::office:
:office::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::office:
:office::green_square::green_square::green_square::green_square::green_square::deciduous_tree::green_square::green_square::office:
:office::green_square::green_square::green_square::deciduous_tree::deciduous_tree::green_square::green_square::green_square::office:
:office::green_square:⛳️:deciduous_tree::green_square::green_square::green_square::green_square::green_square::office:
:office::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::office:
:red_car::blue_car::taxi::blue_car:⬛️:red_car::red_car::taxi::taxi::police_car:
:office::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::office:
:office::green_square::green_square::green_square::deciduous_tree::deciduous_tree::green_square::green_square::green_square::office:
:office::green_square::green_square::deciduous_tree::green_square::green_square::green_square::green_square::green_square::office:
:office::green_square::deciduous_tree::green_square::green_square::green_square::deciduous_tree::green_square::green_square::office:
:office::green_square::deciduous_tree::green_square::green_square::green_square::deciduous_tree::green_square::green_square::office:
:office::green_square::deciduous_tree::green_square:⛳️:green_square::deciduous_tree::green_square::green_square::office:
:office::green_square::green_square::deciduous_tree::deciduous_tree::deciduous_tree::green_square::green_square::green_square::office:
:office::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::office:
:office::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::office:
:office::office::office::office::office::office::office::office::office::office:
''',
# chleckers by syl
'''
⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⛳️⬜️⬜️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️
⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️
⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬜️⬜️⛳️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️
⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️
''',
# loss by astro
'''
:blue_square::black_large_square::blue_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::blue_square:
:blue_square::black_large_square::golf::blue_square::black_large_square::blue_square::black_large_square::blue_square::black_large_square:
:blue_square::black_large_square::blue_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::black_large_square:
:blue_square::black_large_square::blue_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::blue_square:
:black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::blue_square:
:black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::golf::black_large_square::black_large_square:
:black_large_square::blue_square::black_large_square::blue_square::black_large_square::blue_square::blue_square::blue_square::blue_square:
''',
# hades tiger pit by syl
'''
:fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:
:black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::fire::orange_square::black_large_square::orange_square:
:black_large_square::orange_square::fire::orange_square::black_large_square::orange_square::golf::fire::black_large_square::orange_square::tiger2::orange_square:
:black_large_square::orange_square::black_large_square::orange_square::black_large_square::fire::black_large_square::orange_square::black_large_square::fire::black_large_square::orange_square:
:black_large_square::orange_square::tiger2::fire::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::fire::orange_square:
:black_large_square::orange_square::black_large_square::orange_square::black_large_square::fire::black_large_square::fire::black_large_square::orange_square::black_large_square::orange_square:
:black_large_square::fire::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::fire::black_large_square::fire:
:black_large_square::orange_square::black_large_square::orange_square::tiger2::orange_square::black_large_square::fire::black_large_square::orange_square::black_large_square::orange_square:
:black_large_square::orange_square::black_large_square::fire::black_large_square::orange_square::black_large_square::fire::black_large_square::orange_square::black_large_square::orange_square:
:black_large_square::orange_square::black_large_square::orange_square::black_large_square::fire::golf::orange_square::black_large_square::orange_square::tiger2::orange_square:
:black_large_square::fire::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::fire::orange_square::black_large_square::orange_square:
:fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:
''',
# dale by hal 2000
'''
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::yellow_square::golf::yellow_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::tada::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::speedboat::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::yellow_square::golf::yellow_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::blue_square::blue_square::blue_square:
''',
# MOUTH by loading
'''
:red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square:
:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
:black_large_square::golf::black_large_square::black_large_square::red_square::red_square::red_square::black_large_square::black_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::red_square::black_large_square::black_large_square::black_large_square::golf::black_large_square:
:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
:red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square:
''',
# foggy road by davee
'''
:fog::black_large_square::fog::fog::fog::fog::fog::fog::fog::fog::fog:
:fog::black_large_square::black_large_square::fog:⛳️:fog::fog::fog::fog::fog::fog:
:fog::fog::black_large_square::black_large_square::fog::fog::fog::fog::fog::fog::black_large_square:
:fog::fog::fog::black_large_square::black_large_square::fog::fog::fog::fog::black_large_square::black_large_square:
:fog::fog::fog::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::fog:
:fog::fog::fog::fog::black_large_square::black_large_square::black_large_square::black_large_square::fog::fog::fog:
:fog::fog::fog::fog::black_large_square::black_large_square::black_large_square::fog::fog::fog::fog:
:fog::fog::fog::fog::black_large_square::black_large_square::fog::fog::fog::fog::fog:
:fog::fog::fog::black_large_square::black_large_square::black_large_square::fog::fog::fog::fog::fog:
:fog::fog::fog::black_large_square::black_large_square::fog::fog:⛳️:fog::fog::fog:
:fog::fog::black_large_square::black_large_square::fog::fog::fog::fog::fog::fog::fog:
''',
# highway by zickery
'''
:city_sunset::city_dusk::city_dusk::city_dusk::cityscape::cityscape::cityscape::cityscape::cityscape::city_dusk::city_dusk::city_dusk::night_with_stars:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::golf::white_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::blue_car::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:truck::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::motorcycle::black_large_square:
:yellow_square::yellow_square::black_large_square::black_large_square::black_large_square::yellow_square::yellow_square::yellow_square::black_large_square::black_large_square::black_large_square::yellow_square::yellow_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::bus::black_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::race_car::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:white_large_square::golf::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::red_car::police_car::black_large_square::black_large_square::black_large_square::black_large_square:
''',
# gearball by octagenerian redpenguin
'''
:gear::gear::gear::gear::brown_square::orange_square::brown_square::gear::gear::gear::gear:
:gear::orange_square::orange_square::red_square::orange_square::orange_square::orange_square::red_square::orange_square::orange_square::gear:
:gear::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::gear:
:gear::red_square::golf::orange_square::white_large_square::red_square::white_large_square::orange_square::orange_square::red_square::gear:
:brown_square::orange_square::orange_square::white_large_square::red_square::red_square::white_large_square::white_large_square::orange_square::orange_square::brown_square:
:orange_square::orange_square::orange_square::red_square::red_square::white_large_square::red_square::red_square::orange_square::orange_square::orange_square:
:brown_square::orange_square::orange_square::white_large_square::white_large_square::red_square::red_square::white_large_square::orange_square::orange_square::brown_square:
:gear::red_square::orange_square::orange_square::white_large_square::red_square::white_large_square::orange_square::golf::red_square::gear:
:gear::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::gear:
:gear::orange_square::orange_square::red_square::orange_square::orange_square::orange_square::red_square::orange_square::orange_square::gear:
:gear::gear::gear::gear::brown_square::orange_square::brown_square::gear::gear::gear::gear:
''',
# atlantis by zickery
'''
:ocean::ocean::ocean::ocean::ocean:
:blue_square::blue_square::arrow_double_down::blue_square::blue_square:
:fish::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::fish:
:blue_square::blue_square::fish::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::fish::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::fish::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square:
:golf::blue_square::blue_square::blue_square::golf:
:blue_square::blue_square::blue_square::blue_square::blue_square:
:night_with_stars::night_with_stars::night_with_stars::night_with_stars::night_with_stars:
''',
# the taqueria by syl
'''

:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::taco::green_square::green_square::green_square::green_square::green_square:⛳️:green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::yellow_square::yellow_square::yellow_square::yellow_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::green_square::green_square::green_square:
:green_square::green_square::green_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square:⛳️:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
''',

# san fran lovers by syl
'''
:heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:black_large_square::golf::red_square::red_square::red_square::black_large_square::black_large_square::red_square::red_square::red_square::black_large_square::black_large_square:
:black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::black_large_square::black_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::black_large_square::black_large_square::black_large_square::golf::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:
:heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart:
''',
# link by davee
'''
:spider_web::spider_web::spider_web::spider_web::green_square::green_square::green_square::green_square::spider_web::spider_web::spider_web:
:spider_web::purple_square::spider_web::green_square::green_square::green_square::green_square::green_square::green_square::spider_web::spider_web:
:spider_web::purple_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::spider_web:
:spider_web::purple_square::green_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::green_square::green_square::spider_web:
:spider_web::purple_square::golf::yellow_square::blue_square::yellow_square::blue_square::white_large_square::yellow_square::white_large_square::spider_web:
:spider_web::purple_square::green_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::green_square::spider_web:
:purple_square::purple_square::purple_square::green_square::white_large_square::white_large_square::brown_square::brown_square::brown_square::brown_square::brown_square:
:spider_web::white_large_square::green_square::green_square::green_square::green_square::brown_square::brown_square::orange_square::brown_square::brown_square:
:spider_web::white_large_square::green_square::green_square::green_square::green_square::brown_square::orange_square::golf::orange_square::brown_square:
:spider_web::spider_web::spider_web::brown_square::brown_square::yellow_square::brown_square::brown_square::orange_square::brown_square::brown_square:
:spider_web::spider_web::spider_web::green_square::green_square::green_square::green_square::brown_square::brown_square::brown_square::spider_web:
:spider_web::spider_web::spider_web::white_large_square::white_large_square::spider_web::white_large_square::white_large_square::brown_square::spider_web::spider_web:
''',
#cursed madeleine by syl
'''
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::red_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::red_square::white_large_square::golf::white_large_square::golf::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::red_square::red_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::brown_square::white_large_square::white_large_square::white_large_square::black_large_square::red_square::black_large_square:
:black_large_square::black_large_square::brown_square::brown_square::brown_square::brown_square::blue_square::blue_square::brown_square::brown_square::black_large_square::black_large_square::black_large_square:
:black_large_square::black_large_square::brown_square::brown_square::brown_square::blue_square::brown_square::blue_square::blue_square::blue_square::brown_square::black_large_square::black_large_square:
:black_large_square::black_large_square::brown_square::brown_square::blue_square::blue_square::white_large_square::white_large_square::blue_square::blue_square::white_large_square::white_large_square::black_large_square:
:black_large_square::black_large_square::brown_square::brown_square::brown_square::blue_square::white_large_square::white_large_square::blue_square::blue_square::white_large_square::white_large_square::black_large_square:
:black_large_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::black_large_square::black_large_square:
:black_large_square::brown_square::brown_square::brown_square::blue_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::brown_square::black_large_square::black_large_square::brown_square::brown_square::black_large_square::black_large_square:
:black_large_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::black_large_square::black_large_square:
''',
# wrong splort by zickery (it's a baseball diamond)
'''
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::golf::green_square::green_square:
:green_square::green_square::green_square::green_square::orange_square::orange_square::orange_square::green_square::green_square::green_square::green_square::green_square:
:green_square::green_square::green_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::green_square::green_square:
:green_square::green_square::orange_square::orange_square::black_square_button::orange_square::orange_square::orange_square::orange_square::orange_square::black_square_button::green_square:
:green_square::green_square::orange_square::orange_square::orange_square::orange_square::green_square::green_square::green_square::orange_square::orange_square::green_square:
:green_square::green_square::orange_square::orange_square::orange_square::green_square::green_square::green_square::green_square::green_square::orange_square::green_square:
:green_square::green_square::green_square::orange_square::orange_square::green_square::green_square::black_square_button::green_square::green_square::orange_square::green_square:
:green_square::green_square::green_square::orange_square::orange_square::green_square::green_square::green_square::green_square::green_square::orange_square::green_square:
:green_square::golf::green_square::orange_square::orange_square::orange_square::green_square::green_square::green_square::orange_square::orange_square::orange_square:
:green_square::green_square::green_square::green_square::black_square_button::orange_square::orange_square::orange_square::orange_square::orange_square::black_square_button::orange_square:
:green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::orange_square::orange_square::orange_square:
''',
#munich's the scream by loading
'''
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::green_square:
:blue_square::blue_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::golf::green_square:
:blue_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square::green_square::green_square:
:blue_square::blue_square::orange_square::yellow_square::white_square_button::yellow_square::white_square_button::yellow_square::orange_square::green_square::green_square:
:blue_square::blue_square::orange_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::orange_square::green_square::green_square:
:brown_square::blue_square::orange_square::orange_square::yellow_square::black_large_square::yellow_square::orange_square::orange_square::green_square::green_square:
:brown_square::brown_square::blue_square::orange_square::yellow_square::black_large_square::yellow_square::orange_square::blue_square::green_square::green_square:
:blue_square::brown_square::brown_square::orange_square::yellow_square::yellow_square::yellow_square::orange_square::blue_square::green_square::green_square:
:blue_square::golf::brown_square::brown_square::orange_square::yellow_square::orange_square::brown_square::blue_square::blue_square::green_square:
:blue_square::blue_square::blue_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::blue_square:
''',
# house by hal 2000
'''
:white_large_square::white_large_square::white_large_square::window::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::window::white_large_square::white_large_square:
:white_large_square::brown_square::brown_square::brown_square::brown_square::white_large_square::brown_square::brown_square::brown_square::brown_square::brown_square::white_large_square:
:window::brown_square::golf::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::chair::desktop::white_large_square:
:white_large_square::brown_square::brown_square::brown_square::brown_square::brown_square::white_large_square::printer::brown_square::brown_square::brown_square::white_large_square:
:white_large_square::white_large_square::white_large_square::brown_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::brown_square::white_large_square::white_large_square:
:door::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::white_large_square::white_large_square:
:door::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::sunflower::white_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::brown_square::brown_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:white_large_square::brown_square::frame_photo::brown_square::brown_square::brown_square::brown_square::white_large_square::brown_square::toilet::roll_of_paper::white_large_square:
:window::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::window:
:white_large_square::alarm_clock::brown_square::brown_square::brown_square::brown_square::brown_square::white_large_square::brown_square::golf::brown_square::white_large_square:
:white_large_square::bed::brown_square::brown_square::brown_square::couch::brown_square::white_large_square::brown_square::brown_square::bathtub::white_large_square:
:white_large_square::white_large_square::white_large_square::window::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::window::white_large_square::white_large_square:
'''

]
# to do: give each course a name


special_case_emojis = { #these are emojis which aren't converted to unicode by emojize() so I need to do it manually
":golf:":"⛳",
":city_dusk:":"🌆",
":race_car:":"🏎️",
":frame_photo:":"🖼️",
":desktop:":"🖥️",
":couch:":"🛋️",
":gear:":"⚙️",
"⚙":"⚙️", # emojize converts :gear: to this tiny non-fullwidth thing (it's the same character, but missing a variation selector)
}


def discord_to_unicode_convert(coursedata):
    course = emoji.emojize(coursedata,use_aliases=True)
    for special_case_emoji in special_case_emojis:
        course = course.replace(special_case_emoji, special_case_emojis[special_case_emoji])
    
    return course

def get_random_course():
    return discord_to_unicode_convert(random.choice(courses))


def verify_courses():
    unconverted_emoji = []
    for coursedata in courses:
        course = discord_to_unicode_convert(coursedata)
        print(course)
        if ":" in course:
            start = course.index(":")
            end = course.index(":",start+1)
            unconverted_emoji.append(course[start:end+1])

    if len(unconverted_emoji) > 0:
        print("!!!! WARNING: UNCONVERTED EMOJI STILL REMAIN!!!!")
        print([x for x in unconverted_emoji])
        raise ValueError



if __name__ == "__main__":
    verify_courses()
