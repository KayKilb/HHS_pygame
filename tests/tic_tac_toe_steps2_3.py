
import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Load the background image
background_image = pygame.image.load("background.png")

# Load the O and X images
o_image = pygame.image.load("o_image.png")
x_image = pygame.image.load("x_image.png")

# Calculate the position to center the background image
image_x = (window_size[0] - background_image.get_width()) // 2
image_y = (window_size[1] - background_image.get_height()) // 2

# Function to draw the O image at a given position
def draw_o(position):
    window.blit(o_image, position)

# Function to draw the X image at a given position
def draw_x(position):
    window.blit(x_image, position)

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image at the calculated position
    window.blit(background_image, (image_x, image_y))

    # Example: Draw O and X at specific positions (you can modify these positions)
    draw_o((150, 150))
    draw_x((450, 450))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
