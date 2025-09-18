from abc import ABCMeta, abstractmethod

class Jogador:
    def __init__(self, nome: str):
        self._nome = nome
        self.vida = 100
        self.arma = None

    def pegar(self, a):
        self.arma = a

    def bater(self, j):
        j.vida -= 1

    def disparar(self, j):
        self.arma.atirar(j)
    
    def __str__(self):
        txt = f"Nome: {self._nome} │ Vida: {self.vida}"
        txt += f"\nArma: {self.arma}"
        return txt

class Disparavel(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def atirar(self, j: Jogador):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Disparavel):
    def __init__(self):
        self.balas = 7

    def atirar(self, j: Jogador):
        if self.balas > 0:
            self.balas -= 1
            j.vida -= 5
        else: 
            raise Exception("A arma Revolver ta sem bala")

    def recarregar(self):
        self._balas = 7

    def __str__(self):
        return f"Revolver com ({self.balas} balas)"

class Bazuca(Disparavel):
    def __init__(self):
        self.balas = 1

    def atirar(self, j: Jogador):
        if self.balas > 0:
            self.balas -= 1
            j.vida -= 50
        else: 
            raise Exception("A arma Bazuca ta sem bala")

    def recarregar(self):
        self._balas = 1

    def __str__(self):
        return f"Bazuca com {self.balas} balas"

if __name__ == "__main__":
    j1 = Jogador("Player1") 
    j2 = Jogador("Player2")
    r = Revolver()
    b = Bazuca()
    j1.pegar(r)
    j2.pegar(b)
    j1.disparar(j2)
    j2.disparar(j1)
    print(f"{j1}\n{j2}")