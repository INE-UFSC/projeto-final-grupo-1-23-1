import pygame
from pygame.locals import *
import constantes
from mapa import Mapa

class Ghostman():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.direction = None
        self.x = 450
        self.y = 405
        self.rect.center = (self.x, self.y)
        self.speed = 20
        
    def draw(self, screen):
        pygame.draw.rect(screen, (5, 255, 0), self.rect)

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

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    #ele ta quicando na tela por causa do -1 ali
    def colisao_tela(self):
        if self.rect.right >= constantes.LARGURA or self.rect.left <= 0:
            self.speed *= -1
        if self.rect.bottom >= 850 or self.rect.top <= 0:
            self.speed *= -1

    #nao ta funcionando, a lógica funciona com base na verificação 
    #(ve esse video https://www.youtube.com/watch?v=1_H7InPMjaY, pode ver a partir do 13:10 se quiser) 
    #bom tem q fazer de alguma forma a verificação das paradas criadas pelo mapa com o personagem, a lógica é tipo essa
    #o problema só esta que não consigo usar a matriz pra verificar
    def colisao_mapa(self):
        tolerancia = 5
        if self.rect.colliderect(Mapa.mapa_atual[33][30]):
            if (Mapa.mapa_atual[33][30] >= 3) and self.rect < tolerancia:
                self.speed = 0