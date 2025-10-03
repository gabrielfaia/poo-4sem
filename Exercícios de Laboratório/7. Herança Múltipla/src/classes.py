from abc import ABC, abstractmethod

class Lutador(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100.0

    def soco(self, oponente):
        oponente.energia -= 5.5
    
    def __str__(self):
        return f"Nome: {self.nome} │ Energia: {self.energia}"
    
class Boxeador(Lutador):
    def golpe_cruzado(self, oponente):
        oponente.energia -= 10.2

    def ganho(self, oponente):
        oponente.energia -= 20.8

class Muay_Thai(Lutador):
    def chute_alto(self, oponente):
        oponente.energia -= 15.4

class JiuJitsu(Lutador):
    def chave_braco(self, oponente):
        oponente.energia -= 100.0

class MMA(Muay_Thai, JiuJitsu):
    def superman_punch(self, oponente):
        oponente.energia -= 53.2

if __name__ == "__main__":
    bronx = MMA("Charles do Bronx")
    mcg = MMA("Connor McGregor")

    print(f"{bronx}\n{mcg}")
    bronx.superman_punch(mcg)
    print(f"{bronx}\n{mcg}")
    mcg.chute_alto(bronx)
    print(f"{bronx}\n{mcg}")
    bronx.chave_braco(mcg)
    print(f"{bronx}\n{mcg}")