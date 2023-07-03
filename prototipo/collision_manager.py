from collision import Collision
import pygame
class CollisionManager:
    #recebe grupo de sprites para detectar colisao
    def __init__(self, mapa, grupo_ghostman, grupo_pacmans) -> None:
        #local onde vai ficar armazenado as listas dos objetos
        self.__mapa = mapa
        self.__ghostman = grupo_ghostman
        self.__pacmans = grupo_pacmans


    #ações realisadas no jogo quando é detectado colisão
    def colisoes_pacman(self, pacman):
        if (self.collision_walls_pacman()):
            collison_list = pygame.sprite.spritecollide(pacman, self.walls, False)
            for walls in collison_list:
                pacman.colidiu_por_wall(walls)

        if (self.collision_gates_pacman()):
            dict = (Collision(self.pacmans, self.gates).dict())
            for pacman, gates in dict.items():
                pacman.colidiu_por_wall()

        if (self.collision_bolinha_pacman()):#seriaos pacmans
            dict = (Collision(self.pacmans, self.bolinhas).dict())

            for pacman, bolinhas in dict.items():
                for bolinha in bolinhas:
                    pacman.colidiu_com_bolinha()
                    bolinha.colidida_por_pacman()


        if (self.collision_pacman_bolao()):
            dict = (Collision(self.pacmans, self.boloes).dict())
            for pacman, boloes in dict.items():
                for bolao in boloes:
                    bolao.hit(self.pacmans)

    def colisoes_ghostman(self):
        if (self.collision_walls_ghostman()):
            dict = (Collision(self.ghostmans, self.walls).dict())
            for ghost, walls in dict.items():
                ghost.colidiu_com_wall()    

        if (self.collision_caixa_supresa_ghostman()):
            dict = (Collision(self.ghostmans, self.caixas_supresas).dict())

            for player, caixas in dict.items():
                for caixa in caixas:
                    caixa.hit(player)    

        if(self.collision_pacman_ghostman()):
            dict = (Collision(self.ghostmans, self.pacmans).dict())

            for ghost, pacmans in dict.items():
                for pacman in pacmans:
                    pacman.colidido_por_ghostman()
                    ghost.colidiu_com_pacman(pacman)

    #verificar se colidiu
    def collision_bolinha_pacman(self) -> bool:
        if (Collision(self.pacmans, self.bolinhas).detect_collision()):#seria com os pacmans
            return True
        else:
            return False
    def collision_pacman_ghostman(self):
        if (Collision(self.ghostmans, self.pacmans).detect_collision()):
            return True
        else:
            return False

    def collision_pacman_bolao(self):
        return Collision(self.pacmans, self.boloes).detect_collision()

    def collision_caixa_supresa_ghostman(self):
        if (Collision(self.ghostmans, self.caixas_supresas).detect_collision()):
            return True
        else:
            return False

    def collision_walls_ghostman(self):
        if (Collision(self.ghostmans, self.walls).detect_collision()):
            return True
        else:
            return False

    def collision_walls_pacman(self):
        if (Collision(self.pacmans, self.walls).detect_collision()):
            return True
        else:
            return False
        
    def collision_gates_pacman(self):
        if (Collision(self.pacmans, self.walls).detect_collision()):
            return True
        else:
            return False

    #nao sei se ultilizaremos essa funçao
    def ghostman_life_detect(self):
        pass

#chama as lsitas do mapa,a fim de poder usar melhor nas colisoes
    @property
    def mapa(self):
        return self.__mapa

    @property
    def bolinhas(self):
        return self.__mapa.bolinhas

    @property
    def ghostmans(self):
        return self.__ghostman

    @property
    def pacmans(self):
        return self.__pacmans

    @property
    def boloes(self):
        return self.mapa.boloes

    @property
    def portoes(self):
        return self.mapa.portoes
    
    @property
    def walls(self):
        return self.mapa.walls

    @property
    def caixas_supresas(self):
        return self.mapa.caixas_supresas