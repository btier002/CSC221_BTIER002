import pygame
from pygame.sprite import Sprite
 
class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, stargame):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = stargame.screen
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
