import pygame
import sys
# Without settings file

# Initialize Pygame
pygame.init()

# Set up the window dimensions
window_width = 1200
window_height = 800

# Set up the colors
blue = (0, 0, 255)

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Blue Background Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the window with blue color
    window.fill(blue)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
