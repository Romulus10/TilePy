import pygame

import TilePy
from DialogWindow import DialogWindow


class MapGate(object):
    def __init__(self, pos_x, pos_y, on_map, to_map, image):
        """
        :param pos_x: Location of the gate on the x axis
        :param pos_y: Location of the gate on the y axis
        :param on_map: Which map the entrance is connected to
        :param to_map: The map the gate points to
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.on_map = on_map
        self.to_map = to_map
        self.image = image
        self.done = False

    def draw(self, screen):
        player = pygame.image.load("../" + self.image)
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def interact_with(self, p):
        """
        :type p: This is completely pointless and only included for uniformity with the other interact_with methods.
        """
        var = DialogWindow("This is a door.")
        var.show()
        TilePy.game_object.dialog_window_stack.append(var)
