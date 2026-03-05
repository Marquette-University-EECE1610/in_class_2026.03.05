"""
MODEL LAYER - Game Logic and State Management

The Model is responsible for:
- Storing the current state of the game (positions, velocities, etc.)
- Managing game logic (collision detection, position updates, physics)
- Being independent from how the game is displayed or how input is handled

Functional approach: Game state is stored in dictionaries, and functions operate on those dictionaries.
"""


# TODO 1: Create a function to initialize a Paddle
# Purpose: Create a paddle data structure
# Parameters:
#   - x: the x position (left or right side of screen)
#   - y: the y position (vertical center)
#   - width: the width of the paddle
#   - height: the height of the paddle
# Returns:
#   - A dictionary with keys: 'x', 'y', 'width', 'height'
# Notes:
#   - Paddles only move up/down, so x should never change
#   - Store the paddle dimensions in the dictionary

def create_paddle(x, y, width, height):
    pass  # TODO: Implement and return a paddle dictionary


# TODO 2: Create a function to move a paddle
# Purpose: Update a paddle's y position
# Parameters:
#   - paddle: a paddle dictionary
#   - dy: change in y (positive = down, negative = up)
#   - screen_height: the height of the game screen (to clamp movement)
# Returns:
#   - The updated paddle dictionary
# Notes:
#   - Make sure the paddle can't move above y=0 or below y=screen_height
#   - Don't modify the input; return a new/updated dictionary

def move_paddle(paddle, dy, screen_height):
    pass  # TODO: Implement paddle movement with boundary checking


# TODO 3: Create a function to initialize a Ball
# Purpose: Create a ball data structure
# Parameters:
#   - x: the x position (center)
#   - y: the y position (center)
#   - radius: the radius of the ball
#   - velocity_x: speed in x direction
#   - velocity_y: speed in y direction
# Returns:
#   - A dictionary with keys: 'x', 'y', 'radius', 'velocity_x', 'velocity_y'

def create_ball(x, y, radius, velocity_x, velocity_y):
    pass  # TODO: Implement and return a ball dictionary


# TODO 4: Create a function to update the ball's position
# Purpose: Move the ball based on its velocity
# Parameters:
#   - ball: a ball dictionary
# Returns:
#   - The updated ball dictionary with new x and y positions
# Notes:
#   - New position = current position + velocity
#   - Don't modify the input; return a new/updated dictionary

def update_ball_position(ball):
    pass  # TODO: Update ball.x and ball.y based on velocities


# TODO 5: Create functions to reverse ball velocity
# Purpose: Handle ball bounces
# Parameters:
#   - ball: a ball dictionary
# Returns:
#   - The updated ball dictionary with reversed velocity component

def bounce_ball_x(ball):
    pass  # TODO: Reverse ball's velocity_x


def bounce_ball_y(ball):
    pass  # TODO: Reverse ball's velocity_y


# TODO 6: Create a function to initialize the game state
# Purpose: Set up all game data
# Parameters:
#   - screen_width: width of the game screen
#   - screen_height: height of the game screen
# Returns:
#   - A dictionary containing:
#       - 'left_paddle': the left paddle dictionary
#       - 'right_paddle': the right paddle dictionary
#       - 'ball': the ball dictionary
#       - 'screen_width': the screen width
#       - 'screen_height': the screen height
# Notes:
#   - Place paddles on left and right sides
#   - Place ball in center with initial velocity

def create_game_state(screen_width, screen_height):
    pass  # TODO: Create and initialize the game state dictionary


# TODO 7: Create a function to reset the game
# Purpose: Put everything back to starting position
# Parameters:
#   - game_state: the current game state dictionary
# Returns:
#   - A reset game_state dictionary with ball centered and velocities reset

def reset_game_state(game_state):
    pass  # TODO: Reset ball position and velocity


# TODO 8: Create a helper function to check Ball-Paddle collision
# Purpose: Determine if the ball hit a paddle
# Parameters:
#   - ball: the ball dictionary
#   - paddle: the paddle dictionary
# Returns:
#   - True if the ball is touching the paddle, False otherwise
# What to check:
#   - Is the ball's x position near the paddle's x position?
#   - Is the ball's y position within the paddle's top and bottom?

def check_paddle_collision(ball, paddle):
    pass  # TODO: Implement collision detection logic


# TODO 9: Create the main game update function
# Purpose: Update all game state each frame
# Parameters:
#   - game_state: the current game state dictionary
# Returns:
#   - The updated game_state dictionary after applying all game rules
# What to do:
#   1. Update the ball position (call update_ball_position())
#   2. Check if ball hit top/bottom wall and bounce if needed (check ball.y)
#   3. Check if ball hit left/right paddle and bounce if needed (check_paddle_collision())
#   4. Check if ball went off-screen and reset if needed
#   5. Return the updated game_state

def update_game_state(game_state):
    pass  # TODO: Implement the complete game update logic
