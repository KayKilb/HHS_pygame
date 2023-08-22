
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
piece_size = (170, 170)
o_image = pygame.image.load("o_image.png")
x_image = pygame.image.load("x_image.png")
o_image = pygame.transform.scale(o_image, piece_size)
x_image = pygame.transform.scale(x_image, piece_size)

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
turn = "O"

# Function to draw the grid (adjusted to fit 650x650 area)
# ... Same as previous code ...

# Function to draw the O and X images based on the game state
# ... Same as previous code ...

# Function to display the winner or draw
def display_winner():
    winner = None
    # Check rows, columns, diagonals for a winner
    # ... Similar logic as previous code ...

    # Display the winner or draw message
    font = pygame.font.Font(None, 74)
    if winner:
        text = font.render(winner + " Wins!", True, (0, 255, 0))
    else:
        text = font.render("It's a Draw!", True, (0, 255, 0))
    
    window.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))

# Rest of the code remains the same...

# Event loop to keep the window open
running = True
while running:
    game_over = False  # Add logic to determine if the game is over (similar to previous code)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image (stretched to fit)
    window.blit(background_image, (0, 0))

    # Draw the grid and pieces
    draw_grid()
    draw_pieces()

    # Display the winner or draw if the game is over
    if game_over:
        display_winner()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
