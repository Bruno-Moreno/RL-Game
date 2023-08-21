import numpy as np 
from itertools import product
import random

class Grid:
    def __init__(self, height, width):

        self.height = height
        self.width = width

        self.grid = np.zeros((self.height, self.width))

        self.snake_position = []
        self.fruit_position = None 

    def show(self):

        print(self.grid)

    def update_grid(self, snake_position):

        # Restart Grid
        self.grid = np.zeros((self.height, self.width))

        # Fruit Position
        x = self.fruit_position[0]
        y = self.fruit_position[1]

        self.grid[x][y] = -1.0

        # Snake Position
        self.snake_position = snake_position
        for p in snake_position:
            x = p[0]
            y = p[1]
            self.grid[x][y] = 1.0

        # Si la serpiente se comió la fruta, crear una nueva
        if self.grid.min() != -1.0:
            self.create_fruit()

    def create_fruit(self):

        positions_x = set(range(self.height))
        positions_y = set(range(self.width))

        positions  = list(product(positions_x, positions_y))

        possible_positions = [p for p in positions if p not in self.snake_position]

        if len(possible_positions) > 0: 

            self.fruit_position = random.choice(possible_positions)
            x = self.fruit_position[0]
            y = self.fruit_position[1]
            self.grid[x][y] = -1.0

        else:
            self.fruit_position = (-1,-1)