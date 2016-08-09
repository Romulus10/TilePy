# Module by Romulus10
# Tile sizes are ALWAYS 32x32.
# Currently running least awkwardly at 10 fps.

# TODO Projectiles

import pygame

import romulus_tools


# Don't use this - it's easier and better practice to just remember "32".
# globals()['tile_size'] = 32


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
    def __init__(self, name):
        self.name = name
        self.FPS = 10
        print("Made with TilePy by Romulus10")
        print("TilePy is loading...")

    def ready(self):
        self.game_log("Ready", 0)

    def game_log(self, msg, level):
        level_name = ""
        if level == 0:
            level_name = "notice"
        if level == 1:
            level_name = "debug"
        if level == 2:
            level_name = "warn"
        if level == 3:
            level_name = "error, continuing"
        print(self.name + " " + level_name + ": " + msg)


class Player(object):
    def __init__(self, sprite_list, x, y):
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.facing = "down"
        self.inventory = {}

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
            if self.pos_x == x.pos_x and self.pos_y == x.pos_y:
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

    def check_for_interaction(self, this_map):
        # DONE Test check_for_interaction
        # DONE Rewrite check_for_interaction.
        for x in this_map.entities:
            if x.pos_x == self.pos_x - 1 and self.facing == "left":
                x.interact_with()
            if x.pos_x == self.pos_x + 1 and self.facing == "right":
                x.interact_with()
            if x.pos_y == self.pos_y - 1 and self.facing == "up":
                x.interact_with()
            if x.pos_y == self.pos_y + 1 and self.facing == "down":
                x.interact_with()


class NPC(object):
    # TODO NPC AI Movement
    def __init__(self, name, done, sprite_list, x, y):
        self.name = name
        self.done = done
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y

    def interact_with(self):
        # TODO NPC Interactions
        globals()['game'].game_log("interacting with " + self.name, 0)

    def draw(self, screen):
        # TODO Handle moving NPCs.
        # TODO Handle turning to face player.
        # TODO Handle differentiating between items and people and projectiles.
        # TODO Handle changing active sprite.
        player = pygame.image.load(self.sprite_list[0])
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])


class Item(NPC):
    # TODO Add using and picking up items.
    def __init__(self, name, done, sprite_list, x, y):
        super(Item, self).__init__(name, done, sprite_list, x, y)


class Projectile(NPC):
    # TODO This needs specialized collision detection.
    def __init__(self, name, done, sprite_list, x, y):
        super(Projectile, self).__init__(name, done, sprite_list, x, y)

    def interact_with(self):
        # TODO Redesign for projectiles.
        pass
