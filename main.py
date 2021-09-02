import pygame
import random


class Apple:
    def __init__(self):
        self.r = 5
        self.x = random.randint(10, width - 10) // 10*10
        self.y = random.randint(10, height - 10) // 10*10
        # self.w = 5
        # self.h = 5
        self.color = (255, 0, 0)

    def show(self):
        pygame.draw.circle(surface=display, color=self.color, center = [self.x, self.y], radius=self.r)
        # pygame.draw.rect(surface=display, color=self.color, rect=[self.x, self.y, self.w, self.h])


class Snake:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = width / 2
        self.y = height / 2
        # self.name = "Snake-AI"
        self.color = (60, 60, 60)
        self.speed = 2.5
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []

    def Eat(self):
        if (apple.x - apple.r <= self.x <= apple.x + apple.r) and (apple.y - apple.r - 5 <= self.y <= apple.x + apple.r):
            print("*")
            self.score += 1
            return True

        else:
            return  False

    def show(self):
        pygame.draw.rect(surface=display, color=self.color, rect=[self.x, self.y, self.w, self.h])
        # for item in self.body:
        #     pygame.draw.rect(surface=display, color=self.color, rect=[self.x, self.y, self.w, self.h])

    def move(self):
        if self.x_change == -1:
            self.x -= self.speed

        elif self.x_change == 1:
            self.x += self.speed

        elif self.y_change == -1:
            self.y -= self.speed

        elif self.y_change == 1:
            self.y += self.speed


if __name__ == "__main__":

    width = 600
    height = 400
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    snake.x_change = -1
                    snake.y_change = 0

                elif event.key == pygame.K_d:
                    snake.x_change = 1
                    snake.y_change = 0

                elif event.key == pygame.K_w:
                    snake.y_change = -1
                    snake.x_change = 0

                elif event.key == pygame.K_s:
                    snake.y_change = 1
                    snake.x_change = 0

        snake.move()
        result = snake.Eat()

        if result == True:
            apple = Apple()

        display.fill((220, 220, 220))
        snake.show()
        apple.show()
        pygame.display.update()
        clock.tick(30)