# Sudoku Solver Game

## Description

This is a simple graphical Sudoku solver built using Python and Pygame. The application allows users to input numbers on a blank Sudoku grid and solve the puzzle by pressing the "Solve" button. The solver will attempt to complete the puzzle and display the results.

## Features

- Interactive 9x9 Sudoku board.
- Input numbers by clicking on the cells and typing.
- Solve the Sudoku puzzle with the press of a button.
- User-entered numbers are displayed in black, while solved numbers are displayed in blue.

## Requirements

- Python 3
- Pygame

## Installation

### Linux/macOS

1. **Clone the repository**:
    ```bash
    git clone https://github.com/azharxkhan/Sudoku-Solver.git
    cd sudoku-solver-game
    ```

2. **Make the Bash script executable**:
    Ensure the script has executable permissions:
    ```bash
    chmod +x sudoku_game.sh
    ```

3. **Run the setup script**:  
    The provided `sudoku_game.sh` script will:
    - Create a virtual environment.
    - Install the required dependencies (Pygame sudoku_game).
    - Run the application.
    ```bash
    ./sudoku_game.sh
    ```

    The game will start automatically once the setup completes.

### Windows

1. **Clone the repository**:
    Open the command prompt and run:
    ```cmd
    git clone https://github.com/your-repo/sudoku-solver-game.git
    cd sudoku-solver-game
    ```

2. **Run the batch file**:  
    The `setup_sudoku.bat` script will:
    - Create a virtual environment.
    - Install the required dependencies (Pygame sudoku_game).
    - Run the application.
    ```cmd
    setup_sudoku.bat
    ```

    The game will start automatically once the setup completes.

## Running the Game Manually

If you prefer to run the game manually after the setup:

- **For Linux/macOS**:  
    1. Make virtual environment(Must have pygame and venv installed):
    ```bash
    python3 -m venv venv
    ```
    2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
    3. Install the required dependencies:
    ```bash
    pip install pygame
    ```
    3. Run the game:
    ```bash
    python3 sudoku_game.py
    ```

- **For Windows**:  
    1. Activate the virtual environment:
    ```cmd
    venv\Scripts\activate
    ```
    2. Run the game:
    ```cmd
    python sudoku_game.py
    ```

## Usage

1. Start the game.
2. Click on any cell in the 9x9 grid to select it.
3. Enter numbers using your keyboard (1-9).
4. Press the "Solve" button to solve the puzzle.
5. Solved numbers will appear in blue, while user-entered numbers will remain black.

## File Structure

- `sudoku_game.py`: Main game file containing the game logic.
- `sudoku_solver.py`: That solves the sudoku and returns the numbers.
- `sudoku_game.sh`: Bash script to automate the setup and running of the game (Linux/macOS).
- `setup_sudoku.bat`: Windows batch script for setup and running the game.
