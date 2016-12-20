import sys


class Game(object):
    """
    Implements an in-memory object for saving, loading, and logging games built with TilePy.
    """

    def __init__(self, name):
        self.name = name
        self.FPS = 10
        self.dialog_window_stack = []
        print("Made with TilePy by Romulus10")
        print("TilePy is loading...")

    def ready(self):
        self.game_log("Ready", 0)

    def game_log(self, msg, level):
        msg = str(msg)
        level_name = ""
        if level == 0:
            # This level should be used only by the engine.
            level_name = "notice"
        if level == 1:
            # This level should be used when developing a game or extending the engine.
            level_name = "debug"
        if level == 2:
            # This level should be used to warn of unexpected activity.
            level_name = "warn"
        if level == 3:
            # This level should be used *only* when a game-crashing bug is being fixed.
            level_name = "error"
        print(self.name + " " + level_name + ": " + msg)
        if level == 3:
            sys.exit(1)

    def save_game(self):
        # TODO Implement
        pass

    def load_game(self):
        # TODO Implement
        pass
