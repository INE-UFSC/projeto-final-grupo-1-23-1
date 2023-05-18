import pygame
from pygame.locals import *
import math

class Ghostman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 15, 15)
        self.radius = 15
        self.direction = "right"
        self.speed = 1

    def move(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

    def checar_colisao(self, obj):
        distance = math.sqrt((self.rect.centerx - obj.rect.centerx) ** 2 + (self.rect.centery - obj.rect.centery) ** 2)
        if distance < self.radius + obj.radius:
            return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, (5, 255, 0), (self.x, self.y), self.radius)

    def move_right(self):
        self.direction = "right"
        self.rect.x += 1

    def move_left(self):
        self.direction = "left"
        self.rect.x -= 1

    def move_up(self):
        self.direction = "up"
        self.rect.y -= 1

    def move_down(self):
        self.direction = "down"
        self.rect.y += 1

