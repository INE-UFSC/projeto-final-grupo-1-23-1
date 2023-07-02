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
        self.instancia_partida()
        self.gui = Gui()




    def instancia_partida(self):
        self.partida = Match()
        self.partida.cria_tela()
        self.tela = self.partida.tela
        self.relogio = self.partida.relogio
        self.programa_esta_aberto = self.partida.programa_esta_aberto



    def interface_loop(self):
        while True:
            self.relogio.tick(constantes.FPS)
            events = self.handle_events()
            if self.partida.jogando == False:
                self.gui.game_loop(events)
            else:
                self.partida.nova_partida()


    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == START_GAME:
                self.partida.jogando = True
            if event.type == pygame.QUIT:
                self.programa_esta_aberto = False
                pygame.quit()
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.Sound(os.path.join(get_path('audios', constantes.TECLA_START))).play()
        return events




