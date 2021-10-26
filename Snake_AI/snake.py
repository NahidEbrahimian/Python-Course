import arcade
import config
import random


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color1 = arcade.color.ARMY_GREEN
        self.color2 = arcade.color.APPLE_GREEN
        self.speed = 10
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.flag = 0
        self.direction = random.randint(0, 3)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)

        for index, item in enumerate(self.body):
            if index % 2 == 0:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color2)
            else:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color1)

    def eat(self):
        self.score += 1

    def move(self):
        if self.direction == 0:
            self.change_x = -1
            self.change_y = 0

        elif self.direction == 1:
            self.change_x = 1
            self.change_y = 0

        elif self.direction == 2:
            self.change_x = 0
            self.change_y = -1

        elif self.direction == 3:
            self.change_x = 0
            self.change_y = 1

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

        self.body.append([self.center_x, self.center_y])
        if len(self.body) > self.score:
            del (self.body[0])

    def vision(self, apple):

        # left
        if self.center_x > apple.center_x and self.center_y == apple.center_y:
            for part in self.body:
                if self.center_x > part[0] > apple.center_x and self.center_y == part[1]:
                    break
            else:
                return '0'

        # left up
        if self.center_x > apple.center_x and self.center_y > apple.center_y:
            for part in self.body:
                if abs(self.center_x - part[0]) == abs(self.center_y - part[1]) and self.center_x > part[0] > apple.center_x and self.center_y > part[1] > apple.center_y:
                    break
            else:
                return '02'

        # right
        if self.center_x < apple.center_x and self.center_y == apple.center_y:
            for part in self.body:
                if self.center_x < part[0] < apple.center_x and self.center_y == part[1]:
                    break
            else:
                return '1'

        # down right
        if self.center_x < apple.center_x and self.center_y < apple.center_y:
            for part in self.body:
                if abs(self.center_x - part[0]) == abs(self.center_y - part[1]) and self.center_x < part[0] < apple.center_x and self.center_y < part[1] < apple.center_y:
                    break
            else:
                return '31'

        # up
        if self.center_x == apple.center_x and self.center_y > apple.center_y:
            for part in self.body:
                if self.center_x == part[0] and self.center_y > part[1] > apple.center_y:
                    break
            else:
                return '2'

        # up right
        if self.center_x < apple.center_x and self.center_y > apple.center_y:
            for part in self.body:
                if abs(self.center_x - part[0]) == abs(self.center_y - part[1]) and self.center_x < part[0] < apple.center_x and self.center_y > part[1] > apple.center_y:
                    break
            else:
                return '21'

        # down
        if self.center_x == apple.center_x and self.center_y < apple.center_y:
            for part in self.body:
                if self.center_x == part[0] and self.center_y < part[1] < apple.center_y:
                    break
            else:
                return '3'

        # down left
        if self.center_x > apple.center_x and self.center_y < apple.center_y:
            for part in self.body:
                if abs(self.center_x - part[0]) == abs(self.center_y - part[1]) and self.center_x > part[0] > apple.center_x and self.center_y < part[1] < apple.center_y:
                    break
            else:
                return '30'

        return None

    def decision(self, direction):
        # left
        if direction == '0':
            if self.direction != 1:
                self.direction = 0

        # up left
        elif direction == '02':
            if self.direction != 1:
                self.direction = 0
            elif self.direction != 3:
                self.direction = 2

        # right
        elif direction == '1':
            # print("right")
            if self.direction != 0:
                self.direction = 1

        # down right
        elif direction == '31':
            if self.direction != 0:
                self.direction = 1
            elif self.direction != 2:
                self.direction = 3

        # up
        elif direction == '2':
            if self.direction != 3:
                self.direction = 2

        # up right
        elif direction == '21':
            if self.direction != 3:
                self.direction = 2
            elif self.direction != 0:
                self.direction = 1

        # down
        elif direction == '3':
            if self.direction != 2:
                self.direction = 3

        # down left
        elif direction == '30':
            if self.direction != 2:
                self.direction = 3
            elif self.direction != 1:
                self.direction = 0

    def collision_with_wall(self, direction):
        if direction == 2:
            if self.center_y - 10 > config.wall_offset:
                return False

        elif direction == 1:
            if self.center_x + 10 < config.width - config.wall_offset:
                return False

        elif direction == 3:
            if self.center_y + 10 < config.height - config.wall_offset:
                return False

        elif direction == 0:
            if self.center_x - 10 > config.wall_offset:
                return False

        return True
