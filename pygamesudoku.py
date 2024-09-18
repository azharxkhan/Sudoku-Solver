import pygame
import sys
from sudoku_solver import solve  # Assuming you have a function that solves the Sudoku puzzle
import time

# Define the empty Sudoku board
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# User-entered numbers stored separately from solved numbers
user_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

pygame.init()

WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT_SIZE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


def draw_board():
    """
    Draws the Sudoku board and displays user-entered numbers in black and solved numbers in blue.
    """
    for i in range(9):
        for j in range(9):
            if user_board[i][j] != 0:
                font = pygame.font.Font(None, FONT_SIZE)
                text = font.render(str(user_board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * 60 + 30, i * 60 + 30))
                screen.blit(text, text_rect)
            elif board[i][j] != 0:
                font = pygame.font.Font(None, FONT_SIZE)
                text = font.render(str(board[i][j]), True, BLUE)
                text_rect = text.get_rect(center=(j * 60 + 30, i * 60 + 30))
                screen.blit(text, text_rect)

    for i in range(10):
        line_thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * 60), (WIDTH, i * 60), line_thickness)
        pygame.draw.line(screen, BLACK, (i * 60, 0), (i * 60, HEIGHT - 60), line_thickness)


def get_cell(pos):
    """
    Returns the row and column of the clicked cell based on the mouse position.
    
    Args:
        pos (tuple): The (x, y) position of the mouse click.
    
    Returns:
        tuple: The row and column index of the cell.
    """
    x, y = pos
    return y // 60, x // 60


def handle_input(row, col, event):
    """
    Handles the user input for entering numbers into the Sudoku board.
    
    Args:
        row (int): The row of the selected cell.
        col (int): The column of the selected cell.
        event (pygame.event): The keyboard event to handle number input.
    """
    if event.unicode.isdigit():
        number = int(event.unicode)
        if 1 <= number <= 9:
            user_board[row][col] = number
        else:
            user_board[row][col] = 0


def reveal_solution():
    """
    Slowly reveals the solution by showing each number one by one.
    """
    for i in range(9):
        for j in range(9):
            if user_board[i][j] == 0 and board[i][j] != 0:
                user_board[i][j] = board[i][j]
                draw_board()
                pygame.display.update()
                time.sleep(0.1)


def main():
    """
    Main game loop for the Sudoku solver. Handles drawing the board, user input, and solving the puzzle.
    """
    selected_cell = None

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
                    if solve_button.collidepoint(event.pos):
                        solve(board)  
                        reveal_solution()  
                    else:
                        selected_cell = get_cell(event.pos)
            elif event.type == pygame.KEYDOWN and selected_cell:
                row, col = selected_cell
                handle_input(row, col, event)

        pygame.display.update()


if __name__ == "__main__":
    main()
