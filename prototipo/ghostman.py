import pygame
from pygame.locals import *
import constantes
from mapa import Mapa
from utils import get_path

class Ghostman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(get_path('ghostman_imagem.png'))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 18, 18)
        self.direction = None
        self.x = 378
        self.y = 478
        self.rect.center = (self.x, self.y)
        self.speed = 5
        
    def draw(self, screen):
        ghost = pygame.draw.rect(screen, (5, 255, 0), self.rect)
        screen.blit(self.image, (self.x - 10, self.y - 10))


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

    def ghostman_movimentacao(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_right()
                elif event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_DOWN:
                    self.move_down()
        self.move()

    def colisao_tela(self):
        if self.x > constantes.LARGURA:
            self.x = 0
        elif self.x < 0:
            self.x = constantes.LARGURA

    #nao ta funcionando, a lógica funciona com base na verificação 
    #(ve esse video https://www.youtube.com/watch?v=1_H7InPMjaY, pode ver a partir do 13:10 se quiser) 
    #bom tem q fazer de alguma forma a verificação das paradas criadas pelo mapa com o personagem, a lógica é tipo essa
    #o problema só esta que não consigo usar a matriz pra verificar
    def colisao_mapa(self, lista_de_paredes):
        #b = lista das paredes
        for c in lista_de_paredes:
            if c.colliderect(self.rect):
                if self.rect.right  >= c.left and self.rect.right <= c.left +5:
                    self.x = c.left - 12
                    #melhorar depois
                if self.rect.left  <= c.right and self.rect.left>= c.right -5:
                    self.x = c.right + 12
                if self.rect.top <= c.bottom and self.rect.top >= c.bottom -5:
                    self.y = c.bottom + 10
                if self.rect.bottom >= c.top and self.rect.bottom <= c.top + 5:
                    self.y = c.top - 12

    def colisao_bolinhas(self,bolinhas):
        for bolinha in bolinhas:
            if bolinha.colliderect(self.rect):
                bolinhas.remove(bolinha)

    def hit(self):
        print('colidiu')

