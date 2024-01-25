"""
The food module
"""
import random


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.rect = None
        self.generate_food()

    def generate_food(self):
        # Check if the old food item exists and delete it
        if self.rect is not None:
            self.canvas.delete(self.rect)

        # Wait until the canvas has a valid width and height
        while self.canvas.winfo_width() == 1 or self.canvas.winfo_height() == 1:
            self.canvas.update()

        # Calculate the maximum valid range for the food position
        max_x_range = self.canvas.winfo_width() // 20 - 1
        max_y_range = self.canvas.winfo_height() // 20 - 1

        # Generate random coordinates for the food
        self.x = random.randint(0, max_x_range) * 20
        self.y = random.randint(0, max_y_range) * 20

        # Create a rectangle for the new food
        self.rect = self.canvas.create_rectangle(
            self.x, self.y, self.x + 20, self.y + 20, fill="red", tags="food"
        )