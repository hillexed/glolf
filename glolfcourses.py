import random
import emoji

courses = [
#The Llawn
'''
        🕸️🟩🟩🟩🟩🟩🟩🟩🟩🕸️🕸️
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
# glolf in SPACE by shorkball
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
'''
]
# to do: give each course a name


special_case_emojis = {
":golf:":"⛳",
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
