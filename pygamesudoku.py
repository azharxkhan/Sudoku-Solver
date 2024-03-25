import pygame
import sys
from sudoku_solver import solve

# Define the Sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,0,0,9,3,0],
    [9,0,4,0,6,0,0,0,0],
    [0,7,0,0,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,0,9,2,0,0,0,0,7]
]

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 40

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Function to draw the Sudoku board
def draw_board():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                font = pygame.font.Font(None, FONT_SIZE)
                text = font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j*60+30, i*60+30))
                screen.blit(text, text_rect)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, i*60), (WIDTH, i*60), 3)
            pygame.draw.line(screen, BLACK, (i*60, 0), (i*60, HEIGHT-60), 3)
        else:
            pygame.draw.line(screen, BLACK, (0, i*60), (WIDTH, i*60), 1)
            pygame.draw.line(screen, BLACK, (i*60, 0), (i*60, HEIGHT-60), 1)

def main():
    while True:
        screen.fill(WHITE)
        draw_board()
        solve_button = pygame.Rect(200, 550, 140, 40)
        pygame.draw.rect(screen, (0, 255, 0), solve_button)
        solve_font = pygame.font.Font(None, 36)
        solve_text = solve_font.render("Solve", True, BLACK)
        solve_text_rect = solve_text.get_rect(center=solve_button.center)
        screen.blit(solve_text, solve_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    solve(board)

        pygame.display.update()

if __name__ == "__main__":
    main()
