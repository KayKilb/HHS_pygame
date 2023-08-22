
import pygame

# Initialize Pygame
pygame.init()

# Create a window with a specific size (800x800)
window_size = (800, 800)
window = pygame.display.set_mode(window_size)

# Load and stretch the background image to fit the window size
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, window_size)

# Load the O and X images and resize them to fit the grid spaces
piece_size = (170, 170)  # Adjust this size to fit within the grid spaces
o_image = pygame.image.load("o_image.png")
x_image = pygame.image.load("x_image.png")
o_image = pygame.transform.scale(o_image, piece_size)
x_image = pygame.transform.scale(x_image, piece_size)

# Rest of the code remains the same as previous...

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
            x_pos = col * (650 // 3) + 75 + 15  # Centered within the grid space
            y_pos = row * (650 // 3) + 75 + 15  # Centered within the grid space
            if piece == "O":
                window.blit(o_image, (x_pos, y_pos))
            elif piece == "X":
                window.blit(x_image, (x_pos, y_pos))

# Rest of the code remains the same...

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
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

# Function to determine the winner or draw
def get_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][0]

    # Check for draw (if the board is full)
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return "Draw"

    return None

# Event loop to keep the window open
running = True
while running:
    winner = get_winner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
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

    # Display the winner or draw if the game is over
    if winner:
        font = pygame.font.Font(None, 74)
        if winner != "Draw":
            text = font.render(winner + " Wins!", True, (0, 255, 0))
        else:
            text = font.render("It's a Draw!", True, (0, 255, 0))
        
        window.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
