
import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Load the background image
background_image = pygame.image.load("background.png")

# Calculate the position to center the background image
image_x = (window_size[0] - background_image.get_width()) // 2
image_y = (window_size[1] - background_image.get_height()) // 2

# Function to draw the grid
def draw_grid():
    # Draw vertical lines
    pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 5)

    # Draw horizontal lines
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image at the calculated position
    window.blit(background_image, (image_x, image_y))

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
