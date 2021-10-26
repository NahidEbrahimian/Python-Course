import math
import arcade
from apple import Apple
from snake import Snake
from pear import Pear
from bomb import Bomb
import config


class Game(arcade.Window):
    def __init__(self, width, height):
        arcade.Window.__init__(self, width, height, 'snake')
        arcade.set_background_color(arcade.color.DARK_GRAY)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.pear = Pear(width, height)
        self.bomb = Bomb(width, height)
        self.exit = 0
        self.flag = 0

    def on_draw(self):
        # display objects in game
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.bomb.draw()

        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.DARK_BLUE_GRAY, 14)

        # minimum score
        if self.snake.score != 0:
            self.flag = 1

        if self.flag == 1 and self.snake.score <= 0:
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.snake = Snake(config.width, config.height)
            self.flag = 0
            # self.exit = 1

        # collision with the wall
        if (config.width <= self.snake.center_x + self.snake.r) or (0 >= self.snake.center_x - self.snake.r) or (config.height <= self.snake.center_y + self.snake.r) or (0 >= self.snake.center_y - self.snake.r):
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.snake = Snake(config.width, config.height)
            # self.exit = 1

        # collision with the body
        if self.snake.score > 1:
            for i in range (len(self.snake.body) - 1):
                if self.snake.center_x == self.snake.body[i][0] and self.snake.center_y == self.snake.body[i][1]:
                    arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
                    self.snake = Snake(config.width, config.height)
                    break

    def on_update(self, delta_time: float):
        # display events during game
        self.snake.move()

        # Apple, Pear and Bomb position
        if self.apple.center_x - 10 <= self.snake.center_x <= self.apple.center_x + 10 and self.apple.center_y - 10 <= self.snake.center_y <= self.apple.center_y + 10 :
            fruit = 'apple'
            self.snake.eat(fruit)
            self.apple = Apple(config.width, config.height)

        if self.pear.center_x - 10 <= self.snake.center_x <= self.pear.center_x + 10 and self.pear.center_y - 10 <= self.snake.center_y <= self.pear.center_y + 10 :
            fruit = 'pear'
            self.snake.eat(fruit)
            self.pear = Pear(config.width, config.height)

        if self.bomb.center_x - 10 <= self.snake.center_x <= self.bomb.center_x + 10 and self.bomb.center_y - 10 <= self.snake.center_y <= self.bomb.center_y + 10 :
            fruit = 'bomb'
            self.snake.eat(fruit)
            self.bomb = Bomb(config.width, config.height)

        # Apple and Pear direction
        apple_direction = self.snake.vision(self.apple)
        pear_direction = self.snake.vision(self.pear)
        apple_distance = math.hypot((self.snake.center_x - self.apple.center_x), (self.snake.center_y - self.apple.center_y))
        pear_distance = math.hypot((self.snake.center_x - self.pear.center_x), (self.snake.center_y - self.pear.center_y))

        if apple_distance < pear_distance:
            self.snake.decision(apple_direction)
        else:
            self.snake.decision(pear_direction)

        # Snake: Check collision with the wall
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
                    self.snake = Snake(config.width, config.height)

            self.snake.direction = direction


game = Game(config.width, config.height)
arcade.run()