from abc import ABC, abstractmethod
import math

class Personagem(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.direction = "right"

    def checar_colisao(self, obj):
        distance = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
        if distance < self.radius + obj.radius:
            return True
        return False
    
    def desenha_sprite(self, screen):
        raise NotImplementedError("Subclasses must implement the 'draw' method.")
