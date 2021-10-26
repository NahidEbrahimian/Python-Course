import random
import arcade

class Bomb():
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = arcade.Sprite('img/bomb1.png')
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()