# Module by Romulus10
# Tile sizes are ALWAYS 32x32.
# Currently running least awkwardly at 10 fps.

import pygame


class Map(object):
    def __init__(self, name, tiles, wall_values, list_tiles, x, y, entities, entity_pos):
        self.name = name
        self.tiles = tiles
        self.wall_values = wall_values
        self.list_tiles = list_tiles
        self.size_x = x
        self.size_y = y
        self.entities = entities
        self.entity_pos = entity_pos

    def draw(self, screen):
        for x in range(self.size_x):
            for y in range(self.size_y):
                tile = pygame.image.load(self.list_tiles[self.tiles[x][y]])
                screen.blit(tile, [x * 32, y * 32])


class Game(object):
    def __init__(self):
        self.FPS = 10


class Player(object):
    def __init__(self, sprite_list, x, y):
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y
        self.speed_x = x
        self.speed_y = y
        self.facing = "down"
        self.inventory = {}

    def draw(self, screen, this_map):
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
        if not (not (this_map.tiles[self.pos_x][self.pos_y] in this_map.wall_values) and not (
                    this_map.entity_pos[self.pos_x][self.pos_y] is not 0)):
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
        if self.facing == "left":
            with this_map.entity_pos[self.pos_x - 1][self.pos_y] as tmp:
                if tmp in this_map.entities:
                    tmp.interact_with()

        if self.facing == "right":
            with this_map.entity_pos[self.pos_x + 1][self.pos_y] as tmp:
                if tmp in this_map.entities:
                    tmp.interact_with()

        if self.facing == "up":
            with this_map.entity_pos[self.pos_x][self.pos_y - 1] as tmp:
                if tmp in this_map.entities:
                    tmp.interact_with()

        if self.facing == "down":
            with this_map.entity_pos[self.pos_x][self.pos_y + 1] as tmp:
                if tmp in this_map.entities:
                    tmp.interact_with()


class NPC(object):
    def __init__(self, name, npc_cat, done, sprite_list):
        self.name = name
        self.npc_cat = npc_cat
        self.done = done
        self.sprite_list = sprite_list
