import pygame


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
        """
        :param screen: A pygame.Surface object
        """
        for x in range(self.size_x):
            for y in range(self.size_y):
                tile = pygame.image.load("../" + self.list_tiles[self.tiles[x][y]])
                screen.blit(tile, [x * 32, y * 32])
        for x in self.entities:
            x.draw(screen)
