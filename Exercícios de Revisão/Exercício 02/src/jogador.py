from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from armas import Disparavel, Arma, Golpe

class Jogador:
    def __init__(self, no : str):
        self.nome = no
        self.energia = 150
        self.armas = []

    def atirar(self, d: "Disparavel", j: "Jogador"):
        d.disparar(j)

    def municiar(self, d: "Disparavel"):
        d.recarregar()

    def bater(self, j : "Jogador", g : "Golpe" = None, a: "Arma" = None):
        if a != None:
            a.agredir(j)
        else:
            g.golpear(j)

    def __str__(self):
        if self.energia > 0:
            return f"{self.nome} {self.energia:.2f}"
        else:
            return f"{self.nome} MORREU!"