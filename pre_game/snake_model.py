import numpy as np 

from grid import Grid
from snake import Snake

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten

class SnakeModel:
    def __init__(self, snake_length, grid_height, grid_width):

        self.model = None
        self.snake_length = snake_length
        self.grid_height = grid_height
        self.grid_width = grid_width

        self.direction_dict = {0: "up", 1: "down", 2: "left", 3: "right"}


    def create_model(self, shape):
       
        model = Sequential()
        model.add(Dense(100 , input_shape = (shape, ), activation = "relu"))
        model.add(Dense(50 , activation = "tanh"))
        model.add(Dense(4 , activation = "softmax"))

        print(model.summary())
        self.model = model

    def train_model(self, train_iterations):
        
        # Create the snake and the grid
        snake = Snake(snake_length = self.snake_length)
        grid = Grid(height = self.grid_height, width = self.grid_width)

        grid.create_fruit()
        grid.update_grid(snake.snake_position)
        grid.show()

        for i in range(train_iterations):

            print(f"################### Iteración {i} #####################")

            X = np.expand_dims(grid.grid.flatten(), axis=0)
            prediction_vector = self.model.predict(X)
            prediction_value = prediction_vector.argmax()

            direction = self.direction_dict[prediction_value]
            print(f"La red decide moverse a: {direction}")
            result = snake.move(direction=direction, grid = grid)
            print(result)
            grid.update_grid(snake.snake_position)
            grid.show()



if __name__ == "__main__":

    snake_length = 2
    grid_height = 5
    grid_width = 5
    snake_model = SnakeModel(snake_length, grid_height, grid_width)
    snake_model.create_model(shape = grid_height * grid_width)
    snake_model.train_model(train_iterations = 3)