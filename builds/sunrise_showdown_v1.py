
import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size (twice as big)
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Load the background image
background_image = cd pygame.image.load("background.png")

# Calculate the position to center the background image
image_x = (window_size[0] - background_image.get_width()) // 2
image_y = (window_size[1] - background_image.get_height()) // 2

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image at the calculated position
    window.blit(background_image, (image_x, image_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
