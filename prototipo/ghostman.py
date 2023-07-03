import pygame
from pygame.locals import *
import constantes
from mapa import Mapa
from utils import get_path
from mapa import Mapa
from collision_manager import CollisionManager

class Ghostman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(get_path('imagens','ghostman_imagem.png'))
        self.image = pygame.transform.scale(self.image, (22, 22))
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 18, 18)
        self.direcao_x = None
        self.direcao_y = None
        self.rect.centerx = 420
        self.rect.centery = 425
        self.velocidade = 4
        self.direcao_da_ultima_colisao = None
        self.direcao_futura = None
        self.direcao_atual = None
        
    def draw(self, tela):

        tela.blit(self.image, (self.rect.centerx - 12, self.rect.centery - 12))

    def input_movimentacao(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direcao_x = 'right'
                    self.direcao_futura = self.direcao_x
                elif event.key == pygame.K_LEFT:
                    self.direcao_x = 'left'
                    self.direcao_futura = self.direcao_x
                if event.key == pygame.K_UP:
                    self.direcao_y = 'up'
                    self.direcao_futura = self.direcao_y
                elif event.key == pygame.K_DOWN:
                    self.direcao_y = 'down'
                    self.direcao_futura = self.direcao_y
        
    def handle_direcao_atual(self):
        if self.direcao_atual == None:
            self.last_direction = self.direcao_futura
            

    def movimentacao(self, direcao):
        if direcao == 'x' and self.direcao_futura != None:
            if self.direcao_x == 'right':
                self.rect.centerx += self.velocidade
            elif self.direcao_x == 'left':
                self.rect.centerx -= self.velocidade
        if direcao == 'y' and self.direcao_futura != None:
            if self.direcao_y == 'up':
                self.rect.centery -= self.velocidade
            elif self.direcao_y == 'down':
                self.rect.centery += self.velocidade
        self.direcao_da_ultima_colisao = direcao

    def colisao_tela(self):
        if self.rect.centerx > constantes.LARGURA:
            self.rect.centerx = 0
        elif self.rect.centerx < 0:
            self.rect.centerx = constantes.LARGURA



    def colisao_bolinhas(self,bolinhas):
        for bolinha in bolinhas:
            if bolinha.colliderect(self.rect):
                bolinhas.remove(bolinha)

    def colidiu_com_pacman(self,pacman):

        if pacman.vuneravel == False:
            self.rect.centerx= 473
            self.rect.centery = 428

    def colidiu_com_wall(self):
        if self.direcao_da_ultima_colisao == 'x':
            if self.direcao_x == "right":
                self.direcao_x = self.direcao_futura
                self.rect.centerx -= self.velocidade
            elif self.direcao_x == "left":
                self.direcao_x = self.direcao_futura
                self.rect.centerx += self.velocidade
        if self.direcao_da_ultima_colisao == 'y':
            if self.direcao_y == "down":
                self.direcao_y = self.direcao_futura
                self.rect.centery -= self.velocidade
            elif self.direcao_y == "up":
                self.direcao_y = self.direcao_futura
                self.rect.centery += self.velocidade




