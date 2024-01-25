"""
Utility Module
"""
class Node:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = None  # Reference to the canvas rectangle