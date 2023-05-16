from constantes import LARGURA, ALTURA, TITULO_JOGO
import pygame

class Janela:
    def __init__(self):
        self.janela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
