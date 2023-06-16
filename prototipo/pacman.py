import pygame
from pygame.locals import *
from random import randint
from utils import get_path

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(get_path('pacman_imagem.png'))
        self.image = pygame.transform.scale(self.image, (20, 20)) #tamanho do personagem,
        self.rect = self.image.get_rect()
        self.x = 110
        self.y = 150
        self.rect.center = (self.x, self.y)
        self.direction = None
        self.vidas = 3
        self.speed = 5


    def draw(self, screen):
            ghost = pygame.draw.rect(screen, (255, 0, 0), self.rect)
            screen.blit(self.image, (self.x - 10, self.y - 10))

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
        self.vidas -= 1
        self.x = 200
        self.y = 200
        print('colidi com o fastasma!!!')

    def colidiu_com_bolinha(self):
        pass

    def colidiu_com_bolao(self):
        pass