import pygame
from pygame.locals import *
import math

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 15, 15)
        self.radius = 20
        self.direction = "right"

    def checar_colisao(self, obj):
        distance = math.sqrt((self.rect.centerx - obj.rect.centerx) ** 2 + (self.rect.centery - obj.rect.centery) ** 2)
        if distance < self.radius + obj.radius:
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)

