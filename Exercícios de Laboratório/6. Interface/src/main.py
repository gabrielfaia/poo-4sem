from typing import List
from FPS import *

def exibir_jogadores(jogadores : List[Jogador]):
	for j in jogadores:
		print(j)

if __name__ == "__main__":
	jogador1 = Jogador("Jogador de CS")
	jogador2 = Jogador("Jogador de VALORANT")
	lista_jogadores = [jogador1, jogador2]
	
	print("=== Situação Inicial ===")
	exibir_jogadores(lista_jogadores)
	
	print("=== Jogador 1 bateu no jogador 2")
	jogador1.bater(jogador2)
	exibir_jogadores(lista_jogadores)
	
	print("=== jogador 2 pegou um revolver e atirou no jogador 1  ===")
	r = Revolver()
	jogador2.arma = r
	jogador2.disparar(jogador1)
	exibir_jogadores(lista_jogadores)
	
	print("=== jogador 1 pegou uma bazuca e atirou no jogador 2 ===")
	bazuka = Bazuca()
	jogador1.arma = bazuka
	jogador1.arma.atirar(jogador2)
	exibir_jogadores(lista_jogadores)