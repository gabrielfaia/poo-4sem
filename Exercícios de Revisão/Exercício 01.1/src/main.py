from quiz import *

if __name__ == "__main__":
	poo = Quiz("POO", "Joao Maria Jose", 20, 1)
	ihc = Quiz("IHC", "Pedro Paulo Francisco", 20, 10)
	
	print(poo)
	print(ihc)
	
	if poo.get_acertos() > ihc.get_acertos():
		print(f"{poo.aluno} teve mais acertos do que {ihc.aluno}")
	elif poo.get_acertos() < ihc.get_acertos():
		print(f"{ihc.aluno} teve mais acertos do que {poo.aluno}")
	else:
		print(f"{ihc.aluno} empatou com {poo.aluno} em quantidade de acertos")
		
	if poo.calcular_pontos() > ihc.calcular_pontos():
		print(f"{poo.aluno} teve mais pontos do que {ihc.aluno}")
	elif poo.calcular_pontos() < ihc.calcular_pontos():
		print(f"{ihc.aluno} teve mais pontos do que {poo.aluno}")
	else:
		print(f"{ihc.aluno} empatou com {poo.aluno} em quantidade de pontos")