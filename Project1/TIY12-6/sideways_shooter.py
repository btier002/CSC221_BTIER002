# 12-2
import sys

import pygame

from tiysettings import Settings
from tiyrocket import Rocket
from tiybullet import Bullet

class RocketGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")
        
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color
        self.bg_color = (255, 0, 0)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.screen.fill(self.bg_color)
            self.rocket.blitme()

            # Make the most recently drawn screen visible.
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # for up 
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        # for down
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

        
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        # for up
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        # for down
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        # for the bullets
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update postion of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = RocketGame()
    ai.run_game()