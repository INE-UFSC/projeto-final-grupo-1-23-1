from collision import Collision
class CollisionManager:
    #recebe grupo de sprites para detectar colisao
    def __init__(self, mapa= None) -> None:
        #local onde vai ficar armazenado as listas dos objetos
        self.__mapa = mapa

    #ações realisadas no jogo quando é detectado colisão
    def collisions(self) -> None:
        if (self.collision_bolinha_pacman()):#seriaos pacmans
            #chama os colisores.Grupoa= list e Grupob = list(list)
            grupoa, grupob = (Collision(self.pacmans, self.bolinhas).getcolisores())
            for x1 in grupoa:
                x1.hit()
            for g2 in grupob:
                for x2 in g2:
                    x2.hit()
        if(self.collision_pacman_ghostman()):
            grupoa, grupob = (Collision(self.ghostmans, self.pacmans).getcolisores())
            for x1 in grupoa:
                x1.hit()

            for g2 in grupob:
                for x2 in g2:
                    x2.hit()

        if (self.collision_caixa_supresa_ghostman()):
            grupoa, grupob = (Collision(self.ghostmans, self.caixas_supresas).getcolisores())

            for x1 in grupoa:
                x1.hit()

            for g2 in grupob:
                for x2 in g2:
                    x2.hit()

        if (self.collision_walls_pacman()):
            grupoa, grupob = (Collision(self.pacmans, self.walls).getcolisores())

            for x1 in grupoa:
                x1.hit()

            for g2 in grupob:
                for x2 in g2:
                    x2.hit()

        if (self.collision_walls_ghostman()):
            grupoa, grupob = (Collision(self.ghostmans, self.walls).getcolisores())

            for x1 in grupoa:
                x1.hit()

            for g2 in grupob:
                for x2 in g2:
                    x2.hit()


        self.ghostman_life_detect()

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

    #nao sei se ultilizaremos essa funçao
    def ghostman_life_detect(self):
        pass

#chama as lsitas do mapa,a fim de poder usar melhor nas colisoes
    @property
    def mapa(self):
        return self.__mapa

    @property
    def bolinhas(self):
        return self.mapa.bolinhas

    @property
    def ghostmans(self):
        return self.mapa.ghostmans

    @property
    def pacmans(self):
        return self.mapa.pacmans

    @property
    def walls(self):
        return self.mapa.walls
    @property
    def caixas_supresas(self):
        return self.mapa.caixas_supresas