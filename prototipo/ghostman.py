import pygame
from pygame.locals import *
import constantes
from mapa import Mapa
from utils import get_path
from mapa import Mapa

class Ghostman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(get_path('ghostman_imagem.png'))
        self.image = pygame.transform.scale(self.image, (22, 22))
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 18, 18)
        self.direction = None
        self.x = 378
        self.y = 478
        self.rect.center = (self.x, self.y)
        self.speed = 5
        #self.lista_de_paredes = Mapa.WallGroup

        
    def draw(self, screen):
        #ghost = pygame.draw.rect(screen, (5, 255, 0), self.rect)
        screen.blit(self.image, (self.x - 11, self.y - 11))


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
    '''def colisao_mapa(self, lista_de_paredes):
        #b = lista das paredes
        for parede in lista_de_paredes:
            if parede.colliderect(self.ghostman):
                if self.ghostman.right  >= parede.left and self.ghostman.right <= parede.left +5:
                    self.x = parede.left - 12
                    #melhorar depois
                if self.ghostman.left  <= parede.right and self.ghostman.left>= parede.right -5:
                    self.x = parede.right + 12
                if self.ghostman.top <= parede.bottom and self.ghostman.top >= parede.bottom -5:
                    self.y = parede.bottom + 10
                if self.ghostman.bottom >= parede.top and self.ghostman.bottom <= parede.top + 5:
                    self.y = parede.top - 12'''

    def colisao_bolinhas(self,bolinhas):
        for bolinha in bolinhas:
            if bolinha.colliderect(self.rect):
                bolinhas.remove(bolinha)

    def colidiu_com_pacman(self,pacman):
        print(pacman.vuneravel)

        if pacman.vuneravel == False:
            self.x= 473
            self.y = 428


    def coliliu_por_wall(self):
        if self.direction == "right":
            self.x -= 5
        if self.direction == "left":
            self.x += 5
        if self.direction == "down":
            self.y -= 5
        if self.direction == "up":
            self.y += 5
        self.direction = None
