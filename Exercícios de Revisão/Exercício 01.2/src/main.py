from quiz import *

if __name__ == "__main__":
	poo = Quiz("POO", "Joao Maria Jose", 20, 1)
	ihc = Quiz2A("IHC", "Pedro Paulo Francisco", 20, 10)
	redes = Quiz3A("Redes", "Teodoro Sampaio", 35, 9)
	
	print(poo)
	print(ihc)
	print(redes)
	
	quizes = [poo, ihc, redes]
	
	acertos = []
	erros = []
	pontos = []
	for i, q in enumerate(quizes):
		acertos.append(q.get_acertos())
		erros.append(q.get_erros())
		pontos.append(q.calcular_pontos())
	
	print(f"A maior quantidade de acertos foi {max(acertos)}")
	print(f"A maior quantidade de erros foi {max(erros)}")
	print(f"A maior quantidade de pontos foi {max(pontos)}")