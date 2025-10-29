from abc import ABC, ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jogador import Jogador

class Arma(ABC):
    destruicao : float

    def __init__(self, po : float):
        self.destruicao = po

    def agredir(self, j: "Jogador"):
        j.energia -= 5

    def __str__(self):
        return f"Poder destruicao: {self.destruicao}\n Agredir = 5"
    
class Disparavel(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def disparar(self, j: "Jogador"):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartuchos : int

    def __init__(self):
        super().__init__(20)
        self.cartuchos = 6

    def disparar(self, j : "Jogador"):
        if self.cartuchos > 0:
            j.energia -= self.destruicao
            self.cartuchos -= 1
        else:
            raise Exception("Revolver vazio!")
    
    def recarregar(self):
        self.cartuchos = 6

    def __str__(self):
        return f"Revolver com {self.cartuchos} catuchos {super().__str__()}"
        
class LancaChamas(Arma, Disparavel):
    gas : float

    def __init__(self):
        super().__init__(30)
        self.gas = 100

    def disparar(self, j):
        if self.gas > 0:
            j.energia -= self.destruicao
            self.gas -= 5.5
        else:
            raise Exception("Acabou o gás do Lanca Chamas")

    def recarregar(self):
        self.gas = 100
    
    def __str__(self):
        return f"Lanca Chamas {super().__str__()}"

class Faca(Arma):
    lamina : int

    def __init__(self):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, j):
        if self.lamina > 0:
            j.energia -= self.destruicao
            self.lamina -= 1
        else:
            super().agredir(j)
    
    def __str__(self):
        if self.lamina > 0:
            return f"Faca integrida da laminha {self.lamina} {super().__str__()}"
        else:
            return f"Lamina quebrada. Agredir = 5"

class Golpe(ABC):
    @abstractmethod
    def golpear(self, j : "Jogador"):
        pass

class Soco(Golpe):
    def golpear(self, j):
        j.energia -= 1

class Chute(Golpe):
    def golpear(self, j):
        j.energia -= 2

class Soco_Ingles(Faca, Soco):
    def __init__(self):
        super().__init__()
        self.destruicao +=1

    def agredir(self, j):
        super().agredir(j)
        self.golpear(j)
    
    def __str__(self):
        return f"Soco Ingles {super().__str__()}"

         
