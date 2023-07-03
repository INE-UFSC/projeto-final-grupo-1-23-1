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
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()
        self.direction_x = None
        self.direction_y = None
        self.rect.centerx = 420
        self.rect.centery = 420
        self.speed = 4
        self.last_collision_direction = None
        self.future_direction = None
        self.current_direction = None
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.centerx - 12, self.rect.centery - 12))

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
            self.rect.centerx = 420
            self.rect.centery = 420

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

    def handle_current_direction(self):
        if self.current_direction == None:
            self.last_direction = self.future_direction

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


