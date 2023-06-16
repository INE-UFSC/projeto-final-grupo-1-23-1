import pygame
import constantes


class Bolao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estavel = True

    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        bolao = pygame.draw.rect(tela, constantes.AMARELO, self.rect)
        return bolao

    def colidido_por_pacman(self):
        self.estavel = False
        pass
