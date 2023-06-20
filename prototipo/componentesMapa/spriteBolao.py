import pygame
from componentesMapa.mapComponent import MapComponent
import constantes

class SpriteBolao(MapComponent):
    def __init__(self, x, y):
        self.image = pygame.Surface((20, 20))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        super().__init__(self.image, x, y)