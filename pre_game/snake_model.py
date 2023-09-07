import numpy as np 

from grid import Grid
from snake import Snake

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
import keras


class SnakeModel:
    def __init__(self, snake_length, grid_height, grid_width):

        self.snake_length = snake_length
        self.grid_height = grid_height
        self.grid_width = grid_width

        self.direction_dict = {0: "up", 1: "down",
                               2: "left", 3: "right"
                               }

        self.model = None
        self.snake = None
        self.grid = None

    def create_snake_and_grid(self):

        # Create the snake and the grid
        self.snake = Snake(snake_length = self.snake_length)
        self.grid = Grid(height = self.grid_height, width = self.grid_width)

        self.grid.create_fruit()
        self.grid.update_grid(self.snake.snake_position)
        self.grid.show()
        
    def custom_loss(self, y_true, y_pred):

        # Minimizar la Loss, y_true = 0- En caso de Victoria, loss = -1, en Derrota, loss = 1, en Neutro, loss = 0
        loss = -tf.reduce_sum((y_pred - y_true))
        print(loss)

        return loss

    def create_model(self, shape):
       
        model = Sequential()
        model.add(Dense(100 , input_shape = (shape, ), activation = "relu"))
        model.add(Dense(50 , activation = "tanh"))
        model.add(Dense(4 , activation = "softmax"))

        model.compile(loss = self.custom_loss, optimizer='adam', run_eagerly=True)
        print(model.summary())
        self.model = model

    def train(self, epochs):

        optimizer = keras.optimizers.SGD(learning_rate=1e-3)

        print("#################### Training Start #################")

        for epoch in range(epochs):

            print("\nStart of epoch %d" % (epoch,))

            with tf.GradientTape() as tape:

                # Network Forward
                X = np.expand_dims(self.grid.grid.flatten(), axis=0)
                y_pred_vector = self.model(X, training=True)

                # Obtener la predicción
                prediction_value = tf.argmax(y_pred_vector, axis=1)
                print(y_pred_vector)
                print(prediction_value)

                # Mover la Serpiente
                direction = self.direction_dict[prediction_value.numpy()[0]]
                print(f"Dirección: {direction}")

                result = self.snake.move(direction=direction, grid = self.grid)
                print(f"Resultado: {result}")

                # Actualizar el tablero
                self.grid.update_grid(self.snake.snake_position)
                self.grid.show()
                
                # Resetear si es necesario
                if result == -1:
                    print("Reset")
                    self.create_snake_and_grid()

                # Computar la loss
                y_pred = tf.convert_to_tensor([result], dtype='float32')

                y_true_array = np.array([0.0]).reshape((-1,1))
                y_true = tf.convert_to_tensor(y_true_array, dtype='float32')

                loss_value = self.custom_loss(y_true, y_pred)

            # Use the gradient tape to automatically retrieve
            # the gradients of the trainable variables with respect to the loss.
            grads = tape.gradient(loss_value, self.model.trainable_weights)

            # Run one step of gradient descent by updating
            # the value of the variables to minimize the loss.
            optimizer.apply_gradients(zip(grads, self.model.trainable_weights))


if __name__ == "__main__":

    snake_length = 2
    grid_height = 5
    grid_width = 5
    epochs = 3

    snake_model = SnakeModel(snake_length, grid_height, grid_width)
    snake_model.create_snake_and_grid()
    snake_model.create_model(shape = grid_height * grid_width)
    snake_model.train(epochs = epochs)