import pygame


class Map(object):
    def __init__(self, name, tiles, list_tiles, x, y):
        self.name = name
        self.tiles = tiles
        self.list_tiles = list_tiles
        self.size_x = x
        self.size_y = y

    def draw(self, screen):
        for x in range(self.size_x):
            for y in range(self.size_y):
                print(self.tiles[x][y])
                print(self.list_tiles[self.tiles[x][y]])
                tile = pygame.image.load(self.list_tiles[self.tiles[x][y]])
                screen.blit(tile, [x * 32, y * 32])


class Game(object):
    def __init__(self):
        pass


class Player(object):
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list


class NPC(object):
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list
