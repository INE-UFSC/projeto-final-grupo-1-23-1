import pygame
import constantes
class Bolinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estavel = True

    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        bolinha = pygame.draw.rect(tela, constantes.AMARELO, self.rect)
        return bolinha

    def colidida_por_pacman(self):
        self.estavel = False

