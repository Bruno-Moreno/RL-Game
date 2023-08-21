class Snake:

  def __init__(self, snake_length):

    self.snake_position = [(0,i) for i in range(snake_length)]
    self.snake_direction = "right"

  def move(self, direction, grid):

    # Validamos que el movimiento no sea en contra de la dirección de la cabeza (giro 180)
    actual_direction = self.snake_direction

    if (direction == "up" and actual_direction == "down") or (direction == "down" and actual_direction == "up") or (direction == "right" and actual_direction == "left") or (direction == "left" and actual_direction == "right"):

      direction = actual_direction
    
    # Creamos la nueva posición de la cabeza

    if direction == "up":
      new_head_position = (self.snake_position[-1][0] - 1, self.snake_position[-1][1])

    elif direction == "right":
      new_head_position = (self.snake_position[-1][0], self.snake_position[-1][1] + 1)

    elif direction == "down":
      new_head_position = (self.snake_position[-1][0] + 1, self.snake_position[-1][1])

    elif direction == "left":
      new_head_position = (self.snake_position[-1][0], self.snake_position[-1][1] - 1)

    else:

      return -1.0

    # Validamos esta nueva posición
    height = grid.grid.shape[0]
    width = grid.grid.shape[1]

    if new_head_position[0] == height or new_head_position[0] == -1.0 or new_head_position[1] == width or new_head_position[1] == -1.0:
    
      return -1.0
    
    if (new_head_position[0], new_head_position[1]) in self.snake_position:

      return -1.0
    
    self.snake_direction = direction

    # Ver si toca una fruta
    if grid.grid[new_head_position[0]][new_head_position[1]] != -1.0:
      self.snake_position.pop(0) # Eliminar la cola
      self.snake_position.append(new_head_position)  # Mover la cabeza

      return 0.0

    else: 
      self.snake_position.append(new_head_position) # Mover la cabeza

      return 1.0

  
  def eat_animal(self, animal_position):

    self.snake_position.append(animal_position)
