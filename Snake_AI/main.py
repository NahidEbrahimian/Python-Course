import arcade
from apple import Apple
from snake import Snake
import config


class Game(arcade.Window):
    def __init__(self, width, height):
        arcade.Window.__init__(self, width, height, 'snake')
        arcade.set_background_color(arcade.color.DARK_GRAY)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.exit = 0

    def on_draw(self):
        # display objects in game
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()

        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.DARK_BLUE_GRAY, 14)

        # collision with the wall
        if (600 <= self.snake.center_x + self.snake.r) or (0 >= self.snake.center_x - self.snake.r) or (400 <= self.snake.center_y + self.snake.r) or (0 >= self.snake.center_y - self.snake.r):
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.exit = 1

    def on_update(self, delta_time: float):
        # display events during game
        self.snake.move()

        # Apple position
        if self.apple.center_x - 10 <= self.snake.center_x <= self.apple.center_x + 10 and self.apple.center_y - 10 <= self.snake.center_y <= self.apple.center_y + 10 :
            self.snake.eat()
            self.apple = Apple(600, 400)

        # Snake: Collision with body
        if self.snake.score > 1:
            for i in range (len(self.snake.body) - 1):
                if self.snake.center_x == self.snake.body[i][0] and self.snake.center_y == self.snake.body[i][1]:
                    self.snake = Snake(config.width, config.height)
                    break

        direction = self.snake.vision(self.apple)
        self.snake.decision(direction)

        # Snake: Collision with wall
        if self.snake.collision_with_wall(self.snake.direction):
            if self.snake.direction == 0:
                direction = 2

            elif self.snake.direction == 2:
                direction = 1

            elif self.snake.direction == 3:
                direction = 0

            elif self.snake.direction == 1:
                direction = 3

            if self.snake.collision_with_wall(direction):

                if self.snake.direction == 0:
                    direction = 3

                elif self.snake.direction == 2:
                    direction = 30

                elif self.snake.direction == 3:
                    direction = 1

                elif self.snake.direction == 1:
                    direction = 2

                if self.snake.collision_with_wall(direction):
                    self.snake = Snake()

            self.snake.direction = direction



game = Game(config.width, config.height)
arcade.run()