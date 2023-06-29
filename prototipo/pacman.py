import pygame
from pygame.locals import *
from random import randint
from utils import get_path
import constantes

class Pacman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image_standard = pygame.image.load(get_path('imagens', 'pacman_imagem.png'))
        self.image_standard = pygame.transform.scale(self.image_standard, (24, 24)) #tamanho do personagem,
        self.image_atual = self.image_standard
        self.rect = self.image_atual.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.center = (self.x, self.y)
        self.direction = None
        self.vidas = 3
        self.speed = 5
        self.posicao_inicial = (pos_x, pos_y)
        self.pode_comer_ghostman = False

        self.vuneravel = True


    def draw(self, screen):
        if not self.pode_comer_ghostman:
            #ghost = pygame.draw.rect(screen, (255, 0, 0), self.rect)
            screen.blit(self.image_atual, (self.x - 12, self.y - 12))
        else:
            #ghost = ghost = pygame.draw.rect(screen, (0, 250, 0), self.rect)
            pass

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

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

    def colisao_tela(self):
        if self.x > constantes.LARGURA:
            self.x = 0
        elif self.x < 0:
            self.x = constantes.LARGURA

    def movimentacao(self):
        direcoes_possiveis = ['up', 'down', 'left', 'right']
        direcao_sorteada = direcoes_possiveis[randint(0, 3)]
        if direcao_sorteada == 'right' and self.direction != 'left':
            self.move_right()
        elif direcao_sorteada == 'left' and self.direction != 'right':
            self.move_left()
        elif direcao_sorteada == 'up' and self.direction != 'down':
            self.move_up()
        elif direcao_sorteada == 'down' and self.direction != 'up':
            self.move_down()
        self.move()
    def colidido_por_ghostman(self):
        if self.vuneravel == True:
            self.vidas -= 1
            self.x, self.y = self.posicao_inicial
            print('colidi com o fastasma!!!')

    def colidiu_com_bolinha(self):
        pass

    def colidiu_com_bolao(self):
        pass

    def colidiu_por_wall(self):
        if self.direction == "right":
            self.x -= self.speed
        if self.direction == "left":
            self.x += self.speed
        if self.direction == "down":
            self.y -= self.speed
        if self.direction == "up":
            self.y += self.speed
        self.direction = None