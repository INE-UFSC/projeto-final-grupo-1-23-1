import pygame
from pygame.locals import *
import constantes
from ghostman import Ghostman
import random
from mapa import Mapa

class PacmanRight():
    def __init__(self):
        self.pac = pygame.Rect(50, 465, 18, 18)
        self.direction = None
        self.speed = 5
        self.vidas = 3
        self.x = 10
        self.y = 465
        self.pac.center = (self.x, self.y)
        self.lista_pacman = []
    
    def draw(self, screen):
        pac1 = pygame.draw.rect(screen, (255, 255, 0), self.pac)
        pac2 = pygame.draw.rect(screen, (255, 255, 0), self.pac)
        self.lista_pacman.append(pac1, pac2)

    def colisao_ghostman(self, ghost):
        for pac in self.lista_pacman:
            if pac.colliderect(ghost.rect):
                self.speed = 0
                self.vidas -= 1
                self.x = 10
                self.y = 465
                self.movimento_pacman()

    def esta_no_mapa(self, b):
        for c in b:
            if c.colliderect(self.pac):
                if self.pac.right  >= c.left and self.pac.right <= c.left +5:
                    self.x = c.left - 12
                if self.pac.left  <= c.right and self.pac.left>= c.right -5:
                    self.x = c.right + 12
                if self.pac.top <= c.bottom and self.pac.top >= c.bottom -5:
                    self.y = c.bottom + 10
                if self.pac.bottom >= c.top and self.pac.bottom <= c.top + 5:
                    self.y = c.top - 12

    def movimento_pacman(self):
        directions = ["up", "down", "left", "right"]
        new_direction = random.choice(directions)

        if new_direction == "up":
            new_x = self.x
            new_y = self.y - self.speed
        elif new_direction == "down":
            new_x = self.x
            new_y = self.y + self.speed
        elif new_direction == "left":
            new_x = self.x - self.speed
            new_y = self.y
        elif new_direction == "right":
            new_x = self.x + self.speed
            new_y = self.y

        new_pac = pygame.Rect(new_x, new_y, 18, 18)
        
        if self.esta_no_mapa(new_pac):
            self.x = new_x
            self.y = new_y

        self.pac.center = (self.x, self.y)
