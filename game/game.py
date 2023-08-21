import os 
from game.snake import Snake
from game.grid import Grid

class Game:
    def __init__(self, snake_length, grid_height, grid_width):

        self.snake = Snake(snake_length = snake_length)
        self.grid = Grid(height = grid_height, width = grid_width)

    def start_game(self):

        self.grid.create_fruit()
        self.grid.update_grid(self.snake.snake_position)
        self.grid.show()

        for _ in range(100):

            direction = input("Ingrese su próximo movimiento (right, left, up, down): ")
            os.system('clear')
            result = self.snake.move(direction=direction, grid = self.grid)
            if result == -1.0:
                print("Game Over")
                break

            self.grid.update_grid(self.snake.snake_position)
            self.grid.show()
