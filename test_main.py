if winner:
    winner_text = font.render(f"{winner} WINS!!!", True, (255, 0, 0))
    screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)

    exit()
elif event.type == pygame.MOUSEBUTTONDOWN:
    x, y = pygame.mouse.get_pos()
    row, col = x // CELL_SIZE, y // CELL_SIZE
    if board[col][row] == '':
        board[col][row] = 'O' if player_turn == 'O' else 'X'
        player_turn = 'O' if player_turn == 'X' else 'X'
