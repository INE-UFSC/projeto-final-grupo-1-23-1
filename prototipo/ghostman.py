import pygame
from pygame.locals import *
from mapa import Mapa

class Ghostman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((5, 255, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.direction = None
        self.speed = 1
        self.radius = 20
        self.stopped = False

    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
        self.rect.center = (self.x, self.y)
        

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
