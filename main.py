"""
MAIN ENTRY POINT - Demonstrates the MVC Pattern in Action

This file shows how the Model, View, and Controller work together.
Students should NOT implement anything here - just understand how it demonstrates MVC.

GRAPHICS ENGINE: This game uses tkinter for graphics.
- tkinter comes built-in with Python (no installation needed)
- Import at the top of view.py: import tkinter as tk
- You'll use tk.Tk() for the window and Canvas for drawing shapes
"""

from model import (
    create_game_state,
)
from view import (
    create_display,
)
from controller import (
    create_controller,
    run_game,
)


# TODO: Understand how these layers work together
#
# The MVC Pattern separates concerns into three layers:
#
# 1. MODEL (model.py):
#    - create_game_state(): Creates a dictionary holding all game objects
#    - update_game_state(): Applies the rules of the game (physics, collisions)
#    - Paddle/Ball functions: Create and manipulate individual objects
#    - The Model doesn't know or care about displaying or input
#
# 2. VIEW (view.py):
#    - create_display(): Creates a window/canvas dictionary
#    - draw_paddle(), draw_ball(), etc.: Render game objects
#    - update_display(): Refreshes the screen with the current model state
#    - The View doesn't know or care about game logic or input
#
# 3. CONTROLLER (controller.py):
#    - create_controller(): Sets up the orchestration state
#    - handle_*_input(): Reads user input and updates the Model
#    - run_game(): The main game loop that coordinates everything
#    - The Controller connects input → Model → View
#
#
# Below is the ONLY code that ties the three layers together:
#

def main():
    # Configuration
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    FRAME_RATE = 60
    
    # Create the Model (game state)
    # This dictionary knows about the game rules and current state
    game_state = create_game_state(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Create the View (display)
    # This dictionary knows how to draw things on the screen
    display = create_display(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Create the Controller
    # This orchestrates the Model and View, running the game loop
    controller = create_controller(game_state, display, FRAME_RATE)
    
    # Run the game
    # This loop will:
    #   - Get input (Controller's job)
    #   - Update game logic (Model's job)
    #   - Draw everything (View's job)
    run_game(controller)


if __name__ == "__main__":
    main()
