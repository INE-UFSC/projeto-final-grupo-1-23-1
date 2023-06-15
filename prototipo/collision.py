import pygame

class Collision:
    def __init__(self, grupo1: pygame.sprite.Group, grupo2: pygame.sprite.Group) -> None:
        self.__grupo1 = grupo1
        self.__grupo2 = grupo2
    #detecta colisao entre 2 grupos de sprites (pygame.Sprite.Group)
    def detect_collision(self) -> bool:
        collision_dict = pygame.sprite.groupcollide(self.grupo1, self.grupo2, False, False)
        #grupo1 = quem foi colidido
        #grupo2 = quem colidiu com o grupo 1
        if (collision_dict):

            return True
        else:
            return False

    @property
    def grupo1(self):
        return self.__grupo1

    @property
    def grupo2(self):
        return self.__grupo2

    def getcolisores(self):
        collision_dict = pygame.sprite.groupcollide(self.grupo1, self.grupo2, False, False)
        group1 = collision_dict.keys()
        group2 = collision_dict.values()
        return group1,group2
