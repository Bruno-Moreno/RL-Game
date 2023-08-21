from pre_game.game import Game

snake_length = 6 
grid_height = 10 
grid_width = 10

if __name__ == "__main__":

    game = Game(snake_length, grid_height, grid_width)
    game.start_game()
