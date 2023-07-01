import pygame
from pygame import *
import os
from utils import get_path
import constantes
from mapa import Mapa
import mapa_1
from pacman import Pacman
from ghostman import Ghostman
from collision_manager import CollisionManager

class Match:
    def __init__(self):
        self.programa_esta_aberto = True
        self.jogando = False
        self.relogio = pygame.time.Clock()


    def cria_tela(self):
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)

    def iniciar_jogo(self):
        self.abrir_mapa()
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.current_timer = pygame.time.get_ticks()

            self.iniciar_movimentacao_dos_personagens()

            self.conferir_personagens_vivos()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.programa_esta_aberto = False
                    pygame.quit()

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def nova_partida(self):
        self.jogando = True
        self.organizar_diretorios()
        self.cria_tela()
        self.todas_as_sprites = pygame.sprite.Group()
        self.instancia_entidades_da_partida()
        self.reproduzir_musica_start()
        self.iniciar_jogo()

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

        self.colisoes = CollisionManager(self.mapa, self.grupo_ghostman, self.grupo_pacmans)

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

    def conferir_colisoes(self):
        self.colisoes.collisions()

    def conferir_personagens_vivos(self):
        for pacman in self.grupo_pacmans:
            if pacman.vidas <= 0:
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

        pygame.display.flip()


    def conferir_condicoes_de_fim(self):
        if self.mapa.acabaram_as_bolinhas() or len(self.grupo_pacmans):
            return True
        else:
            return False