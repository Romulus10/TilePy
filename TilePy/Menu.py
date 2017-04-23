import pygame

from TilePy import colors


class Menu(object):
    # TODO Develop a system for interacting with windows.
    def __init__(self, text):
        """
        :type text: list
        :param text: A list of menu items
        """
        pygame.font.init()
        self.visible = False
        self.corner_pos_x = 500
        self.corner_pos_y = 10
        self.length = 200
        self.width = 400
        self.font = pygame.font.Font(None, 40)
        self.current_selection = 0
        self.text = text
        self.text.append("Save")
        self.text.append("Load")

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, colors['white'], [self.corner_pos_x, self.corner_pos_y, self.length, self.width])
            for x in range(len(self.text)):
                if self.current_selection == x:
                    screen.blit(self.font.render(self.text[x], True, colors['red']),
                                [self.corner_pos_x + 16, 5 + (self.corner_pos_y + (16 * (x * 2)))])
                else:
                    screen.blit(self.font.render(self.text[x], True, colors['black']),
                                [self.corner_pos_x + 16, 5 + (self.corner_pos_y + (16 * (x * 2)))])

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False
