import pygame
from componentesMapa.mapComponent import MapComponent

class SpriteVazio(MapComponent):
    def __init__(self, x, y, largura, altura):
        self.image = pygame.Surface((largura, altura))
        self.image.fill((0, 0, 0))
        super().__init__(self.image, x, y)
