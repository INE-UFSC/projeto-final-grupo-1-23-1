import pygame
import sys
import constantes
from gui import *
import os
from pygame.locals import *
from utils import get_path
from match import Match
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        #self.instancia_partida()
        self.cria_tela()
        self.gui = Gui(self.tela)
        self.jogo = Match(self.tela)
        self.rodando = True
        self.atual = self.gui

    def cria_tela(self):
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)


    """ def instancia_partida(self):
        self.partida.cria_tela()
        self.tela = self.partida.tela
        self.cria_tela()
        self.partida = Match(self.tela)
        self.gui = Gui(self.tela)
        self.relogio = self.partida.relogio
        self.programa_esta_aberto = self.partida.programa_esta_aberto """



    def interface_loop(self):
        """ while True:
            events = pygame.event.get()
            self.relogio.tick(constantes.FPS)
            self.handle_events(events)
            if self.partida.jogando == False:
                self.gui.game_loop(events)
            else:
                self.partida.nova_partida() """
        while self.rodando:
            events = pygame.event.get()
            self.atual.game_loop(events)
            self.handle_events(events)

    def handle_events(self, events):
        for event in events:
            if event.type == START_GAME:
                self.atual = self.jogo
                self.atual.game_loop()
                self.jogo.conferir_condicoes_de_fim()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    QUIT_MENU
            if event.type == EXIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.Sound(os.path.join(get_path('audios', constantes.TECLA_START))).play()
        return events




