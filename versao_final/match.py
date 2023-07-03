import pygame
from pygame import *
import os
from utils import get_path
import constantes
import sys
from mapa import Mapa
import mapa_1
from pacman import Pacman
from ghostman import Ghostman
from collision_manager import CollisionManager

class Match:
    def __init__(self, screen):
        self.programa_esta_aberto = True
        self.jogando = False
        self.relogio = pygame.time.Clock()
        self.tela = screen

    def iniciar_partida(self):
        self.abrir_mapa()
        self.iniciar_movimentacao_dos_personagens()

    def update(self):
        self.relogio.tick(constantes.FPS)
        self.current_timer = pygame.time.get_ticks()
        self.movimentar_personagens()
        self.conferir_personagens_vivos()
        self.acabaram_as_bolinhas()
        self.conferir_condicoes_de_fim

    def game_loop(self):
        self.jogando = True
        self.organizar_diretorios()
        #self.cria_tela()
        self.todas_as_sprites = pygame.sprite.Group()
        self.instancia_entidades_da_partida()
        self.reproduzir_musica_start()
        self.iniciar_partida()
        pygame.display.set_caption('Ghostman')
        self.relogio.tick(constantes.FPS)
        while self.jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.programa_esta_aberto = False
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()

    def reproduzir_musica_start(self):
        pygame.mixer.music.load(os.path.join(get_path('audios', constantes.MUSICA_START)))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)

    def organizar_diretorios(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')

    def abrir_mapa(self):
        self.mapa.carregar_mapa()
        self.mapa_surface = self.mapa.tela.copy()

    def instancia_entidades_da_partida(self):
        self.mapa = Mapa(mapa_1.mapa1)
        self.player = Ghostman()
        self.pacman_1 = Pacman(100, 65)
        self.pacman_2 = Pacman(700, 65)
        self.pacman_3 = Pacman(100, 765)
        self.pacman_4 = Pacman(700, 765)

        self.grupo_ghostman = pygame.sprite.Group()
        self.grupo_pacmans = pygame.sprite.Group()

        self.todas_as_sprites.add(self.pacman_1)
        self.todas_as_sprites.add(self.pacman_2)
        self.todas_as_sprites.add(self.pacman_3)
        self.todas_as_sprites.add(self.pacman_4)
        self.todas_as_sprites.add(self.player)

        self.grupo_pacmans.add(self.pacman_1)
        self.grupo_pacmans.add(self.pacman_2)
        self.grupo_pacmans.add(self.pacman_3)
        self.grupo_pacmans.add(self.pacman_4)

        self.grupo_ghostman.add(self.player)

        self.colisoes = CollisionManager(self.mapa, self.grupo_ghostman, self.grupo_pacmans)

    def movimentar_personagens(self):
        self.player.input_movimentacao()
        self.player.ghostman_movimentacao('x')
        self.player.handle_current_direction()
        self.colisoes.colisoes_ghostman()

        self.player.ghostman_movimentacao('y')
        self.player.handle_current_direction()
        self.colisoes.colisoes_ghostman()

        self.player.colisao_tela()
        for pacman in self.grupo_pacmans:
            pacman.movimentacao_continua()
            self.colisoes.colisoes_pacman(pacman)
            pacman.colisao_tela()

    def iniciar_movimentacao_dos_personagens(self):
        for pacman in self.grupo_pacmans:
            pacman.movimentacao_inicial()

    def conferir_personagens_vivos(self):
        for pacman in self.grupo_pacmans:
            if pacman.vidas == 0:
                self.grupo_pacmans.remove(pacman)

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
            # onde que eu deixo a funçao set_timer eupdate:
            caixa.update(self.current_timer)
        self.player.draw(self.tela)

        for pacman in self.grupo_pacmans:
            pacman.draw(self.tela)
            pacman.update(self.current_timer)

        pygame.display.flip()

    def conferir_personagens_vivos(self):
        for pacman in self.grupo_pacmans:
            if pacman.vidas == 0:
                self.grupo_pacmans.remove(pacman)

    def acabaram_as_bolinhas(self):
        if CollisionManager.bolinhas == 0:
            return True
        else:
            False

    def conferir_condicoes_de_fim(self):
        if self.grupo_pacmans == []:
            print("Vitória")
            fonte = pygame.font.SysFont("Monospace", 15, True, True)
            formatacao_texto = fonte.render('VITÓRIA', False, (255, 255, 255))
            self.tela.blit(formatacao_texto, (450, 40))
            return True
        if self.acabaram_as_bolinhas():
            print("Derrota")
            fonte = pygame.font.SysFont("Monospace", 15, True, True)
            formatacao_texto = fonte.render('DERROTA', False, (255, 255, 255))
            self.tela.blit(formatacao_texto, (450, 40))
            return False

    def instancia_sistema_de_colisoes(self):
        self.colisoes = CollisionManager(self.mapa, self.grupo_ghostman, self.grupo_pacmans)

    def instancia_mapa(self):
        self.mapa = Mapa(mapa_1.mapa1)

    def instancia_personagens(self):
        self.player = Ghostman()
        self.pacman_1 = Pacman(120, 425)
        self.pacman_2 = Pacman(750, 425)
        self.pacman_3 = Pacman(150, 425)
        self.pacman_4 = Pacman(770, 425)

        self.grupo_ghostman = pygame.sprite.Group()
        self.grupo_pacmans = pygame.sprite.Group()

        self.todas_as_sprites.add(self.pacman_1)
        self.todas_as_sprites.add(self.pacman_2)
        self.todas_as_sprites.add(self.pacman_3)
        self.todas_as_sprites.add(self.pacman_4)
        self.todas_as_sprites.add(self.player)

        self.grupo_pacmans.add(self.pacman_1)
        self.grupo_pacmans.add(self.pacman_2)
        self.grupo_pacmans.add(self.pacman_3)
        self.grupo_pacmans.add(self.pacman_4)

        self.grupo_ghostman.add(self.player)