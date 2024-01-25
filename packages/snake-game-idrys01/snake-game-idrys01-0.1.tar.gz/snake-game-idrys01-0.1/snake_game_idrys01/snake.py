"""
Snake module
"""
from utility import Node
from food import Food
import uuid


class Snake:
    def __init__(self, canvas, score_label):
        self.canvas = canvas
        self.segments = [Node(100, 100, "green"), Node(90, 100, "blue")]
        self.food = Food(self.canvas)
        self.direction = "Right"
        self.score = 0

        # Create a label for the score display
        self.score_label = score_label
        self.update_score_display()

        # Speed setting
        self.speed = 100  # Default speed
        self.move_snake_after_id = None  # Store the ID of the move_snake after() method

        # Game state
        self.is_playing = False

        self.update_speed()

    def move_snake(self):
        if self.is_playing:
            self.move()
            self.score_label.config(text=f"Score: {self.score}")  # Update score display on the label
        self.move_snake_after_id = self.canvas.after(self.speed, self.move_snake)

    def set_speed(self, speed):
        self.speed = speed
        self.update_speed()

    def update_speed(self):
        # Cancel the previous move_snake timer, if any
        if self.move_snake_after_id is not None:
            self.canvas.after_cancel(self.move_snake_after_id)

        # Restart the timer with the updated speed
        self.move_snake_after_id = self.canvas.after(self.speed, self.move_snake)

    def create_block(self, x, y, color):
        tag = "snake_{}".format(str(uuid.uuid4()).replace('-', "")[:5])
        return self.canvas.create_rectangle(x, y, x + 20, y + 20, fill=color, tags=tag)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i-1].x
            self.segments[i].y = self.segments[i-1].y

        if self.direction == "Up":
            self.segments[0].y -= 20
        elif self.direction == "Down":
            self.segments[0].y += 20
        elif self.direction == "Left":
            self.segments[0].x -= 20
        elif self.direction == "Right":
            self.segments[0].x += 20

        # Check if the head collides with the body
        if self.check_body_collision():
            self.end_game() 


        # Check if the head collides with the food
        if self.check_food_collision():
            self.score += 10  # Increase score by a certain value
            self.update_score_display()  # Update score display
            new_node = Node(0, 0, "blue")  # Add a new node to the tail
            self.segments.append(new_node)
            self.food.generate_food()  # Generate a new position for the food
            new_node.rect = self.create_block(new_node.x, new_node.y, new_node.color)

        # Check if the head is beyond the canvas boundaries
        if self.segments[0].x < 0:
            self.segments[0].x = self.canvas.winfo_width() - 20
        elif self.segments[0].x >= self.canvas.winfo_width():
            self.segments[0].x = 0

        if self.segments[0].y < 0:
            self.segments[0].y = self.canvas.winfo_height() - 20
        elif self.segments[0].y >= self.canvas.winfo_height():
            self.segments[0].y = 0

        for segment in self.segments:
            coords = [segment.x, segment.y, segment.x + 20, segment.y + 20]
            self.canvas.coords(segment.rect, *coords)

    def direction_check(self, new_direction):
        # Ensure the snake cannot move directly opposite its current direction
        if (new_direction == "Up" and not self.direction == "Down") or \
           (new_direction == "Down" and not self.direction == "Up") or \
           (new_direction == "Left" and not self.direction == "Right") or \
           (new_direction == "Right" and not self.direction == "Left"):
            self.direction = new_direction


    def check_food_collision(self):
        # Check if the head collides with the food
        if not self.segments or not self.segments[0].rect or not self.food.rect:
            return False

        head_coords = self.canvas.coords(self.segments[0].rect)
        food_coords = self.canvas.coords(self.food.rect)

        return (
            head_coords[0] < food_coords[2] and
            head_coords[2] > food_coords[0] and
            head_coords[1] < food_coords[3] and
            head_coords[3] > food_coords[1]
        )

    def update_score_display(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_body_collision(self):
        # Check if the head collides with any part of the body
        head_id = self.segments[0].rect
        for segment in self.segments[1:]:
            body_id = segment.rect
            if self.canvas.coords(head_id) == self.canvas.coords(body_id):
                return True
        return False


    def end_game(self):
        self.is_playing = False

        # Reset the score
        self.score = 0
        self.update_score_display()

        # Clear existing snake segments from the canvas
        for segment in self.segments:
            self.canvas.delete(segment.rect)

        # Recreate the initial snake size
        initial_segments = [Node(100, 100, "green"), Node(90, 100, "blue")]
        self.segments = initial_segments

        # Recreate canvas rectangles for each snake segment
        for segment in self.segments:
            segment.rect = self.create_block(segment.x, segment.y, segment.color)

        # Stop the timer
        if self.move_snake_after_id is not None:
            self.canvas.after_cancel(self.move_snake_after_id)
            self.move_snake_after_id = None