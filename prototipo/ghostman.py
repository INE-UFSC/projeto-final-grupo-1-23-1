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
        self.direction_x = None
        self.direction_y = None
        self.rect.centerx = 420
        self.rect.centery = 425
        self.speed = 4
        self.last_collision_direction = None
        self.future_direction = None
        self.current_direction = None
        
    def draw(self, screen):
        #ghost = pygame.draw.rect(screen, (5, 255, 0), self.rect)
        screen.blit(self.image, (self.rect.centerx - 12, self.rect.centery - 12))

    def input_movimentacao(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction_x = 'right'
                    self.future_direction = self.direction_x
                elif event.key == pygame.K_LEFT:
                    self.direction_x = 'left'
                    self.future_direction = self.direction_x
                if event.key == pygame.K_UP:
                    self.direction_y = 'up'
                    self.future_direction = self.direction_y
                elif event.key == pygame.K_DOWN:
                    self.direction_y = 'down'
                    self.future_direction = self.direction_y
        
    def handle_current_direction(self):
        if self.current_direction == None:
            self.last_direction = self.future_direction
            

    def ghostman_movimentacao(self, direction):
        if direction == 'x' and self.future_direction != None:
            if self.direction_x == 'right':
                self.rect.centerx += self.speed
            elif self.direction_x == 'left':
                self.rect.centerx -= self.speed
        if direction == 'y' and self.future_direction != None:
            if self.direction_y == 'up':
                self.rect.centery -= self.speed
            elif self.direction_y == 'down':
                self.rect.centery += self.speed
        self.last_collision_direction = direction

    def colisao_tela(self):
        if self.rect.centerx > constantes.LARGURA:
            self.rect.centerx = 0
        elif self.rect.centerx < 0:
            self.rect.centerx = constantes.LARGURA

    #nao ta funcionando, a lógica funciona com base na verificação 
    #(ve esse video https://www.youtube.com/watch?v=1_H7InPMjaY, pode ver a partir do 13:10 se quiser) 
    #bom tem q fazer de alguma forma a verificação das paradas criadas pelo mapa com o personagem, a lógica é tipo essa
    #o problema só esta que não consigo usar a matriz pra verificar
    '''def colisao_mapa(self, lista_de_paredes):
        #b = lista das paredes
        for parede in lista_de_paredes:
            if parede.colliderect(self.ghostman):
                if self.ghostman.right  >= parede.left and self.ghostman.right <= parede.left +5:
                    self.rect.centerx = parede.left - 12
                    #melhorar depois
                if self.ghostman.left  <= parede.right and self.ghostman.left>= parede.right -5:
                    self.rect.centerx = parede.right + 12
                if self.ghostman.top <= parede.bottom and self.ghostman.top >= parede.bottom -5:
                    self.rect.centery = parede.bottom + 10
                if self.ghostman.bottom >= parede.top and self.ghostman.bottom <= parede.top + 5:
                    self.rect.centery = parede.top - 12'''

    def colisao_bolinhas(self,bolinhas):
        for bolinha in bolinhas:
            if bolinha.colliderect(self.rect):
                bolinhas.remove(bolinha)

    def colidiu_com_pacman(self,pacman):

        if pacman.vuneravel == False:
            self.rect.centerx= 473
            self.rect.centery = 428

    def colidiu_com_wall(self):
        if self.last_collision_direction == 'x':
            if self.direction_x == "right":
                self.direction_x = self.future_direction
                self.rect.centerx -= self.speed
            elif self.direction_x == "left":
                self.direction_x = self.future_direction
                self.rect.centerx += self.speed
        if self.last_collision_direction == 'y':
            if self.direction_y == "down":
                self.direction_y = self.future_direction
                self.rect.centery -= self.speed
            elif self.direction_y == "up":
                self.direction_y = self.future_direction
                self.rect.centery += self.speed

    '''def colidiu_com_wall(self):
        print("colidiu")
        if self.last_colission_direction == 'x':
            if self.direction_x == "right":
                self.rect.centerx -= self.speed
            elif self.direction_x == "left":
                self.rect.centerx += self.speed
        if self.last_colission_direction == 'y':
            if self.direction_y == "down":
                self.rect.centery -= self.speed
            elif self.direction_y == "up":
                self.rect.centery += self.speed'''

        #self.direction = None


