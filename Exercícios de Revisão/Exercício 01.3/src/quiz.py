from typing import List

class Quiz:
    def __init__(self, ac: str, err: str):
        self.__acertos = ac
        self.__erros = err

    def get_erros(self):
        return self.__erros 

    def get_acertos(self):
        return self.__acertos 
    
    def calcular_pontos(self):
        return self.__acertos - self.__erros 
    
    def __str__(self):
        txt = ""
        txt += f"Acertos = {self.__acertos} │ Erros = {self.__erros}\n"
        txt += f"Total Pontos = {self.calcular_pontos()}"
        return txt

class Quiz2A(Quiz):
    def __init__(self, ac: str, err: str):
        super().__init__(ac, err)

    def calcular_pontos(self):
        return self.get_acertos() - (4 * self.get_erros())

class Quiz3A(Quiz):
    def __init__(self, ac: str, err: str):
        super().__init__(ac, err)

    def calcular_pontos(self):
        return self.get_acertos() - (2 * self.get_erros())

class Aluno:
    def __init__(self, ma: str, n: str, qs: List[Quiz]):
        self.__matricula = ma
        self.__nome = n
        self.__quizes = qs

    def __str__(self):
        txt = f"Aluno: {self.__nome} (RA: {self.__matricula})\n\n"
        for q in self.__quizes:
            txt += f"{q}"
        return txt

class Disciplina:
    def __init__(self, n: str, p: str, a: str, s: str):
        self.__nome = n
        self.__professor = p
        self.__ano = a
        self.__semestre = s
        self.__alunos = []

    def add_aluno(self, a: Aluno):
        self.__alunos.append(a)

    def __str__(self):
        txt = f"{self.__nome} - Prof: {self.__professor}\n"
        txt += f"Ano/Semestre: {self.__ano}/{self.__semestre}\n\n"
        for a in self.__alunos:
            txt += f"{a}"
        return txt

if __name__ == "__main__":
    d = Quiz(5, 3)
    d2a = Quiz2A(5, 1)
    d3a = Quiz3A(5, 1)

    aluno = Aluno(445151, "Gabriel", [d])
    poo = Disciplina("POO", "Thiago Ferrauche", "2025", "4° Semestre")
    poo.add_aluno(aluno)
    print(poo)