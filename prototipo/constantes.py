
from math import pi
from mapa_1 import mapa1
from pygame import *

#eventos personalizados para a gui
SHOW_MAIN_MENU = USEREVENT +1
SHOW_MAP_MENU = USEREVENT + 2
SHOW_HOW_TO_MENU = USEREVENT + 3
SHOW_CREDITS_MENU = USEREVENT + 4
QUIT_MENU = USEREVENT + 5
EXIT = USEREVENT + 6
START_GAME = USEREVENT + 7

MANSION_MAP = USEREVENT + 8
FOOTBALL_MAP = USEREVENT + 9
TRANSIT_MAP = USEREVENT + 10



TAMANHO_DO_BLOCO = 28
#dimensoes
LARGURA = len(mapa1[0]) * TAMANHO_DO_BLOCO
ALTURA = len(mapa1) * TAMANHO_DO_BLOCO
LARGURA_MENU = 1280
ALTURA_MENU = 720

TITULO_JOGO = 'PacMan'

#FPS
FPS = 30

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO =  (244, 233, 51)
AZUL = (0, 0, 255)
PI = pi


PACMAN_START_LOGO = 'pacman-logo-1.png'

FONTE = 'arial'

#audio
MUSICA_START = 'intermission.wav'
TECLA_START = 'munch_1.wav'
import math
from math import pi
#dimensoes


TITULO_JOGO = 'PacMan'

#FPS
FPS = 30

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO =  (244, 233, 51)
AZUL = (0, 0, 255)
PI = math.pi
ROSA = (218,112,214)

PACMAN_START_LOGO = 'pacman-logo-1.png'
GHOSTMAN = 'ghostman.png'
PACMAN = 'pacman.png'

FONTE = 'arial'

#audio
MUSICA_START = 'intermission.wav'
TECLA_START = 'munch_1.wav'