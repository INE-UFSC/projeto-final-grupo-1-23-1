import pygame
from pygame.locals import *
from mapa import Mapa

class Ghostman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((5, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = 0
        self.y = 0
        self.direction = None
        self.speed = 1
        self.radius = 15
        self.stopped = False

    def move(self):
        if self.stopped:
            return
        if self.direction == "up":
            if Mapa.mapa_atual[self.y - 1][self.x] != 3:
                self.y -= self.speed
            else:
                self.stopped = True
        elif self.direction == "down":
            if Mapa.mapa_atual[self.y + 1][self.x] != 3:
                self.y += self.speed
            else:
                self.stopped = True
        elif self.direction == "left":
            if Mapa.mapa_atual[self.y][self.x - 1] != 3:
                self.x -= self.speed
            else:
                self.stopped = True
        elif self.direction == "right":
            if Mapa.mapa_atual[self.y][self.x + 1] != 3:
                self.x += self.speed
            else:
                self.stopped = True

    def check_collision(self):
        if Mapa.mapa_atual[self.y][self.x] == 3:
            self.stopped = True

    def draw(self, screen):
        pygame.draw.circle(screen, (5, 255, 0), self.rect.center, self.radius)

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

