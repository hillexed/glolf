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
# winter by hal 2000
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
⬛⬛⬛⬛:brown_square::orange_square::brown_square:⬛⬛⬛⬛
⬛:orange_square::orange_square::red_square::orange_square::orange_square::orange_square::red_square::orange_square::orange_square:⬛
⬛:orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square:⬛
⬛:red_square::golf::orange_square::white_large_square::red_square::white_large_square::orange_square::orange_square::red_square:⬛
:brown_square::orange_square::orange_square::white_large_square::red_square::red_square::white_large_square::white_large_square::orange_square::orange_square::brown_square:
:orange_square::orange_square::orange_square::red_square::red_square::white_large_square::red_square::red_square::orange_square::orange_square::orange_square:
:brown_square::orange_square::orange_square::white_large_square::white_large_square::red_square::red_square::white_large_square::orange_square::orange_square::brown_square:
⬛:red_square::orange_square::orange_square::white_large_square::red_square::white_large_square::orange_square::golf::red_square:⬛
⬛:orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square:⬛
⬛:orange_square::orange_square::red_square::orange_square::orange_square::orange_square::red_square::orange_square::orange_square:⬛
⬛⬛⬛⬛:brown_square::orange_square::brown_square:⬛⬛⬛⬛
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
''',
# mario 1-1 by syl
'''
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::question::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::golf::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::golf::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::question::blue_square::brown_square::question::brown_square::question::brown_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::green_square::green_square:
:blue_square::green_square::green_square::blue_square::frog::blue_square::blue_square::blue_square::green_square::green_square::blue_square::green_square::green_square:
:brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square:
''',

# boardwalk by lazaretto
'''
:sunrise_over_mountains:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:crab:﻿:ocean:﻿
﻿:yellow_square:﻿:beach_umbrella:﻿:golf:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:white_large_square:﻿:ocean:﻿
﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:white_large_square:﻿:ocean:﻿
﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:white_large_square:﻿:dolphin:﻿
﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:white_large_square:﻿:ocean:﻿
﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:golf:﻿:yellow_square:﻿:white_large_square:﻿:ocean:﻿
﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:yellow_square:﻿:beach_umbrella:﻿:white_large_square:﻿:ocean:
''',
# rift chasm by hal 2000
'''
:green_square::green_square::green_square::green_square::green_square::black_large_square::black_large_square::black_large_square::black_large_square::blue_square::blue_square::blue_square:
:green_square::green_square::green_square::green_square::black_large_square::boom::black_large_square::black_large_square::black_large_square::green_square::blue_square::blue_square:
:green_square::green_square::green_square::green_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::green_square::green_square::blue_square:
:green_square::green_square::green_square::green_square::black_large_square::black_large_square::black_large_square::boom::black_large_square::green_square::green_square::green_square:
:green_square::golf::green_square::green_square::brown_square::brown_square::brown_square::brown_square::brown_square::green_square::green_square::green_square:
:green_square::green_square::green_square::green_square::brown_square::brown_square::brown_square::brown_square::brown_square::green_square::golf::green_square:
:green_square::green_square::green_square::black_large_square::boom::black_large_square::black_large_square::black_large_square::green_square::green_square::green_square::green_square:
:blue_square::green_square::green_square::black_large_square::black_large_square::black_large_square::boom::black_large_square::mailbox_closed::green_square::green_square::green_square:
:blue_square::blue_square::green_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::brown_square::brown_square::brown_square::brown_square:
:blue_square::blue_square::blue_square::black_large_square::black_large_square::black_large_square::black_large_square::green_square::green_square::green_square::green_square::green_square:''',

# hades tiger pit by syl, revamped by hal
'''
:fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:
:tiger2::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::tiger2:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::golf::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:orange_square::black_large_square::orange_square::black_large_square::orange_square::golf::orange_square::black_large_square::orange_square::black_large_square::orange_square:
:tiger2::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::orange_square::black_large_square::tiger2:
:fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:
''',

#mills phone by lazaretto
'''
:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
:purple_square::notes::blue_square::blue_square::blue_square::blue_square::signal_strength::battery::purple_square:
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square: 
:purple_square::blue_square::golf::blue_square::clock::blue_square::camera_with_flash::blue_square::purple_square:
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square:
:purple_square::blue_square::notepad_spiral::blue_square::blue_book::blue_square::speech_balloon::blue_square::purple_square: 
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square:
:purple_square::blue_square::candy::blue_square::e_mail::blue_square::golf::blue_square::purple_square:
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square: 
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square:
:purple_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::purple_square: 
:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
''',
# ski resort by lazaretto
'''
:mountain_snow::mountain_snow::mountain_snow::mountain_snow::mountain_snow::mountain_snow::mountain_snow::mountain_snow:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::golf::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::evergreen_tree::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::snowman::evergreen_tree::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::snowman::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::evergreen_tree::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::golf::white_large_square::white_large_square::mountain_cableway:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::mountain_cableway:
''',
# yellowstone hotsprings by epix
'''
:evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree: 
:bison::bison::brown_square::green_square::golf::green_square::brown_square::green_square::brown_square: 
:bison::brown_square::brown_square::brown_square::green_square::brown_square::brown_square::brown_square::brown_square: 
:brown_square::brown_square::fog::red_square::red_square::red_square::fog::brown_square::brown_square: 
:brown_square::brown_square::red_square::yellow_square::yellow_square::yellow_square::red_square::brown_square::brown_square: 
:brown_square::red_square::yellow_square::blue_square::fog::blue_square::yellow_square::red_square::brown_square: 
:brown_square::red_square::yellow_square::fog::fog::fog::yellow_square::red_square::brown_square: 
:brown_square::red_square::yellow_square::blue_square::fog::blue_square::yellow_square::red_square::brown_square: 
:brown_square::brown_square::red_square::yellow_square::yellow_square::yellow_square::red_square::brown_square::brown_square: 
:brown_square::brown_square::fog::red_square::red_square::red_square::fog::brown_square::brown_square: 
:brown_square::brown_square::brown_square::brown_square::green_square::brown_square::brown_square::brown_square::bison: 
:brown_square::green_square::brown_square::green_square::golf::green_square::brown_square::bison::bison:
:evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree::evergreen_tree:
''',

#glolfball planet by hal 2000
'''
:milky_way::milky_way::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::milky_way::milky_way:
:milky_way::white_large_square::white_large_square::white_large_square::golf::white_large_square::white_large_square::white_large_square::milky_way:
:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:
:white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square::black_large_square::white_large_square:
:milky_way::white_large_square::white_large_square::white_large_square::golf::white_large_square::white_large_square::white_large_square::milky_way:
:milky_way::milky_way::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::milky_way::milky_way:
''',

# billiards table (six holes) by blamperer

'''
:brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square:
:brown_square::golf::green_square::green_square::green_square::green_square::green_square::green_square::golf::green_square::green_square::green_square::green_square::green_square::green_square::golf::brown_square:
:brown_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::brown_square:
:brown_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::brown_square:
:brown_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::brown_square:
:brown_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::green_square::brown_square:
:brown_square::golf::green_square::green_square::green_square::green_square::green_square::green_square::golf::green_square::green_square::green_square::green_square::green_square::green_square::golf::brown_square:
:brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square::brown_square:
''',

# sunset from a flotation device by lazaretto
'''
:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::cloud::yellow_square:
:yellow_square::yellow_square::yellow_square::golf::yellow_square::yellow_square::yellow_square::yellow_square:
:orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square::orange_square:
:red_square::cloud::red_square::red_square::red_square::red_square::red_square::red_square:
:purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square::purple_square:
:ocean::ocean::ocean::ocean::ocean::ocean::ocean::ocean:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::golf::blue_square::blue_square::blue_square:
:speedboat::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
''',

# sand bird by hal 2000
'''
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::white_large_square::white_large_square::white_large_square:
:white_large_square::white_large_square::white_large_square::blue_square::white_square_button::golf::white_square_button::blue_square::blue_square::white_large_square::white_large_square:
:white_large_square::white_large_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::blue_square:
:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:
:blue_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::blue_square:
:blue_square::blue_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::blue_square::white_large_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::yellow_square::blue_square::blue_square::white_large_square::white_large_square::white_large_square:
:white_large_square::blue_square::blue_square::yellow_square::yellow_square::golf::yellow_square::yellow_square::blue_square::white_large_square::white_large_square:
:white_large_square::white_large_square::blue_square::blue_square::yellow_square::yellow_square::yellow_square::blue_square::blue_square::blue_square::blue_square:
''',

]

disabled_courses = [
# minesweeper by blamperer
# for some reason :one: is showing up as 3 characters
'''
:blue_square::blue_square::blue_square::one::white_large_square::one::blue_square::blue_square::blue_square::blue_square:
:blue_square::blue_square::blue_square::one::golf::one::blue_square::blue_square::one::one:
:one::one::blue_square::one::one::one::blue_square::blue_square::one::white_large_square:
:white_large_square::one::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::one::white_large_square:
:one::one::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::one::white_large_square:
:blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::one::white_large_square:
:one::one::blue_square::blue_square::blue_square::one::one::one::one::one:
:white_large_square::one::blue_square::blue_square::blue_square::one::golf::one::blue_square::blue_square:
:white_large_square::two::one::blue_square::blue_square::one::one::one::blue_square::blue_square:
:white_large_square::white_large_square::one::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square::blue_square:
''',

#cursed madeleine by syl
# so big it cuts off the scoreboard
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
]

# to do: give each course a name


special_case_emojis = { #these are emojis which aren't converted to unicode by emojize() so I need to do it manually
":golf:":"⛳",
":city_dusk:":"🌆",
":race_car:":"🏎️",
":frame_photo:":"🖼️",
":desktop:":"🖥️",
":couch:":"🛋️",

# still-problematic emojis
#":gear:":"⚙️",
#"⚙":"⚙️", # emojize converts :gear: to this tiny non-fullwidth thing (it's the same character, but missing a variation selector)
# ":one:":"1️⃣", #:one: works perfectly on discord but it's actually two emojis and a ZWJ, so python treats it as 3 characters.

":beach_umbrella:":'🏖️', #this is treated as two characters
":salad:":'🥗',
":hotdog:":'🌭',
":notepad_spiral:":'🗒️',
":clock:":'🕰️',
":e_mail:":'📧',
":snowman:":'⛄',
":mountain_snow:":"🏔️",

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
        print(unconverted_emoji)
        raise ValueError



if __name__ == "__main__":
    verify_courses()
