import pygame
from componentesMapa.mapComponent import MapComponent
from utils import get_path

class SpriteMapa(MapComponent):
    def __init__(self, x, y, largura, altura, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura, altura))
        super().__init__(self.image, x, y)