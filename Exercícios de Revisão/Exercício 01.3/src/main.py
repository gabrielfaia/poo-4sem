from quiz import *

if __name__ == "__main__":
	poo = Disciplina("Programacao Orientada a Objetos", "Thiago Ferauche", 2025, 2)

	q1 = Quiz(20, 1)
	q2 = Quiz2A(20, 10)
	q3 = Quiz3A(35, 9)
	pedro = Aluno(123, "Pedro Paulo Francisco",[q1, q2, q3])
	
	q4 = Quiz2A(20, 1)
	q5 = Quiz3A(20, 9)
	joao = Aluno(321, "Joao Maria Jose", [q4, q3])
	
	poo.add_aluno(pedro)
	poo.add_aluno(joao)
	
	print(poo)