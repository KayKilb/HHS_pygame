import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (23, 85, 85)
X_COLOR = (242, 85, 96)
O_COLOR = (85, 170, 85)

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
CELL_SIZE = 100

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

# Variables
player_turn = 'X'
board = [['' for x in range(3)] for y in range(3)]

def draw_board():
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * row, 0), (CELL_SIZE * row, SCREEN_HEIGHT), 5)
        pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * row), (SCREEN_WIDTH, CELL_SIZE * row), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col*CELL_SIZE, row*CELL_SIZE), ((col+1)*CELL_SIZE, (row+1)*CELL_SIZE), 5)
                pygame.draw.line(screen, X_COLOR, (col*CELL_SIZE, (row+1)*CELL_SIZE), ((col+1)*CELL_SIZE, row*CELL_SIZE), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (int((col+0.5)*CELL_SIZE), int((row+0.5)*CELL_SIZE)), CELL_SIZE//3, 5)

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return None
    return 'Tie'

# Main game loop
winner = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not winner:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                winner = check_winner()
                player_turn = 'O' if player_turn == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()
    clock.tick(60)

    if winner:
        print(f'{winner} Wins!' if winner != 'Tie' else 'It\'s a Tie!')
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
