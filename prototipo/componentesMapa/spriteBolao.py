import pygame
from componentesMapa.mapComponent import MapComponent
import constantes
from utils import get_path
class SpriteBolao(MapComponent):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estavel = True
        self.cor = constantes.AMARELO
        self.ativo = False
        self.timer_limit = 10000
        self.set_timer = 0
        self.current_timer = None
        self.pacmans = None
    def desenhar(self,tela):
        #bolinha = pygame.draw.circle(tela,self.cor,(self.pos_x,self.pos_y),self.raio)
        bolao = pygame.draw.rect(tela, self.cor, self.rect)
        return bolao
    def update(self,current_timer):
        self.current_timer = current_timer
        if self.ativo == True:
            self.cor = constantes.PRETO
            if self.current_timer - self.set_timer < self.timer_limit:
                self.set_timer +=1
            else:
                print("acabou o efeito")
                for pacman in self.pacmans:
                    pacman.vuneravel = True
                    pacman.image_atual = pacman.image_standard
                self.kill()

    def hit(self,pacmans):
        self.pacmans = pacmans
        if self.ativo == False:
            print("invunerabilidade ativada em pacman")
            self.ativo = True
            self.set_timer = pygame.time.get_ticks()
            for pacman in self.pacmans:
                pacman.vuneravel = False
                pacman.image_atual = pygame.image.load(get_path('pacman_vermelho.png'))
                pacman.image_atual = pygame.transform.scale(pacman.image_atual, (22, 22))

