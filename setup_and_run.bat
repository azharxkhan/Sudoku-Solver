@echo off

REM ---------------------------------------------
REM Batch script to set up a virtual environment,
REM install required dependencies, and run the 
REM Sudoku game application on Windows.
REM ---------------------------------------------

REM Step 1: Create a virtual environment named 'venv'
echo Creating virtual environment...
python -m venv venv

REM Step 2: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Step 3: Upgrade pip to the latest version
echo Upgrading pip...
pip install --upgrade pip

REM Step 4: Install necessary dependencies (pygame and sudoku_solver)
echo Installing dependencies...
pip install pygame

REM Step 5: Run the application
echo Running the Sudoku game...
python sudoku_game.py

REM Step 6: Deactivate the virtual environment after the game ends
echo Deactivating virtual environment...
call venv\Scripts\deactivate

echo Setup complete and game finished.
pause
