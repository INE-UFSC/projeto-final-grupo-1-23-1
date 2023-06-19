import constantes
import pygame
from mapa_1 import mapa1
from pygame.locals import *
from utils import get_path
from componentesMapa.SpriteVazio import SpriteVazio
from componentesMapa.spriteMapa import SpriteMapa
from bolinha import Bolinha
from bolao import Bolao

altura = ((constantes.ALTURA - 50) // 32)
largura = (constantes.LARGURA // 30)

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

        self.wallGroup.draw(self.tela)
        self.portoes.draw(self.tela)

    def carregar_mapa(self):
        self.tela.fill((0, 0, 0))
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j] == 0:
                    sprite_vazio = SpriteVazio(j * largura, i * altura, largura, altura)
                    self.sprites_vazios.add(sprite_vazio)

                elif self.mapa[i][j] == 1:
                    bolinha = Bolinha(j * largura + (0.5 * largura), i * altura + (0.5 * altura))
                    self.bolinhas.add(bolinha)


                elif self.mapa[i][j] == 2:
                    bolao = Bolao(j * largura + (0.5 * largura), i * altura + (0.5 * altura))
                    self.boloes.add(bolao)

                else:
                    sprite_num = self.mapa[i][j]
                    path = get_path('imagensMapa', 'mapa1', f'sprite{sprite_num}.png')
                    vertical = SpriteMapa(j * largura, i * altura, largura, altura, path)
                    self.wallGroup.add(vertical)
        self.desenhar_mapa()

    def acabaram_as_bolinhas(self):
        if len(self.bolinhas) == 0:
            return True
        else:
            False