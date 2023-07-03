import pygame
from componentesMapa.mapComponent import MapComponent
import constantes
import random
from utils import get_path
class Caixa_Supresa(MapComponent):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(get_path('Power ups.png'))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ativo = False

        self.type = random.choice(['slow','speed'])
        self.timer_limit = 4000
        self.set_timer = 0
        self.player = None
        self.current_timer = None

    def desenhar(self, screen):
        #ghost = pygame.draw.rect(screen, (5, 255, 0), self.rect)
        caixa = screen.blit(self.image, (self.rect.x-11, self.rect.y-11))
        return caixa
    def update(self,current_timer):
        self.current_timer = current_timer
        if self.ativo == True:
            self.image.fill(constantes.PRETO)
            if self.current_timer - self.set_timer > self.timer_limit:
                print("acabou o efeito")
                self.player.velocidade = 5#velocidade padrao
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
                player.velocidade += 3
            elif self.type == "slow":
                player.velocidade -= 3
