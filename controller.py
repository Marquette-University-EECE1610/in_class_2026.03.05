"""
CONTROLLER LAYER - Input Handling and Game Orchestration

The Controller is responsible for:
- Capturing user input (keyboard)
- Updating the Model based on input
- Calling the View to display the current state
- Running the game loop that ties everything together

Functional approach: Functions handle input and orchestration, returning updated state.

GRAPHICS ENGINE: This game uses tkinter. 
- Use tkinter's event system to capture keyboard input
- You may need to use display['window'].bind() to handle key events
- Or use display['window'].winfo_children() and polling for a simpler approach
"""


# TODO 1: Create a function to handle keyboard input for the left paddle
# Purpose: Read which keys are pressed and update the left paddle position
# Parameters:
#   - game_state: the current game state dictionary
#   - screen_height: the height of the game screen (for clamping)
# Returns:
#   - The updated game_state dictionary with left paddle possibly moved
# Typical keys:
#   - 'W' or 'UP' to move paddle up (dy = negative)
#   - 'S' or 'DOWN' to move paddle down (dy = positive)
# Notes:
#   - You may need to track which keys are currently pressed (event-based or polling)
#   - Use move_paddle() from model.py to update the paddle position
#   - Update game_state['left_paddle'] with the result

def handle_left_paddle_input(game_state, screen_height):
    pass  # TODO: Implement left paddle input handling


# TODO 2: Create a function to handle keyboard input for the right paddle
# Purpose: Read which keys are pressed and update the right paddle position
# Parameters:
#   - game_state: the current game state dictionary
#   - screen_height: the height of the game screen (for clamping)
# Returns:
#   - The updated game_state dictionary with right paddle possibly moved
# Typical keys:
#   - 'UP' arrow or 'I' to move paddle up (dy = negative)
#   - 'DOWN' arrow or 'K' to move paddle down (dy = positive)
# Notes:
#   - Similar to left paddle, but different key bindings
#   - Use move_paddle() from model.py to update the paddle position
#   - Update game_state['right_paddle'] with the result

def handle_right_paddle_input(game_state, screen_height):
    pass  # TODO: Implement right paddle input handling


# TODO 3: Create a function to initialize the game controller
# Purpose: Set up the controller with all necessary state
# Parameters:
#   - game_state: the game state dictionary from model.py
#   - display: the display state dictionary from view.py
#   - frame_rate: the target frames per second (default 60)
# Returns:
#   - A controller state dictionary with keys: 'game_state', 'display', 'frame_rate',
#                                              'running', 'clock' (or timing mechanism)

def create_controller(game_state, display, frame_rate=60):
    pass  # TODO: Initialize the controller state


# TODO 4: Create the main game loop function
# Purpose: This is the heart of the game - it runs repeatedly until the game ends
# Parameters:
#   - controller: the controller state dictionary
# What to do:
#   1. While the game is running (is_display_open() from view.py returns True):
#       a. Handle input for both paddles (call handle_left_paddle_input and handle_right_paddle_input)
#       b. Update the model (call update_game_state() from model.py)
#       c. Update the display (call update_display() from view.py)
#       d. Control speed/frame rate so it's not too fast (use time.sleep or pygame.time.Clock)
#   2. When the window closes, cleanly exit
# Returns:
#   - None (or optionally return the final game_state)
# Hint: You may need a clock/timing mechanism to control frame rate
#       (e.g., pygame.time.Clock or time.sleep())

def run_game(controller):
    pass  # TODO: Implement the main game loop


# TODO 5: Create a function to gracefully shut down the game
# Purpose: Clean up resources when the game ends
# Parameters:
#   - controller: the controller state dictionary
# What to do:
#   1. Close the display (call close_display() from view.py)
#   2. Set 'running' to False in the controller
#   3. Clean up any other resources

def quit_game(controller):
    pass  # TODO: Implement graceful shutdown
