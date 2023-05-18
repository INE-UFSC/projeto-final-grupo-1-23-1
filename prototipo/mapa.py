# Legenda do mapa
# 0 = espaço vazio,
# 1 = espaço com bolinha,
# 2 = Espaço com a bolinha maior,
# 3 = Parede vertical,
# 4 = linha horizontal,
# 5 = Curva topo direita,
# 6 = Curva topo esquerda,
# 7 = Curva esquerda baixo,
# 8 = Curva Direita baixo
# 9 = portão dos fantasmas
import constantes
import mapa_1
import pygame

piscando = False


class Mapa:
    def __init__(self, numero_do_mapa):
        self.mapa_atual = numero_do_mapa
        #self.moedas_comidas =  self.mapa_atual.count(0)
        self.mapa_perdido = False # Se tornará True quando todos as "moedas" forem comidas
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))


    def desenhar_mapa(self):
        largura_do_bloco = ((constantes.LARGURA - 50) // 32)  # é a altura de cada peça
        altura_do_bloco = (constantes.ALTURA // 31)  # É a largura de cada peça do mapa

        for i in range(len(self.mapa_atual)):
            for j in range(len(self.mapa_atual[i])):
                ''' if level[i][j] == 1:
                     #aqui começa o desenho de cada item no mapa, o primerio é o 1, que é o espaço com a bolinha
                     # na funcao draw circle, o priemeiro parametro é a tela, o segundo a cor e depois as cordenadas
                     # j*num indica de será na coluna j e somamos mais meio tamanho para centralizar o ponto
                     # quatro é o tamanho do ponto que é a sprinkle'''
                if self.mapa_atual[i][j] == 1:
                    pygame.draw.circle(self.tela, 'white', (j * altura_do_bloco + (0.5 * altura_do_bloco), i * largura_do_bloco + (0.5 * largura_do_bloco)), 4)
                if self.mapa_atual[i][j] == 2 and not piscando:
                    pygame.draw.circle(self.tela, 'white', (j * altura_do_bloco + (0.5 * altura_do_bloco), i * largura_do_bloco + (0.5 * largura_do_bloco)), 10)
                if self.mapa_atual[i][j] == 3:
                    pygame.draw.line(self.tela, constantes.AZUL, (j * altura_do_bloco + (0.5 * altura_do_bloco), i * largura_do_bloco),
                                     (j * altura_do_bloco + (0.5 * altura_do_bloco), i * largura_do_bloco + largura_do_bloco), 3)
                if self.mapa_atual[i][j] == 4:
                    pygame.draw.line(self.tela, constantes.AZUL, (j * altura_do_bloco, i * largura_do_bloco + (0.5 * largura_do_bloco)),
                                     (j * altura_do_bloco + altura_do_bloco, i * largura_do_bloco + (0.5 * largura_do_bloco)), 3)
                if self.mapa_atual[i][j] == 5:
                    pygame.draw.arc(self.tela, constantes.AZUL,
                                    [(j * altura_do_bloco - (altura_do_bloco * 0.4)) - 2, (i * largura_do_bloco + (0.5 * largura_do_bloco)), altura_do_bloco, largura_do_bloco],
                                    0, constantes.PI / 2, 3)
                if self.mapa_atual[i][j] == 6:
                    pygame.draw.arc(self.tela, constantes.AZUL,
                                    [(j * altura_do_bloco + (altura_do_bloco * 0.5)), (i * largura_do_bloco + (0.5 * largura_do_bloco)), altura_do_bloco, largura_do_bloco], constantes.PI / 2, constantes.PI, 3)
                if self.mapa_atual[i][j] == 7:
                    pygame.draw.arc(self.tela, constantes.AZUL, [(j * altura_do_bloco + (altura_do_bloco * 0.5)), (i * largura_do_bloco - (0.4 * largura_do_bloco)), altura_do_bloco, largura_do_bloco],
                                    constantes.PI,
                                    3 * constantes.PI / 2, 3)
                if self.mapa_atual[i][j] == 8:
                    pygame.draw.arc(self.tela, constantes.AZUL,
                                    [(j * altura_do_bloco - (altura_do_bloco * 0.4)) - 2, (i * largura_do_bloco - (0.4 * largura_do_bloco)), altura_do_bloco, largura_do_bloco], 3 * constantes.PI / 2,
                                    2 * constantes.PI, 3)
                if self.mapa_atual[i][j] == 9:
                    pygame.draw.line(self.tela, 'white', (j * altura_do_bloco, i * largura_do_bloco + (0.5 * largura_do_bloco)),
                                     (j * altura_do_bloco + altura_do_bloco, i * largura_do_bloco + (0.5 * largura_do_bloco)), 3)

    def draw_board():
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == 1:
                    pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
                if level[i][j] == 2 and not flicker:
                    pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                if level[i][j] == 3:
                    pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                     (j * num2 + (0.5 * num2), i * num1 + num1), 3)
                if level[i][j] == 4:
                    pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                     (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                if level[i][j] == 5:
                    pygame.draw.arc(screen, color,
                                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                    0, PI / 2, 3)
                if level[i][j] == 6:
                    pygame.draw.arc(screen, color,
                                    [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
                if level[i][j] == 7:
                    pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1],
                                    PI,
                                    3 * PI / 2, 3)
                if level[i][j] == 8:
                    pygame.draw.arc(screen, color,
                                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                    2 * PI, 3)
                if level[i][j] == 9:
                    pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                     (j * num2 + num2, i * num1 + (0.5 * num1)), 3)




    def carregar_mapa(self):
        self.desenhar_mapa()