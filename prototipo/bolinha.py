import pygame
class Bolinha(pygame.sprite.Sprite):
    def __init__(self,cor,pos_x: int, pos_y: int,lado):
        pygame.sprite.Sprite.__init__(self)
        self.lado = lado
        #self.raio = raio
        self.pos_x= pos_x
        self.pos_y = pos_y
        self.cor = cor
        self.rect = ((pos_x, pos_y), (self.lado, self.lado))
        self.estavel = True
    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        bolinha = pygame.draw.rect(tela, self.cor, self.rect)
        return bolinha

    def colidida_por_pacman(self):
        self.estavel = False

