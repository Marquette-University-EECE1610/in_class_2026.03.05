"""
VIEW LAYER - Display and Rendering

The View is responsible for:
- Creating and managing the display window
- Drawing all game objects (paddles, ball, court boundaries)
- Updating the screen to show the current state
- Being independent from game logic - it just draws what it's told to draw

Functional approach: Functions take display state and game state, and perform rendering.

GRAPHICS ENGINE: This game uses tkinter for graphics.
- tkinter comes built-in with Python (no installation needed)
- You will need to import tkinter.Tk for the window
- You will need tkinter.Canvas to draw rectangles and circles
- Example imports at the top of this file:
    import tkinter as tk
    from tkinter import Canvas
"""


# TODO 1: Create a function to initialize the display window
# Purpose: Set up the game window that will display the pong game
# Parameters:
#   - width: the window width
#   - height: the window height
# Returns:
#   - A display state dictionary with keys: 'window', 'canvas', 'width', 'height'
# Requirements:
#   - Create a tkinter.Tk window (root window)
#   - Create a tkinter.Canvas on that window with the given dimensions
#   - Set the canvas background color to black
#   - Give the window a title (e.g., "Pong Game")
# Tkinter hints:
#   - root = tk.Tk()
#   - canvas = Canvas(root, width=width, height=height, bg='black')
#   - canvas.pack()
#   - root.title("Pong Game")

def create_display(width, height):
    pass  # TODO: Create and initialize the display window


# TODO 2: Create a function to draw a paddle
# Purpose: Render a paddle (a rectangle) at a given position
# Parameters:
#   - display: the display state dictionary (should have 'canvas' key)
#   - paddle: a paddle dictionary with x, y, width, height
# What to do:
#   - Use the tkinter canvas to draw a rectangle at the paddle's position
#   - Use white color (or any contrasting color) for the paddle
# Tkinter hints:
#   - display['canvas'].create_rectangle(x1, y1, x2, y2, fill='white')
#   - x1, y1 is the top-left corner
#   - x2, y2 is the bottom-right corner
#   - You'll need to calculate these from paddle['x'], paddle['y'], width, height

def draw_paddle(display, paddle):
    pass  # TODO: Draw the paddle rectangle


# TODO 3: Create a function to draw the ball
# Purpose: Render the ball (a circle) at a given position
# Parameters:
#   - display: the display state dictionary (should have 'canvas' key)
#   - ball: a ball dictionary with x, y, radius
# What to do:
#   - Use the tkinter canvas to draw a circle (oval) at the ball's position
#   - Use white color (or any contrasting color) for the ball
# Tkinter hints:
#   - display['canvas'].create_oval(x1, y1, x2, y2, fill='white')
#   - For a circle at (center_x, center_y) with radius r:
#     x1 = center_x - r
#     y1 = center_y - r
#     x2 = center_x + r
#     y2 = center_y + r

def draw_ball(display, ball):
    pass  # TODO: Draw the ball circle


# TODO 4: Create a function to draw the court (optional but nice)
# Purpose: Render visual elements of the game court (center line, boundaries)
# Parameters:
#   - display: the display state dictionary (should have 'canvas' key)
# What to do:
#   - Draw a dashed/dotted line down the center of the screen (optional)
#   - Draw boundary lines at top and bottom (optional)
# Note: This is purely visual - it doesn't affect gameplay
# Tkinter hints:
#   - display['canvas'].create_line(x1, y1, x2, y2, fill='white')
#   - For center line: from (width/2, 0) to (width/2, height)

def draw_court(display):
    pass  # TODO: Draw court boundaries and center line


# TODO 5: Create a function to update the entire display
# Purpose: Render a complete frame of the game
# Parameters:
#   - display: the display state dictionary (should have 'canvas' key)
#   - game_state: a game state dictionary containing paddles and ball
# What to do:
#   1. Clear the canvas (erase the previous frame)
#   2. Call draw_court(display)
#   3. Draw both paddles: draw_paddle(display, game_state['left_paddle'])
#                         draw_paddle(display, game_state['right_paddle'])
#   4. Draw the ball: draw_ball(display, game_state['ball'])
#   5. Update/refresh the tkinter window so the new frame appears
# Tkinter hints:
#   - display['canvas'].delete('all')  # Clears the canvas
#   - display['canvas'].update()  # Updates the display
# Note: This function should be called once per game loop iteration

def update_display(display, game_state):
    pass  # TODO: Implement the update/refresh logic


# TODO 6: Create a function to check if the window is still open
# Purpose: Determine if the game should continue or if the user closed the window
# Parameters:
#   - display: the display state dictionary (should have 'window' key)
# Returns:
#   - True if the window is still open, False if it's been closed
# Tkinter hints:
#   - display['window'].winfo_exists() returns True if the window is open
#   - This checks if the user clicked the close button

def is_display_open(display):
    pass  # TODO: Check if the display window is still open


# TODO 7: Create a function to close/cleanup the display
# Purpose: Gracefully shut down the display
# Parameters:
#   - display: the display state dictionary (should have 'window' key)
# Returns:
#   - None
# What to do:
#   - Destroy the tkinter window
#   - Clean up any graphics resources
# Tkinter hints:
#   - display['window'].destroy()  # Closes the window

def close_display(display):
    pass  # TODO: Implement display cleanup
