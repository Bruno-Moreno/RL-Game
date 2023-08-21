from game.game import Game

snake_length = 3 
grid_height = 5 
grid_width = 5 

if __name__ == "__main__":

    game = Game(snake_length, grid_height, grid_width)
    game.start_game()
