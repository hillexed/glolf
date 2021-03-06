import logging
logger = logging.getLogger(__name__)

users_with_games_active = []
MAX_SIMULTANEOUS_GAMES = 10

def limit_one_game_per_person(func):
    '''
    A decorator to ensure someone can only run one command at a time.
    Also, has some bonus error reporting if something goes wrong.
    The first argument of a function using this decorator must be 'message', a discord message to react to if something goes wrong
    '''
    async def wrapper(message, *args, **kwargs):
        global users_with_games_active

        if message.author in users_with_games_active:
            await message.channel.send("To avoid lag, please wait for your current game to finish before starting any more.")
            return
        users_with_games_active.append(message.author)
        try:
            return await func(message, *args, **kwargs)
        except (Exception, KeyboardInterrupt) as e:
                logger.exception(e)
                await message.add_reaction('⚠️')
                raise e
        finally:
            if message.author in users_with_games_active:
                users_with_games_active.remove(message.author)

    return wrapper

def get_users_with_games_active():
    return users_with_games_active

def clear_users_with_games_active():
    global users_with_games_active
    users_with_games_active = []

def too_many_games_active():
    return len(users_with_games_active) > MAX_SIMULTANEOUS_GAMES




update_coming = False
def set_update_coming(value):
    global update_coming
    update_coming = value

def is_update_coming():
    return update_coming

def disable_if_update_coming(func):
    '''
    A decorator to disable starting new games if updates are coming
    '''
    async def wrapper(message, *args, **kwargs):
        print(is_update_coming())
        if is_update_coming():
            await message.channel.send(":loop: HANG TIGHT FOR A MOMENT, GOT SOME RADICAL RENOVATIONS COMIN' RIGHT UP\n:loop: PLEASE LEAVE A MESSAGE AFTER THE TONE")
            return
        return await func(message, *args, **kwargs)
    return wrapper
