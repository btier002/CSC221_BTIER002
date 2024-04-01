import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draw Image Example")

# Load image
image = pygame.image.load("images\lebron.bmp")  # Replace "your_image_path_here.jpg" with the path to your image
image_rect = image.get_rect()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue
    screen.fill((0, 0, 255))  # (R, G, B) - this fills the screen with blue color

    # Calculate image position to center it
    image_x = (screen_width - image_rect.width) // 2
    image_y = (screen_height - image_rect.height) // 2

    # Draw the image
    screen.blit(image, (image_x, image_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
