import pygame
from componentesMapa.mapComponent import MapComponent
import constantes
import random

class Caixa_Supresa(MapComponent):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = constantes.ROSA
        self.image = pygame.Surface((18, 18))
        self.image.fill(constantes.ROSA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ativo = False

        self.type = random.choice(['slow','speed'])
        self.timer_limit = 4000
        self.set_timer = 0
        self.player = None
        self.current_timer = None

    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        caixa = pygame.draw.rect(tela, self.cor, self.rect)
        return caixa
    def update(self,current_timer):
        self.current_timer = current_timer
        if self.ativo == True:
            self.cor = constantes.PRETO
            if self.current_timer - self.set_timer < self.timer_limit:
                self.set_timer +=1
            else:
                print("acabou o efeito")
                self.player.speed = 5#velocidade padrao
                self.kill()
    def hit(self,player):
        self.player = player
        if self.ativo == False:
            self.ativo = True
            self.set_timer = pygame.time.get_ticks()
            self.aplicar_efeito(player)

    def aplicar_efeito(self,player):
        print("aplicando o efeito de :",self.type)
        if self.ativo == True:
            if self.type == "speed":
                player.speed += 3
            elif self.type == "slow":
                player.speed -= 3
