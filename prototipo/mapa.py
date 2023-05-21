
import constantes
import pygame
from mapa_1 import mapa_original


mapaPath = "imagensMapa/"


class Mapa:
    def __init__(self):
        self.mapa = mapa_original
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))



    def desenhar_mapa(self):
        self.tela.fill((0, 0, 0))  # Flushes the screen
        # Draws game elements
        tile = 0

        for i in range(3, len(self.mapa) - 2):
            for j in range(len(self.mapa[0])):
                if self.mapa[i][j] == 3:  # Draw wall
                    nome_do_arquivo = str(tile)
                    if len(nome_do_arquivo) == 1:
                        nome_do_arquivo = "00" + nome_do_arquivo
                    elif len(nome_do_arquivo) == 2:
                        nome_do_arquivo = "0" + nome_do_arquivo
                    # Seleciona a imagem desejada
                    nome_do_arquivo = "tile" + nome_do_arquivo + ".png"
                    tileImage = pygame.image.load(mapaPath + nome_do_arquivo)
                    tileImage = pygame.transform.scale(tileImage, (constantes.TAMANHO_DO_BLOCO, constantes.TAMANHO_DO_BLOCO))

                    # coloca as imagens na tela
                    self.tela.blit(tileImage, (j * constantes.TAMANHO_DO_BLOCO, i * constantes.TAMANHO_DO_BLOCO, constantes.TAMANHO_DO_BLOCO, constantes.TAMANHO_DO_BLOCO))


                elif self.mapa[i][j] == 2:  # Desenha os pontinhos
                    pygame.draw.circle(self.tela, constantes.AMARELO, (j * constantes.TAMANHO_DO_BLOCO + constantes.TAMANHO_DO_BLOCO // 2, i * constantes.TAMANHO_DO_BLOCO + constantes.TAMANHO_DO_BLOCO // 2),
                                       constantes.TAMANHO_DO_BLOCO // 4)

                elif self.mapa[i][j] == 6:  # Pontinho maior (poder dos pacman)
                    pygame.draw.circle(self.tela, constantes.AMARELO, (j * constantes.TAMANHO_DO_BLOCO + constantes.TAMANHO_DO_BLOCO // 2, i * constantes.TAMANHO_DO_BLOCO + constantes.TAMANHO_DO_BLOCO // 2),
                                       constantes.TAMANHO_DO_BLOCO // 2)

    def carregar_mapa(self):
        self.desenhar_mapa()

