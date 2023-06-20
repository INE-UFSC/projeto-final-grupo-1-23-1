import pygame
from componentesMapa.mapComponent import MapComponent
import constantes

class SpriteBolinha(MapComponent):
    def __init__(self, x, y):
        self.image = pygame.Surface((4, 4))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        super().__init__(self.image, x, y)
        self.estavel = True


    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        bolinha = pygame.draw.rect(tela, constantes.AMARELO, self.rect)
        return bolinha

    def colidida_por_pacman(self):
        self.estavel = False