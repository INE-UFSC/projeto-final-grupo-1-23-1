import pygame
from pygame.locals import *
import math
import constantes
import os

class Ghostman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = pygame.Rect(x, y, 15, 15)

    def move(self):
        if self.direction == "right":
            self.rect.x += 1
        elif self.direction == "left":
            self.rect.x -= 1
        elif self.direction == "up":
            self.rect.y -= 1
        elif self.direction == "down":
            self.rect.y += 1

    def checar_colisao(self, obj):
        distance = math.sqrt((self.rect.centerx - obj.rect.centerx) ** 2 + (self.rect.centery - obj.rect.centery) ** 2)
        if distance < self.radius + obj.radius:
            return True
        return False

    def carrega_sprite(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')        
        self.ghostman_sprite = os.path.join(diretorio_imagens, constantes.GHOSTMAN)
        # a linha abaixo transforma o arquivo de txto da variável em uma imagem do pygame
        self.ghostman_sprite = pygame.image.load(self.ghostman_sprite).convert()

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
