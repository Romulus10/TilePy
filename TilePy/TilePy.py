# Module by Romulus10
# Tile sizes are ALWAYS 32x32.
# Currently running least awkwardly at 10 fps.

# TODO System for saving and loading game data.
# TODO System for easy game_init scripts - Document the module
# FIXME Performance is probably utterly atrocious.
# DONE Dancing Off the Map bug - Reproduce by running test.py and rapidly and repeatedly pressing different arrow keys.
# DONE Projectiles

import romulus_tools

# Don't use this - it's easier and better practice to just remember "32".
# globals()['tile_size'] = 32
# TODO Develop a function to be called every tick to adjust the position of each active NPC based on a given path
import Game
import Exceptions

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

game = object

def check_for_open_window_and_close(game):
    if len(game.dialog_window_stack) > 0:
        if game.dialog_window_stack[len(game.dialog_window_stack) - 1].visible:
            game.dialog_window_stack[len(game.dialog_window_stack) - 1].hide()
            game.dialog_window_stack.pop()
            return True
        return False
    return False


def read_map_file(filename):
    # TODO Test read_map_file.
    """
    Returns a tuple of (map_list, x, y)
    :rtype: tuple
    """
    iterations = 0
    inr_len = 0
    f = open(filename, 'r')
    list_1 = f.readlines()
    f.close()
    for x in list_1:
        x.split(',')
        romulus_tools.remove_newlines(x)
        if iterations > 0:
            inr_len = len(x)
        else:
            if len(x) != inr_len:
                # Raises a fatal exception if the rows of the map are uneven.
                raise Exceptions.InvalidMapFileException("All rows of the map must be the same length.")
    top_len = len(list_1)
    return list_1, top_len, inr_len


def begin(name):
    globals()['game'] = Game.Game(name)
    return globals()['game']
