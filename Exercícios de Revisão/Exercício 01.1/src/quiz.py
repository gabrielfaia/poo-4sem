class Quiz:
    def __init__(self, d: str, a: str, ac: str, err: str):
        self.disciplina = d
        self.aluno = a
        self.__acertos = ac
        self.__erros = err

    def get_erros(self):
        return self.__erros 

    def get_acertos(self):
        return self.__acertos 
    
    def calcular_pontos(self):
        return self.__acertos - self.__erros 
    
    def __str__(self):
        txt = f"{self.disciplina} aluno {self.aluno}\n"
        txt += f"Acertos = {self.__acertos} │ Erros = {self.__erros}\n"
        txt += f"Total Pontos = {self.calcular_pontos()}"
        return txt

if __name__ == "__main__":
    d = Quiz("Circuitos", "Rodney Silveira", 5, 3)
    print(d) 