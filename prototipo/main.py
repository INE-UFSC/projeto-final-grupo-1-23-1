import pygame
import constantes
import os
from mapa import Mapa
import mapa_1
from pacman_right import PacmanRight
from pacman_left import PacmanLeft
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
        self.carregar_arquivos()
        self.jogando = True
        #entidades no mais

        self.mapa = Mapa(mapa_1.mapa_original)
    def novo_jogo(self):
        self.definir_entidades()
        self.iniciar_jogo()

    def definir_entidades(self):
        self.player = Ghostman()
        self.pac = Pacman()
        self.grupo_ghostman = pygame.sprite.Group()
        self.grupo_pacmans = pygame.sprite.Group()
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
        self.mapa.carregar_mapa()
        self.mapa_surface = self.mapa.tela.copy()
    def draw(self):
        self.tela.fill(constantes.PRETO)
        self.tela.blit(self.mapa_surface, (0, 0))
        self.player.draw(self.tela)
        self.pac.desenhar(self.tela)
        #pacman1.draw(self.tela)
        #pacman2.draw(self.tela)
        pygame.display.flip()

    def iniciar_jogo(self):
        self.abrir_mapa()
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.player.ghostman_movimentacao()
            self.pac.movimentacao()
            self.draw()
            self.player.colisao_tela()
            self.player.colisao_mapa(self.mapa.lista_rect)
            self.player.colisao_bolinhas(self.mapa.bolinhas)
            self.mapa.atualizar()
            #pacman1.movimento_pacman(b)#tentando implementar colisao
            #pacman2.movimento_pacman()
            #pacman1.colisao_ghostman(player)
            #pacman2.colisao_ghostman(player)


    def mostrar_tela_game_over(self):
        pass


#pacman1 = PacmanRight()
#pacman2 = PacmanLeft()
g = Main()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()
