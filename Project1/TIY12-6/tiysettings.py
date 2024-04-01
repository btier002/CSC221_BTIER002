class Settings:
    '''A class to store all settings for the Rocket Game'''

    def __init__(self):
        '''Initialize the game's settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 230, 230)

        # Rocket settings
        self.rocket_speed = 10.0

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3