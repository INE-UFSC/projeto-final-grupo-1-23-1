import pygame
import constantes
import os
from mapa import Mapa
import mapa_1
from pacman import Pacman
from ghostman import Ghostman
from pygame.locals import *
from collision_manager import CollisionManager
from utils import get_path

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

        self.mapa = Mapa(mapa_1.mapa1)
    def novo_jogo(self):
        self.definir_entidades()
        self.iniciar_jogo()

    def definir_entidades(self):
        self.player = Ghostman()
        self.pac = Pacman(150 , 163)
        self.pac_2 = Pacman(550, 163)
        self.pac_3 = Pacman(150, 400)
        self.pac_4 = Pacman(550, 400)


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

    def mostrar_logo(self, pos_x, pos_y):
        start_logo_rect = self.pacman_start_logo.get_rect()
        start_logo_rect.midtop = (pos_x, pos_y)
        self.tela.blit(self.pacman_start_logo, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(get_path('audios', constantes.MUSICA_START)))
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
                    pygame.mixer.Sound(os.path.join(get_path('audios', constantes.TECLA_START))).play()

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
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.iniciar_movimentacao_dos_personagens()
            self.conferir_personagens_vivos()
            self.player.colisao_tela()
            #self.player.colisao_mapa(self.Mapa.wallGroup)
            #self.player.colisao_bolinhas(self.mapa.bolinhas)
            self.conferir_colisoes()
            self.draw()
            print(self.conferir_condicoes_de_fim())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
        self.esta_rodando = False

            #self.mapa.atualizar()
            #pacman1.movimento_pacman(b)#tentando implementar colisao
            #pacman2.movimento_pacman()
            #pacman1.colisao_ghostman(player)
            #pacman2.colisao_ghostman(player)


    def mostrar_tela_game_over(self):
        pass

    def iniciar_movimentacao_dos_personagens(self):
        self.player.ghostman_movimentacao()
        for pacman in self.grupo_pacmans:
            pacman.movimentacao()

    def conferir_condicoes_de_fim(self):
        if self.mapa.acabaram_as_bolinhas() or len(self.grupo_pacmans):
            return True
        else:
            return False



#pacman1 = PacmanRight()
#pacman2 = PacmanLeft()
g = Main()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()
