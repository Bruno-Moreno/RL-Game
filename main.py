from pre_game.game import Game

snake_length = 2 
grid_height = 4
grid_width = 4

if __name__ == "__main__":

    game = Game(snake_length, grid_height, grid_width)
    game.start_game_player()
