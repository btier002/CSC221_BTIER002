import pygame

class Rocket:
    '''A class to manage the rocket.'''
    def __init__(self, rocket_game):
        '''Initalize the rocket and set its starting position.'''
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\R.bmp')
        # Rotate the image
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        # for self.y (vertical postion)
        self.y = float(self.rect.y)


        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        # for up and down
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''Update the rocket's postion based on the movement flags.'''
        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        # for up
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        # for down
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed



        # Update rect object from self.x
        self.rect.x = self.x
        # for self.y
        self.rect.y = self.y

    def blitme(self):
        '''Draw theh rocket at its current location.'''
        self.screen.blit(self.image, self.rect)

    