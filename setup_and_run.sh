#!/bin/bash

# ---------------------------------------------
# Bash script to set up a virtual environment,
# install required dependencies, and run the 
# Sudoku game application on Linux/macOS.
# ---------------------------------------------

# Step 1: Create a virtual environment named 'venv'
echo "Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Upgrade pip to the latest version
echo "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install necessary dependencies (pygame and sudoku_solver)
echo "Installing dependencies..."
pip install pygame

# Step 5: Run the application
echo "Running the Sudoku game..."
python3 sudoku_game.py

# Step 6: Deactivate the virtual environment after the game ends
echo "Deactivating virtual environment..."
deactivate

echo "Setup complete and game finished."
