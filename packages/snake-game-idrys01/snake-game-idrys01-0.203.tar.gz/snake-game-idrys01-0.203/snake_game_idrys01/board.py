"""
Board Module
"""
import tkinter as tk
from .snake import Snake


class Board:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="top", anchor="ne", padx=10, pady=10)

        # Create a label for the score display
        self.score_label = tk.Label(self.button_frame, text="Score: 0", font=("Helvetica", 16), bg="gray", fg="white")
        self.score_label.pack(side="left", padx=(0, 10))  # Add padding to the right

        # Play button
        self.play_button = tk.Button(self.button_frame, text="Play", command=self.toggle_play)
        self.play_button.pack(side="right")

        # Get screen width
        screen_width = self.master.winfo_screenwidth()

        # Calculate the square size (width and height of each square in the snake)
        square_size = 20  # Adjust as needed

        # Calculate the window size as a multiple of the square size
        window_size = max(400, int(screen_width * 0.4))
        window_size = (window_size // square_size) * square_size

        # Canvas for drawing (maintaining a square window)
        self.canvas = tk.Canvas(self.master, width=window_size, height=window_size, borderwidth=0, highlightthickness=0, bg="gray")
        self.canvas.pack()

        # Snake instance
        self.snake = Snake(self.canvas, self.score_label)

        # Create canvas rectangles for each snake segment
        for segment in self.snake.segments:
            segment.rect = self.create_block(segment.x, segment.y, segment.color)

        # Game state
        self.is_playing = False

        # Bind arrow key presses to methods
        self.master.bind("<Up>", lambda event: self.snake.direction_check("Up"))
        self.master.bind("<Down>", lambda event: self.snake.direction_check("Down"))
        self.master.bind("<Left>", lambda event: self.snake.direction_check("Left"))
        self.master.bind("<Right>", lambda event: self.snake.direction_check("Right"))

        # Level options
        self.level_var = tk.StringVar(value="easy")
        self.level_label = tk.Label(self.button_frame, text="Level:")
        self.level_label.pack(side="right")
        self.level_easy = tk.Radiobutton(self.button_frame, text="Easy", variable=self.level_var, value="easy", command=self.set_level)
        self.level_easy.pack(side="right")
        self.level_medium = tk.Radiobutton(self.button_frame, text="Medium", variable=self.level_var, value="medium", command=self.set_level)
        self.level_medium.pack(side="right")
        self.level_hard = tk.Radiobutton(self.button_frame, text="Hard", variable=self.level_var, value="hard", command=self.set_level)
        self.level_hard.pack(side="right")

        # Set up a timer to move the snake
        self.move_snake()


    def create_block(self, x, y, color):
        return self.canvas.create_rectangle(
            x, y, x + 20, y + 20, fill=color, tags="snake"
        )

    def move_snake(self):
        if self.is_playing:
            self.snake.move()
            self.score_label.config(text=f"Score: {self.snake.score}")
        self.master.after(100, self.move_snake)

    
    def set_level(self):
        # Update the level based on the selected option
        level = self.level_var.get()
        if level == "easy":
            self.snake.set_speed(100)  # Adjust as needed
        elif level == "medium":
            self.snake.set_speed(75)  # Adjust as needed
        elif level == "hard":
            self.snake.set_speed(50)  # Adjust as needed
    
    def restart_game(self):
        # Reset the game state
        self.is_playing = False
        self.play_button.config(text="Play")  # Update play button text

        # Reset the snake and its segments
        self.snake = Snake(self.canvas, self.score_label)

        # Remove existing snake segments from the canvas
        for segment in self.snake.segments:
            self.canvas.delete(segment.rect)

    def toggle_play(self):
        self.is_playing = not self.is_playing

        if not self.is_playing:
            new_text = "Play"
        else:
            new_text = "Pause"

        self.play_button.config(text=new_text)