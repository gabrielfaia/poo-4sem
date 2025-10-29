from classes import *
import random

def golpear(batedor : Lutador, apanhador : Lutador):
    golpes = ['soco', 'cruzado', 'gancho', 'chute_alto', 'chave_braco', 'superman_punch']
    print(f"==== {batedor.nome} irá golpear {apanhador.nome}, escolha o golpe ====")
    print(golpes)
    golpe = input('Digite um dos golpes cima: ')
    while golpe not in golpes:
        print(golpes)
        golpe = input('Digite um dos golpes cima: ')

    method = getattr(batedor, golpe)
    method(apanhador)

if __name__ == "__main__":
    nome1 = input("Digite o nome do Lutador 1: ")
    nome2 = input("Digite o nome do Lutador 2: ")

    lutador1 = MMA(nome1)
    lutador2 = MMA(nome2)

    while lutador1.energia > 0 and lutador2.energia > 0:
        numero = random.randint(1,2)
        if numero == 1:
            golpear(lutador1, lutador2)
        else:
            golpear(lutador2, lutador1)
        
        print("==== Status da Luta ====")
        print(lutador1)
        print(lutador2)

    print("=== Fim da Luta ====")
    if lutador1.energia <= 0:
        print(f"{lutador2.nome} venceu {lutador1.nome}")
    else:
        print(f"{lutador1.nome} venceu {lutador2.nome}")