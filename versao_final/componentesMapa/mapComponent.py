import pygame
from abc import ABC

class MapComponent(ABC, pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.rect = image.get_rect()
        self.rect.x=x
        self.rect.y=y