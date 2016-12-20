# Module by Romulus10
# Tile sizes are ALWAYS 32x32.
# Currently running least awkwardly at 10 fps.

# TODO System for saving and loading game data.
# TODO System for easy game_init scripts - Document the module
# FIXME Performance is probably utterly atrocious.
# DONE Dancing Off the Map bug - Reproduce by running test.py and rapidly and repeatedly pressing different arrow keys.
# DONE Projectiles

import sys

import pygame

import romulus_tools

# Don't use this - it's easier and better practice to just remember "32".
# globals()['tile_size'] = 32

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}


# TODO Develop a function to be called every tick to adjust the position of each active NPC based on a given path


def check_for_open_window_and_close(game):
    if len(game.dialog_window_stack) > 0:
        if game.dialog_window_stack[len(game.dialog_window_stack) - 1].visible:
            game.dialog_window_stack[len(game.dialog_window_stack) - 1].hide()
            game.dialog_window_stack.pop()
            return True
        return False
    return False


class MapGate(object):
    def __init__(self, pos_x, pos_y, on_map, to_map):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.on_map = on_map
        self.to_map = to_map


class DialogWindow(object):
    # TODO Test dialog windows.
    # TODO Check string overflow.
    # DONE Set up multiple dialog boxes to one event.
    #   We just push multiple DialogWindows to the queue in reverse order.
    def __init__(self, text):
        self.visible = False
        self.corner_pos_x = 16
        self.corner_pos_y = 10 * 32
        self.length = 668
        self.width = 400
        self.text = text
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, colors['white'], [self.corner_pos_x, self.corner_pos_y, self.length, self.width])
            screen.blit(self.font.render(self.text, True, colors['black']),
                        [self.corner_pos_x + 16, self.corner_pos_y + 16])

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False


class InvalidMapFileException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


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
                raise InvalidMapFileException("All rows of the map must be the same length.")
    top_len = len(list_1)
    return list_1, top_len, inr_len


def begin(name):
    globals()['game'] = Game(name)
    return globals()['game']


class Map(object):
    # TODO Handle moving between maps.
    def __init__(self, name, tiles, wall_values, list_tiles, x, y, entities):
        self.name = name
        self.tiles = tiles
        self.wall_values = wall_values
        self.list_tiles = list_tiles
        self.size_x = x
        self.size_y = y
        self.entities = entities

    def draw(self, screen):
        for x in range(self.size_x):
            for y in range(self.size_y):
                tile = pygame.image.load(self.list_tiles[self.tiles[x][y]])
                screen.blit(tile, [x * 32, y * 32])
        for x in self.entities:
            x.draw(screen)


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


class Player(object):
    def __init__(self, sprite_list, x, y):
        self.sprite_list = sprite_list
        self.original_pos_x = x
        self.original_pos_y = y
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.facing = "down"
        self.inventory = []

    def draw(self, screen, this_map):
        player = None
        self.check_pos()
        self.check_collision(this_map)
        if self.facing == "down":
            player = pygame.image.load(self.sprite_list[0])
        if self.facing == "up":
            player = pygame.image.load(self.sprite_list[1])
        if self.facing == "right":
            player = pygame.image.load(self.sprite_list[2])
        if self.facing == "left":
            player = pygame.image.load(self.sprite_list[3])
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def move(self, direction):
        self.facing = direction
        if direction == "down":
            self.speed_y = 1
        if direction == "up":
            self.speed_y = -1
        if direction == "right":
            self.speed_x = 1
        if direction == "left":
            self.speed_x = -1

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def check_pos(self):
        self.pos_y += self.speed_y
        self.pos_x += self.speed_x

    def check_collision(self, this_map):
        # DONE Check collision with NPC.
        try:
            if this_map.tiles[self.pos_x][self.pos_y] in this_map.wall_values:
                if self.facing == "left":
                    self.stop()
                    self.pos_x += 1
                if self.facing == "right":
                    self.stop()
                    self.pos_x -= 1
                if self.facing == "up":
                    self.stop()
                    self.pos_y += 1
                if self.facing == "down":
                    self.stop()
                    self.pos_y -= 1
            for x in this_map.entities:
                if (self.pos_x == x.pos_x and self.pos_y == x.pos_y) and not x.done:
                    if self.facing == "left":
                        self.stop()
                        self.pos_x += 1
                    if self.facing == "right":
                        self.stop()
                        self.pos_x -= 1
                    if self.facing == "up":
                        self.stop()
                        self.pos_y += 1
                    if self.facing == "down":
                        self.stop()
                        self.pos_y -= 1
        except IndexError:
            globals()['game'].game_log("Outside the map. Repositioning.", 2)
            # HACK Addresses the Dancing Off the Map bug. Not very graceful - should be fixed ASAP.
            self.pos_x = self.original_pos_x
            self.pos_y = self.original_pos_y

    def check_for_interaction(self, this_map):
        # DONE Test check_for_interaction
        # DONE Rewrite check_for_interaction.
        for x in this_map.entities:
            if x.pos_x == self.pos_x - 1 and self.facing == "left":
                x.interact_with(self)
            if x.pos_x == self.pos_x + 1 and self.facing == "right":
                x.interact_with(self)
            if x.pos_y == self.pos_y - 1 and self.facing == "up":
                x.interact_with(self)
            if x.pos_y == self.pos_y + 1 and self.facing == "down":
                x.interact_with(self)

    def get_inventory(self):
        globals()['game'].game_log("Player inventory: " + str(self.inventory), 0)


class NPC(object):
    # TODO NPC AI Movement
    # TODO Determine what dialog box to display when self.done
    def __init__(self, name, done, sprite_list, x, y):
        self.facing = "down"
        self.name = name
        self.done = done
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y

    def interact_with(self, player):
        # DONE How do I get dialog to work with NPCs?
        # TODO NPC Interactions
        globals()['game'].game_log("interacting with " + self.name, 0)

    def turn_to_face_player(self, player):
        if player.pos_x == self.pos_x - 1:
            self.facing = "left"
        elif player.pos_x == self.pos_x + 1:
            self.facing = "right"
        elif player.pos_y == self.pos_y - 1:
            self.facing = "down"
        elif self.pos_y == self.pos_y + 1:
            self.facing = "up"

    def draw(self, screen):
        # TODO Handle moving NPCs.
        # DONE Handle turning to face player.
        # TODO Handle differentiating between items and people and projectiles.
        # DONE Handle changing active sprite.
        if self.facing == "down":
            player = pygame.image.load(self.sprite_list[0])
        if self.facing == "up":
            player = pygame.image.load(self.sprite_list[1])
        if self.facing == "right":
            player = pygame.image.load(self.sprite_list[2])
        if self.facing == "left":
            player = pygame.image.load(self.sprite_list[3])
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def path_act(self, direction):
        if direction is "up":
            self.pos_y += 1
        if direction is "down":
            self.pos_y -= 1
        if direction is "right":
            self.pos_x += 1
        if direction is "left":
            self.pos_x -= 1


class Actor(NPC):
    """
    Implements a human-type NPC that the player can talk to.
    """

    def __init__(self, name, done, sprite_list, x, y):
        super(Actor, self).__init__(name, done, sprite_list, x, y)


class ShopKeep(NPC):
    """
    Implements an NPC entity with an inventory that the player can trade with.
    """

    def __init__(self, name, done, sprite_list, x, y):
        super(ShopKeep, self).__init__(name, done, sprite_list, x, y)


class Item(NPC):
    """
    To add items to a game using the TilePy library, they should be new classes that extend the Item class.
    They should however ONLY override the "use" method. All other methods should work fine.
    """

    # DONE Add using
    # DONE and picking up items.
    def __init__(self, name, done, sprite_list, x, y, msg):
        super(Item, self).__init__(name, done, sprite_list, x, y)
        self.text = msg
        self.in_inventory = False

    def interact_with(self, player):
        globals()['game'].game_log(globals()['game'].dialog_window_stack, 1)
        globals()['game'].game_log("added to inventory: " + self.name, 0)
        var = DialogWindow(self.text)
        var.show()
        globals()['game'].dialog_window_stack.append(var)
        self.done = True
        self.in_inventory = True
        player.inventory.append(self)

    def draw(self, screen):
        if not self.done:
            player = pygame.image.load(self.sprite_list[0])
            screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def use(self):
        """
        This is a stub to be inherited by game-specific Item objects.
        :return:
        """
        if self.in_inventory:
            globals()['game'].game_log("Using " + self.name, 0)
        else:
            globals()['game'].game_log("Item not in player inventory " + self.name, 0)

            # If turn-based combat is the preferred action method of the library, this really isn't necessary.
            # IGNORE class Projectile(NPC):
            # IGNORE This needs specialized collision detection.
            # def __init__(self, name, done, sprite_list, x, y):
            # super(Projectile, self).__init__(name, done, sprite_list, x, y)

            # def interact_with(self, player):
            # IGNORE Redesign for projectiles.
            # pass


class StatsEnabledObject(object):
    """
    Creates a Character object which can be used in turn-based combat or in tracking character stats.
    """

    # For use in turn-based combat. I think I'll use that as the preferred combat system.
    def __init__(self):
        pass
