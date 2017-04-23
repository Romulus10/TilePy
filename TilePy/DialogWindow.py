import pygame

from TilePy import colors


class DialogWindow(object):
    # TODO Check string overflow.
    # We just push multiple DialogWindows to the queue in reverse order.
    def __init__(self, text):
        """
        :param text: Text to display in the dialog window.
        """
        self.visible = False
        self.corner_pos_x = 16
        self.corner_pos_y = 10 * 32
        self.length = 668
        self.width = 400
        self.text = text
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        """
        :param screen: a pygame.Surface object to draw on
        """
        if self.visible:
            pygame.draw.rect(screen, colors['white'], [self.corner_pos_x, self.corner_pos_y, self.length, self.width])
            screen.blit(self.font.render(self.text, True, colors['black']),
                        [self.corner_pos_x + 16, self.corner_pos_y + 16])

    def show(self):
        """ Toggle Method for DialogWindow.visible """
        self.visible = True

    def hide(self):
        """ Toggle Method for DialogWindow.visible """
        self.visible = False
