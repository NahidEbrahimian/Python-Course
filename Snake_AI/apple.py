import random
import arcade

class Apple():
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.r = 8
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
        self.img = arcade.Sprite('img/apple1.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()