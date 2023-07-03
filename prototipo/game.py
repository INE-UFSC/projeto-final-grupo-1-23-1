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
        self.relogio = self.jogo.relogio
        self.programa_esta_aberto = self.jogo.programa_esta_aberto

    def cria_tela(self):
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)


    """ def instancia_partida(self):
        self.partida.cria_tela()
        self.tela = self.partida.tela
        self.cria_tela()
        self.partida = Match(self.tela)
        self.gui = Gui(self.tela) """



    def interface_loop(self):
         while True:
            events = pygame.event.get()
            self.relogio.tick(constantes.FPS)
            self.handle_events(events)
            if self.jogo.jogando == False:
                self.atual.game_loop(events)
                break

         self.jogo.nova_partida()
         self.fim_de_jogo(events)

    '''   while self.rodando:
        self.relogio.tick(constantes.FPS)
        self.events = pygame.event.get()
        if self.jogo.jogando == False:
            self.handle_events(self.events)
            self.atual.game_loop(self.events)'''

            #self.fim_de_jogo(self.events)

    def fim_de_jogo(self, events):
        fim = self.jogo.conferir_condicoes_de_fim()
        end = not fim
        events = events
        for event in events:
            if event.type == fim:
                pygame.event.post(VICTORY)
            if event.type == end:
                pygame.event.post(DEFEAT)
        self.handle_events(events)

    def handle_events(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == START_GAME:
                self.atual = self.jogo
                self.atual.game_loop()
            if event.type == VICTORY:
                self.atual = self.gui
                self.atual.game_loop()
                self.atual.check_events(events)
                pygame.event.post(VICTORY_MENU)
            if event.type == DEFEAT:
                self.atual = self.gui
                self.atual.game_loop()
                self.atual.check_events(events)
                pygame.event.post(DEFEAT_MENU)
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




