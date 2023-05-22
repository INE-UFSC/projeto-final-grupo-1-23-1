import pygame
from pygame.locals import *
import constantes

class Pacman():
    def __init__(self):
        self.direction = None
        self.speed = 5
        self.lista_pacman = []
    
    def draw(self, screen):
        pac1 = pygame.draw.rect(screen, (255, 255, 0), (10, 465, 18, 18))
        pac2 = pygame.draw.rect(screen, (255, 255, 0), (50, 465, 18, 18))
        pac3 = pygame.draw.rect(screen, (255, 255, 0), ((constantes.LARGURA - 30), 465, 18, 18))
        pac4 = pygame.draw.rect(screen, (255, 255, 0), ((constantes.LARGURA - 70), 465, 18, 18))
        self.lista_pacman.append(pac1, pac2, pac3, pac4)

    def colisao_ghostman(self):
        for i in range (len(self.lista_pacman)):
            if i.colliderect(self.rect):
