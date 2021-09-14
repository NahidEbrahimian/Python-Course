import math
import random
import time
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.speed = 1
        self.center_x = random.randint(50, w-50)
        self.center_y = h
        self.angle = 180
        self.height = 50
        self.width = 50

    def move(self):
        self.center_y -= self.speed

    def Speed(self, change_speed):
        self.speed += change_speed


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 5
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.bullet_sound = arcade.load_sound(":resources:sounds/hit1.wav")

    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


class Life(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.img = arcade.load_texture("heart.png")
        self.play_turn = 3
        self.x = 5
        self.y = 5
        self.h = 13
        self.w = 13
        self.x_change = 15

    def draw(self):
        self.x = 5
        for i in range(self.play_turn):
            arcade.draw_lrwh_rectangle_textured(self.x, self.y, self.w, self.h, self.img)
            self.x += self.x_change


class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 50
        self.height = 50
        self.center_x = w // 2
        self.center_y = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = arcade.SpriteList()
        self.speed = 5
        self.score = 0
        self.bullet_sound = arcade.load_sound(":resources:sounds/hit1.wav")

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(self.bullet_sound)


class Game(arcade.Window):
    def __init__(self):
        self.w = 600
        self.h = 400
        super().__init__(self.w, self.h, "Silver SpaceCraft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list = arcade.SpriteList()
        self.start_add_enemy_time = time.time()
        self.life = Life()
        self.enemy = Enemy(self.w, self.h)
        self.num_enemy = 0
        self.change_speed = 0
        self.exit = 0
        self.flag = 0
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 600, 400, self.background_image)

        # draw me
        self.me.draw()

        # draw life
        self.life.draw()

        # draw bullet_list
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        # draw enemy_list
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()

        # draw score
        output = f"Score: {self.me.score}"
        arcade.draw_text(output, 500, 10, arcade.color.DARK_BLUE_GRAY, 14)

        # draw game over
        if self.flag == 1:
            # arcade.start_render()
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.start_render()
            arcade.draw_lrwh_rectangle_textured(0, 0, 600, 400, self.background_image)
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.exit = 1

    def on_update(self, delta_time):
        # update enemy_list
        self.end_add_enemy_time = time.time()
        t = random.randint(2, 5)
        if self.end_add_enemy_time - self.start_add_enemy_time >= t:
            self.num_enemy += 1
            self.enemy_list.append(Enemy(self.w, self.h))
            self.enemy_list[-1].Speed(self.change_speed)
            if self.num_enemy % 4 == 0:
                self.change_speed += 0.5
            self.start_add_enemy_time = time.time()

        # update me
        self.me.rotate()

        # update and move bullet
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()

        # update life
        for i in range(len(self.enemy_list)):
            if self.enemy_list[i].center_y <= 0:
                if self.life.play_turn >= 1:
                    self.life.play_turn -= 1
                    self.enemy_list[i].remove_from_sprite_lists()

                    if self.life.play_turn == 0:
                        self.flag = 1
                    break

        # update and move enemy_list
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

        # collision bullet and enemy
        for i in range(len(self.me.bullet_list)):
            for j in range(len(self.enemy_list)):
                if (self.enemy_list[j].center_x - 25 <= self.me.bullet_list[i].center_x <= self.enemy_list[j].center_x +25) and (self.enemy_list[j].center_y - 25 <= self.me.bullet_list[i].center_y <= self.enemy_list[j].center_y + 25):
                    self.enemy_list[j].remove_from_sprite_lists()
                    # self.me.bullet_list[k].remove_from_sprite_lists()
                    self.me.score += 1
                    arcade.play_sound(self.explosion_sound)
                    break

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.me.change_angle = -1

        elif key == arcade.key.A:
            self.me.change_angle = 1

        elif key == arcade.key.SPACE:
            self.me.fire()

        if self.exit == 1:
            arcade.exit()

    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0


game = Game()
arcade.run()
