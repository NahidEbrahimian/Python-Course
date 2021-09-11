import random
import arcade


class Object(arcade.Sprite):
    def __init__(self, w, h):
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)


class Apple(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.color = arcade.color.RED
        self.r = 8
        self.img = arcade.Sprite('img/apple1.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Pear(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite('img/pear1.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Bomb(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite('img/bomb1.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color1 = arcade.color.ARMY_GREEN
        self.color2 = arcade.color.APPLE_GREEN
        self.speed = 2
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.flag = 0

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)

        for index, item in enumerate(self.body):
            if index % 2 == 0:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color2)
            else:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color1)

    def Eat(self, fruit):
        if fruit == 'apple':
            self.flag = 1

        if fruit == 'pear':
            self.score += 2

        if fruit == 'bomb':
            self.score -= 1

    def move(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

        self.body.append([self.center_x, self.center_y])
        if self.flag == 0:
            del(self.body[0])


class Game(arcade.Window):
    def __init__(self, width, height):
        arcade.Window.__init__(self, width, height, 'snake')
        arcade.set_background_color(arcade.color.DARK_GRAY)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.pear = Pear(width, height)
        self.bomb = Bomb(width, height)
        self.flag = 0
        self.exit = 0

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

        if self.flag == 1:
            if self.snake.score <= 0:
                arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
                self.exit = 1

        # collision with the wall
        if (600 <= self.snake.center_x + self.snake.r) or (0 >= self.snake.center_x - self.snake.r) or (400 <= self.snake.center_y + self.snake.r) or (0 >= self.snake.center_y - self.snake.r):
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.exit = 1

    def on_update(self, delta_time: float):
        # display events during game
        self.snake.move()
        self.snake.flag = 0

        if self.apple.center_x - 10 <= self.snake.center_x <= self.apple.center_x + 10 and self.apple.center_y - 10 <= self.snake.center_y <= self.apple.center_y + 10 :
            fruit = 'apple'
            self.snake.Eat(fruit)
            self.apple = Apple(600, 400)

        if self.pear.center_x - 10 <= self.snake.center_x <= self.pear.center_x + 10 and self.pear.center_y - 10 <= self.snake.center_y <= self.pear.center_y + 10 :
            fruit = 'pear'
            self.snake.Eat(fruit)
            self.pear = Pear(600, 400)

        if self.bomb.center_x - 10 <= self.snake.center_x <= self.bomb.center_x + 10 and self.bomb.center_y - 10 <= self.snake.center_y <= self.bomb.center_y + 10 :
            fruit = 'bomb'
            self.snake.Eat(fruit)
            self.bomb = Bomb(600, 400)

    def on_key_release(self, key, modifiers):

        # left
        if key == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0

        # up
        elif key == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1

        # right
        elif key == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0

        # down
        elif key == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1

        if self.exit == 1:
            arcade.exit()

width = 600
height = 400
game = Game(width, height)
arcade.run()