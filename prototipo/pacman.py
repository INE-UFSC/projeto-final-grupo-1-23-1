import pygame
from pygame.locals import *
from personagem import Personagem

class Pacman(Personagem):
    def __init__(self, x, y):
        super().__init__(x, y)

    def desenha_sprite(self, screen):
        pygame.draw.circle(screen, (5, 255, 0), (self.x, self.y), self.radius)
