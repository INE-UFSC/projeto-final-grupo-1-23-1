import constantes
import pygame
from mapa_1 import mapa1
from pygame.locals import *
from utils import get_path
from componentesMapa.SpriteVazio import SpriteVazio
from componentesMapa.spriteMapa import SpriteMapa

altura = ((constantes.ALTURA - 50) // 32)
largura = (constantes.LARGURA // 30)

class Bolinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Bolao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(constantes.AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
class Mapa:
    def __init__(self, mapa1):
        self.mapa = mapa1
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        self.sprites_vazios = pygame.sprite.Group()
        self.bolinhas = pygame.sprite.Group()
        self.boloes = pygame.sprite.Group()
        self.wallGroup = pygame.sprite.Group()
        self.portoes = pygame.sprite.Group()

    def desenhar_mapa(self):
        self.tela.fill((0, 0, 0))
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j] == 0:
                    sprite_vazio = SpriteVazio(j * largura, i * altura, largura, altura)
                    self.sprites_vazios.add(sprite_vazio)

                elif self.mapa[i][j] == 1:
                    bolinha = Bolinha(j * largura + (0.5 * largura), i * altura + (0.5 * altura))
                    self.wallGroup.add(bolinha)

                elif self.mapa[i][j] == 2:
                    bolao = Bolao(j * largura + (0.5 * largura), i * altura + (0.5 * altura))
                    self.wallGroup.add(bolao)

                else:
                    sprite_num = self.mapa[i][j]
                    path = get_path('imagensMapa', 'mapa1', f'sprite{sprite_num}.png')
                    vertical = SpriteMapa(j * largura, i * altura, largura, altura, path)
                    self.wallGroup.add(vertical)

        self.bolinhas.draw(self.tela)
        self.boloes.draw(self.tela)
        self.wallGroup.draw(self.tela)
        self.portoes.draw(self.tela)

    def carregar_mapa(self):
        self.desenhar_mapa()