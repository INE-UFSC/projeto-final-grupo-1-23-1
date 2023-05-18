import pygame
from pygame.locals import *
#from abc import ABC, abstractmethod
import math
import constantes
import os

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = pygame.Rect(x, y, 15, 15)

    def checar_colisao(self, obj):
        distance = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
        if distance < self.radius + obj.radius:
            return True
        return False
    
    def carrega_sprite(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')        
        self.pacman_sprite = os.path.join(diretorio_imagens, constantes.PACMAN)
        # a linha abaixo transforma o arquivo de txto da variável em uma imagem do pygame
        self.pacman_sprite = pygame.image.load(self.pacman_sprite).convert()
