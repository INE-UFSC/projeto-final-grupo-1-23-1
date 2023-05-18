import pygame
import constantes
import os
from mapa import Mapa
import mapa_1
from pacman import Pacman
from ghostman import Ghostman
from pygame.locals import *

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.todas_as_sprites = pygame.sprite.Group()
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.ghostman = Ghostman(465, 405)
        self.pacman = [Pacman(50, 405), Pacman(100, 405), Pacman(800, 405), Pacman(850, 405)]
        self.carregar_arquivos()
        self.jogando = True

    def novo_jogo(self):
        self.iniciar_jogo()

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.pacman_start_logo = os.path.join(diretorio_imagens, constantes.PACMAN_START_LOGO)
        self.pacman_start_logo = pygame.image.load(self.pacman_start_logo).convert()

    def mostrar_texto(self, texto, tamanho_da_fonte, cor_do_texto, posicao_x, posicao_y):
        fonte = pygame.font.Font(self.fonte, tamanho_da_fonte)
        texto = fonte.render(texto, True, cor_do_texto)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (posicao_x, posicao_y)
        self.tela.blit(texto, texto_rect)

    def mostrar_logo(self, pos_x, pos_y):
        start_logo_rect = self.pacman_start_logo.get_rect()
        start_logo_rect.midtop = (pos_x, pos_y)
        self.tela.blit(self.pacman_start_logo, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, constantes.MUSICA_START))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        self.mostrar_logo(constantes.LARGURA // 2, 80)
        self.mostrar_texto('- Pressione uma tecla para jogar',
                           32,
                           constantes.AMARELO,
                           constantes.LARGURA // 2,
                           480
                           )
        self.mostrar_texto('Antônio Torres, Eric Cardoso, João Victor Cabral, João Vittor Braz',
                           19,
                           constantes.BRANCO,
                           constantes.LARGURA // 2,
                           780
                           )
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios, constantes.TECLA_START)).play()

    def abrir_mapa(self):
        mapa = Mapa(mapa_1.mapa)
        mapa.carregar_mapa()
        self.mapa_surface = mapa.tela.copy()  # Create a copy of the map surface

    def draw(self):
        self.tela.fill(constantes.PRETO)  # Clear the screen
        self.tela.blit(self.mapa_surface, (0, 0))  # Blit the map surface onto the screen
        self.ghostman.draw(self.tela)
        for pacman in self.pacman:
            pacman.draw(self.tela)
        pygame.display.flip()

    def iniciar_jogo(self):
        self.abrir_mapa()
        self.draw()
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.ghostman.move()
            self.ghostman.check_collision()
            self.draw()

    def ghostman_movimentacao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jogando = False
                self.esta_rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ghostman.move_right()
                elif event.key == pygame.K_LEFT:
                    self.ghostman.move_left()
                elif event.key == pygame.K_UP:
                    self.ghostman.move_up()
                elif event.key == pygame.K_DOWN:
                    self.ghostman.move_down()

        self.ghostman.move()

    def mostrar_tela_game_over(self):
        pass

g = Main()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    # g.mostrar_tela_game_over()
