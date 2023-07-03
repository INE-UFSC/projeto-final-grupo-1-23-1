import pygame
from pygame.locals import *
import random
from utils import get_path
import constantes

class Pacman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image_standard = pygame.image.load(get_path('imagens', 'pacman_imagem.png'))
        self.image_standard = pygame.transform.scale(self.image_standard, (22, 22)) #tamanho do personagem,
        self.image_atual = self.image_standard
        self.rect = self.image_atual.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.center = (self.x, self.y)
        self.direction = None
        self.direcao_colidida = None
        self.vidas = 2
        self.velocidade = 4
        self.posicao_inicial = (pos_x, pos_y)
        self.pode_comer_ghostman = False
        self.vuneravel = True
        self.ativar_invunerabilidade = False
        self.invunerabilibidade_timer = 3000
        self.set_timer = 0
        self.current_timer = None
        self.speed = 6

    def update(self,current_timer):
        self.current_timer = current_timer
        if self.ativar_invunerabilidade:
            self.vuneravel = False
        if not self.vuneravel:
            if self.current_timer - self.set_timer > self.invunerabilibidade_timer:
                self.vuneravel = True
                self.ativar_invunerabilidade = False

    def draw(self, screen):
        if not self.pode_comer_ghostman:
            screen.blit(self.image_atual, (self.x - 11, self.y - 11))
        else:
            pass

            
    def colidido_por_ghostman(self):
        if self.vuneravel == True:
            self.vidas -= 1
            self.x, self.y = self.posicao_inicial
            self.set_timer = pygame.time.get_ticks()
            self.ativar_invunerabilidade = True

    def colidiu_com_bolinha(self):
        pass

    def colidiu_com_bolao(self):
        pass
    
    def colisao_tela(self):
        if self.x > constantes.LARGURA:
            self.x = 0
        elif self.x < 0:
            self.x = constantes.LARGURA

    def escolha_de_direcao(self, direcoes = ['up', 'down', 'left', 'right']):
        return random.choice(direcoes)
    
    def movimentacao_inicial(self):
        self.direction = self.escolha_de_direcao()

    def movimentacao_continua(self):
        self.move()

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

    def colidiu_por_wall(self, walls = []):
        self.direcao_colidida = self.direction
        if self.direction == "right":
            self.x -= self.speed
            self.direction = self.escolha_de_direcao(['up', 'down'])
        elif self.direction == "left":
            self.x += self.speed
            self.direction = self.escolha_de_direcao(['up', 'down'])
        elif self.direction == "down":
            self.y -= self.speed
            self.direction = self.escolha_de_direcao(['left', 'right'])
        elif self.direction == "up":
            self.y += self.speed
            self.direction = self.escolha_de_direcao(['left', 'right'])