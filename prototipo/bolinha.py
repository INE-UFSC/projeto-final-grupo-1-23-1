import pygame
class Bolinha:
    def __init__(self,cor,pos_x: int, pos_y: int,raio):
        self.raio = raio
        self.pos_x= pos_x
        self.pos_y = pos_y
        self.cor =cor

    def desenhar(self,tela):
        bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        return bolinha

