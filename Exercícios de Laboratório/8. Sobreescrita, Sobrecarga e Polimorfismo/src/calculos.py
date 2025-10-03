from abc import ABC, abstractmethod 
from typing import List
from math import sqrt

class Operacao(ABC):
    operador: float

    def __init__(self, o: float):
        self.operador = o

    @abstractmethod
    def calcular(self, n: float) -> float:
        pass

    @abstractmethod
    def calcular_inverso(self, n: float) -> float:
        pass  

class Adicao(Operacao):
    def calcular(self, n: float) -> float:
        return n + self.operador

    def calcular_inverso(self, n: float) -> float:
        return n - self.operador

class Subtracao(Operacao):
    def calcular(self, n: float) -> float:
        return n - self.operador 
    
    def calcular_inverso(self, n: float) -> float:
        return n + self.operador

class Divisao(Operacao):
    def calcular(self, n: float) -> float:
        return n / self.operador
    
    def calcular_inverso(self, n: float) -> float:
        return n * self.operador

class Multiplicacao(Operacao):
    def calcular(self, n: float) -> float:
        return n * self.operador

    def calcular_inverso(self, n: float) -> float:
        return n / self.operador

class RaizQuadrada(Operacao):
    def calcular(self, n: float) -> float:
        return sqrt(n)

    def calcular_inverso(self, n: float) -> float:
        return n ** 2

class AoQuadrado(Operacao):
    def calcular(self, n: float) -> float:
        return n ** 2

    def calcular_inverso(self, n: float) -> float:
        return sqrt(n)

class Calculadora:
    resultado: float
    operacoes: List[Operacao]

    def __init__(self):
        self.resultado = 0
        self.operacoes = []

    def add_operacao(self, op: Operacao):
        self.operacoes.append(op)

    def calcular_total(self):
        self.resultado = 0
        for op in self.operacoes:
            self.resultado = op.calcular(self.resultado)

    def desfazer_ultima(self):
        op = self.operacoes.pop()
        self.resultado = op.calcular_inverso(self.resultado)

    def __str__(self):
        return f"Resultado = {self.resultado}"

if __name__ == "__main__":
    c = Calculadora()
    mais = Adicao(2.0)
    menos = Subtracao(1.0)
    c.add_operacao(mais)
    c.add_operacao(menos)
    c.calcular_total()
    print(c)