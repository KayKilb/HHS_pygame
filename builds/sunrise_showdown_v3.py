
import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size (800x800)
window_size = (800, 800)
window = pygame.display.set_mode(window_size)

# Load and stretch the background image to fit the window size
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, window_size)

# Load the O and X images (adjust size if needed)
o_image = pygame.image.load("o_image.png")
x_image = pygame.image.load("x_image.png")

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
turn = "O"

# Function to draw the grid (adjusted to fit 650x650 area)
def draw_grid():
    offset = 75
    size = 650
    step = size // 3
    for i in range(1, 3):
        pygame.draw.line(window, (0, 0, 0), (offset, offset + i * step), (offset + size, offset + i * step), 5)
        pygame.draw.line(window, (0, 0, 0), (offset + i * step, offset), (offset + i * step, offset + size), 5)

# Function to draw the O and X images based on the game state
def draw_pieces():
    for row in range(3):
        for col in range(3):
            piece = board[row][col]
            x_pos = col * (650 // 3) + 75 + 50
            y_pos = row * (650 // 3) + 75 + 50
            if piece == "O":
                window.blit(o_image, (x_pos, y_pos))
            elif piece == "X":
                window.blit(x_image, (x_pos, y_pos))

# Rest of the code remains the same as previous...

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Adjusted to fit new grid
            x, y = pygame.mouse.get_pos()
            row, col = (y - 75) // (650 // 3), (x - 75) // (650 // 3)
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = turn
                turn = "X" if turn == "O" else "O"

    # Draw the background image (stretched to fit)
    window.blit(background_image, (0, 0))

    # Draw the grid and pieces
    draw_grid()
    draw_pieces()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
