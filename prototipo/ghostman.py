import pygame
from pygame.locals import *
from personagem import Personagem

class Ghostman(Personagem):
    collided_pacman = []

    def __init__(self, x, y):
        super().__init__(x, y)

    def mover(self):
        if self.direction == "right":
            self.x += 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "up":
            self.y -= 1
        elif self.direction == "down":
            self.y += 1

    def checar_colisao(self, obj):
        return super().check_collision(obj)

    def desenha_sprite(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)
