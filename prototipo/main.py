import pygame
import sys
import constantes
import os
from mapa import Mapa
import mapa_1
from pacman import Pacman
from ghostman import Ghostman
from pygame.locals import *
from collision_manager import CollisionManager
from utils import get_path
from gui import *

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA_MENU, constantes.ALTURA_MENU))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.todas_as_sprites = pygame.sprite.Group()
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()
        self.jogando = False
        #entidades no mais

        #interface
        self.gui = Gui()

        self.mapa = Mapa(mapa_1.mapa1)

        #current_time:
        self.current_timer = 0
    def novo_jogo(self):
        self.definir_entidades()
        self.iniciar_jogo()

    def definir_entidades(self):
        self.player = Ghostman()
        self.pac = Pacman(120 , 425)
        self.pac_2 = Pacman(750, 425)
        self.pac_3 = Pacman(150, 425)
        self.pac_4 = Pacman(770, 425)


        self.grupo_ghostman = pygame.sprite.Group()
        self.grupo_pacmans = pygame.sprite.Group()

        self.todas_as_sprites.add(self.pac)
        self.todas_as_sprites.add(self.pac_2)
        self.todas_as_sprites.add(self.pac_3)
        self.todas_as_sprites.add(self.pac_4)
        self.todas_as_sprites.add(self.player)


        self.grupo_pacmans.add(self.pac)
        self.grupo_pacmans.add(self.pac_2)
        self.grupo_pacmans.add(self.pac_3)
        self.grupo_pacmans.add(self.pac_4)
        self.grupo_ghostman.add(self.player)

        self.colisoes = CollisionManager(self.mapa, self.grupo_ghostman, self.grupo_pacmans)
        
    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.pacman_start_logo = os.path.join(diretorio_imagens, constantes.PACMAN_START_LOGO)
        self.pacman_start_logo = pygame.image.load(get_path('imagens', constantes.PACMAN_START_LOGO)).convert()

    def mostrar_texto(self, texto, tamanho_da_fonte, cor_do_texto, posicao_x, posicao_y):
        fonte = pygame.font.Font(self.fonte, tamanho_da_fonte)
        texto = fonte.render(texto, True, cor_do_texto)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (posicao_x, posicao_y)
        self.tela.blit(texto, texto_rect)


    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(get_path('audios', constantes.MUSICA_START)))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)

    def game_loop(self):
        while True:
            self.relogio.tick(constantes.FPS)
            events = self.handle_events()
            if self.jogando == False:
                self.gui.game_loop(events)
            else:
                self.novo_jogo()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == START_GAME:
                self.jogando = True
            if event.type == pygame.QUIT:
                self.esta_rodando = False
                pygame.quit()
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.Sound(os.path.join(get_path('audios', constantes.TECLA_START))).play()
        return events

    def abrir_mapa(self):
        self.mapa.carregar_mapa()
        self.mapa_surface = self.mapa.tela.copy()

    def draw(self):

        self.tela.fill(constantes.PRETO)
        self.tela.blit(self.mapa_surface, (0, 0))

        for bolinha in self.mapa.bolinhas:
            if bolinha.estavel:
                bolinha.desenhar(self.tela)

        for bolao in self.mapa.boloes:
            if bolao.estavel:
                bolao.desenhar(self.tela)
                # onde que eu deixo a funçao set_timer eupdate:
                bolao.update(self.current_timer)

        for caixa in self.mapa.caixas_supresas:
            caixa.desenhar(self.tela)
            #onde que eu deixo a funçao set_timer eupdate:
            caixa.update(self.current_timer)
        self.player.draw(self.tela)

        for pacman in self.grupo_pacmans:
            pacman.draw(self.tela)


        #self.pac.draw(self.tela)


        pygame.display.flip()

    def conferir_colisoes(self):
        self.colisoes.collisions()

    def conferir_personagens_vivos(self):
        for pacman in self.grupo_pacmans:
            if pacman.vidas <= 0:
                self.grupo_pacmans.remove(pacman)

    def iniciar_jogo(self):
        self.abrir_mapa()
        jogando = True
        while jogando:
            self.relogio.tick(constantes.FPS)
            self.current_timer = pygame.time.get_ticks()

            self.iniciar_movimentacao_dos_personagens()

            self.conferir_personagens_vivos()
            #self.player.colisao_mapa(self.Mapa.wallGroup)
            #self.player.colisao_bolinhas(self.mapa.bolinhas)
            #self.conferir_colisoes()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.esta_rodando = False
                    pygame.quit()

            #self.mapa.atualizar()
            #pacman1.movimento_pacman(b)#tentando implementar colisao
            #pacman2.movimento_pacman()
            #pacman1.colisao_ghostman(player)
            #pacman2.colisao_ghostman(player)


    def mostrar_tela_game_over(self):
        pass

    def iniciar_movimentacao_dos_personagens(self):
        self.player.input_movimentacao()

        self.player.ghostman_movimentacao('x')
        self.player.handle_current_direction()
        self.conferir_colisoes()

        self.player.ghostman_movimentacao('y')
        self.player.handle_current_direction()
        self.conferir_colisoes()

        self.player.colisao_tela()
        for pacman in self.grupo_pacmans:
            pacman.movimentacao()
            pacman.colisao_tela()

    def conferir_condicoes_de_fim(self):
        if self.mapa.acabaram_as_bolinhas() or len(self.grupo_pacmans):
            return True
        else:
            return False

g = Main()
#g.mostrar_tela_start()
g.game_loop()

