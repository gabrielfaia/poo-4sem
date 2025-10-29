from jogador import *
from armas import *
import random

def ataque(atacante: Jogador, recebedor: Jogador):
    print(f"{atacante.nome} ira atacar")
    sorteio = random.randint(1,2)
    if sorteio == 1:
        print(f"Escolha uma das armas do {atacante.nome} para atirar")
        for indice, arma in enumerate(atacante.armas):
            print(f"[{indice}] - {arma}")
        escolha = int(input("Digite o numero da arma: "))
        while escolha > (len(atacante.armas)-1) or escolha < 0:
            escolha = int(input("Digite o numero da arma: "))
        arma_escolhida = atacante.armas[escolha]
        atacante.atirar(arma_escolhida,recebedor)
        try:
            atacante.atirar(arma_escolhida,recebedor)
        except:
            op = input("Recarregar arma? (S/N)")
            while op.upper() not in ("S", "N"):
                op = input("Recarregar arma? (S/N)")
            if op == "S":
                arma_escolhida.recarregar()
    else:
        escolha = input("Escolha agredir com 1-Arma ou com 2-Golpe? [1-2]:")
        while escolha != "1" and escolha != "2":
            escolha = input("Escolha agredir com 1-Arma ou com 2-Golpe? [1-2]:")
        if escolha == "1":
            for indice, arma in enumerate(atacante.armas):
                print(f"[{indice}] - {arma}")
            escolha = int(input("Digite o numero da arma: "))
            while escolha > (len(atacante.armas)-1) or escolha < 0:
                escolha = int(input("Digite o numero da arma: "))
            arma_escolhida = atacante.armas[escolha]
            atacante.bater(recebedor,a=arma_escolhida)
        else:
            golpes = [Soco(), Chute()]
            g = int(input("0-Soco e 1-Chute:"))
            while g not in (0,1):
                g = int(input("0-Soco e 1-Chute:"))
            golpe = golpes[g]
            atacante.bater(recebedor, golpe)

if __name__ == "__main__":
    player1 = Jogador(input("Digite o nome do player 1:"))
    player2 = Jogador(input("Digite o nome do player 2:"))

    player1.armas = [Revolver(), Faca(), Soco_Ingles()]
    player2.armas = [LancaChamas(), Revolver()]

    print("Inicio do Jogo")
    print("=======================")
    print(f"{player1}\n{player2}")

    while player1.energia > 0 and player2.energia > 0:
        sorteio = random.randint(1,2)
        if sorteio == 1:
            ataque(player1, player2)
        else:
            ataque(player2, player1)
        
        print(f"{player1}\n{player2}")

    print("Fim do jogo")
    print("=========================")


        