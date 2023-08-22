
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

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
turn = "O"

# Function to draw the grid
def draw_grid():
    # Draw vertical lines
    pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 5)

    # Draw horizontal lines
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)

# Function to draw the O and X images based on the game state
def draw_pieces():
    for row in range(3):
        for col in range(3):
            piece = board[row][col]
            if piece == "O":
                window.blit(o_image, (col * 200 + 50, row * 200 + 50))
            elif piece == "X":
                window.blit(x_image, (col * 200 + 50, row * 200 + 50))

# Function to check for a win or draw
def check_game_over():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return True

    # Check for draw (if the board is full)
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return True

    return False

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not check_game_over():
            # Get the row and column based on the mouse click position
            x, y = pygame.mouse.get_pos()
            row, col = y // 200, x // 200

            # Make a move if the square is empty
            if board[row][col] == "":
                board[row][col] = turn
                turn = "X" if turn == "O" else "O"

    # Draw the background image at the calculated position
    window.blit(background_image, (image_x, image_y))

    # Draw the grid and pieces
    draw_grid()
    draw_pieces()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
