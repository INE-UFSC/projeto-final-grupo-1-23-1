import pygame
from pygame.locals import *
from random import randint
from utils import get_path
import constantes

class Pacman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_padrao = pygame.image.load(get_path('imagens', 'pacman_imagem.png'))
        self.imagem_padrao = pygame.transform.scale(self.imagem_padrao, (24, 24))
        self.image_atual = self.imagem_padrao
        self.rect = self.image_atual.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.center = (self.x, self.y)
        self.direction = None
        self.vidas = 3
        self.velocidade = 5
        self.posicao_inicial = (pos_x, pos_y)
        self.pode_comer_ghostman = False
        self.vuneravel = True
        self.ativar_invunerabilidade = False
        self.invunerabilibidade_timer = 3000
        self.set_timer = 0
        self.current_timer = None
    def update(self, tempo_atual):
        self.current_timer = tempo_atual
        if self.ativar_invunerabilidade:
            self.vuneravel = False
        if not self.vuneravel:
            if self.current_timer - self.set_timer > self.invunerabilibidade_timer:
                self.vuneravel = True
                self.ativar_invunerabilidade = False
    def draw(self, screen):
        if not self.pode_comer_ghostman:

            screen.blit(self.image_atual, (self.x - 12, self.y - 12))


    def mover_direita(self):
        self.direction = "right"

    def mover_esquerda(self):
        self.direction = "left"

    def mover_cima(self):
        self.direction = "up"

    def mover_baixo(self):
        self.direction = "down"

    def mover(self):
        if self.direction == "up":
            self.y -= self.velocidade
        elif self.direction == "down":
            self.y += self.velocidade
        elif self.direction == "left":
            self.x -= self.velocidade
        elif self.direction == "right":
            self.x += self.velocidade
        self.rect.center = (self.x, self.y)

    def colisao_tela(self):
        if self.x > constantes.LARGURA:
            self.x = 0
        elif self.x < 0:
            self.x = constantes.LARGURA

    def movimentacao_randomica(self):
        direcoes_possiveis = ['up', 'down', 'left', 'right']
        direcao_sorteada = direcoes_possiveis[randint(0, 3)]
        if direcao_sorteada == 'right' and self.direction != 'left':
            self.mover_direita()
        elif direcao_sorteada == 'left' and self.direction != 'right':
            self.mover_esquerda()
        elif direcao_sorteada == 'up' and self.direction != 'down':
            self.mover_cima()
        elif direcao_sorteada == 'down' and self.direction != 'up':
            self.mover_baixo()
        self.mover()
    def colidido_por_ghostman(self):
        if self.vuneravel == True:
            self.vidas -= 1
            self.x, self.y = self.posicao_inicial
            self.set_timer = pygame.time.get_ticks()
            self.ativar_invunerabilidade = True
            print('colidi com o fastasma!!!')

    def colidiu_com_bolinha(self):
        pass

    def colidiu_com_bolao(self):
        pass

    def colidiu_com_wall(self):
        if self.direction == "right":
            self.x -= self.velocidade
        if self.direction == "left":
            self.x += self.velocidade
        if self.direction == "down":
            self.y -= self.velocidade
        if self.direction == "up":
            self.y += self.velocidade
        self.direction = None