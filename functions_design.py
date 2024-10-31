import tkinter as tk

# Definition of colors and font styles
BLACK = "#000000"
WHITE = "#FFFFFF"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
ORANGE = "#FFA07A"
GRAY = "#A9A9A9"
DIMGEY = "#696969"

# Initializes the main window
window = tk.Tk()
window.geometry("375x667")  # Sets the size of the window
window.title('Calculator')  # Sets the title of the window
window.configure(bg=BLACK)  # Sets the background color

# Creates the frame for the calculator screen
frame = tk.Frame(window, height=221, bg=BLACK)  # Sets the black background for the screen
frame.pack(expand=True, fill='both')  # Allows the frame to expand and fill the available space

# Initializes the expressions to display
total_expression = "0"  # Initial total expression
current_expression = "0"  # Initial current expression

# Creates the label to display the total expression
total_label = tk.Label(
    frame,
    text=total_expression,  # Initial text of the total label
    anchor=tk.E,  # Anchors the text to the right
    bg=BLACK,  # Black background
    fg=WHITE,  # White text
    padx=24,  # Horizontal padding
    font=SMALL_FONT_STYLE  # Small font style
)
total_label.pack(expand=True, fill='both')  # Allows the total label to expand

# Creates the label to display the current expression
label = tk.Label(
    frame,
    text=current_expression,  # Initial text of the current label
    anchor=tk.E,  # Anchors the text to the right
    bg=BLACK,  # Black background
    fg=WHITE,  # White text
    padx=24,  # Horizontal padding
    font=LARGE_FONT_STYLE  # Large font style
)
label.pack(expand=True, fill='both')  # Allows the current label to expand

# Creates the frame for the buttons
button_frame = tk.Frame(window, bg=BLACK)  # Frame to hold the buttons
button_frame.pack(expand=True, fill='both')  # Allows the button frame to expand

# Button configuration
buttons = [
    chr(9003), "C", "√", "\u00F7",  
    "7", "8", "9", "\u00D7",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    ".", "0", "New", "="  
]

# Create the buttons in a grid
row, col = 0, 0
for button in buttons:
    # Assign background color based on the button
    if button in ['C', "√", chr(9003)]:  # If the button is C, √, or the back button
        button_color = GRAY
    elif button in ['\u00F7', '\u00D7', '-', '+', '=']:  # If it is an operator
        button_color = ORANGE
    else:  # For numbers and other buttons
        button_color = DIMGEY
    b = tk.Button(
        button_frame,
        text=button,
        bg=button_color,  # Assigns the button color
        fg=WHITE,  # White text
        font=SMALL_FONT_STYLE,
        borderwidth=0,
    )
    b.grid(row=row, column=col, sticky=tk.NSEW, padx=5, pady=5)  # Places the button in the grid
    col += 1  # Moves to the next column
    if col > 3:  # If the end of the row is reached
        col = 0  # Resets the column
        row += 1  # Moves to the next row

# Configures the weight of the rows and columns so that the buttons expand properly
for i in range(4):
    button_frame.columnconfigure(i, weight=1)  # Allows the columns to expand
for i in range(5):
    button_frame.rowconfigure(i, weight=1)  # Allows the rows to expand

# Starts the main loop of the window
window.mainloop()
