import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size (you can change the size as needed)
window_size = (300, 300)
window = pygame.display.set_mode(window_size)

# Load the background image
background_image = pygame.image.load("background.png")

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
