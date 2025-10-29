class Pessoa:

    def __init__(self, nome):
        self.__nome = nome
    
    def __str__(self):
        return f"Nome: {self.__nome}"
    
class Aluno(Pessoa):

    def __init__(self, nome, ra, tamanho_camisa):
        super().__init__(nome)
        self.__RA = ra
        self.tamanho_camisa = tamanho_camisa
    
    def get_RA(self):
        return self.__RA
    
class Juiz(Pessoa):

    def __init__(self, nome, email):
        super().__init__(nome)
        self.__email = email
    
    def get_email(self):
        return self.__email
    
    def __str__(self):
        txt = super().__str__()
        txt += f"Email: {self.__email}"
        return txt
    
class Time:

    def __init__(self, nome, alunos=None):
        self.__nome = nome
        self.__alunos = alunos if alunos is not None else []

    def get_nome(self):
        return self.__nome

    def get_alunos(self):
        return self.__alunos

    def add_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def get_alunos(self):
        return self.__alunos

    def __str__(self):
        txt = f"Time: {self.__nome}\n"
        txt += "Alunos:\n"
        for a in self.__alunos:
            txt += f" - {a}\n"
        return txt

class Maratona:
    def __init__(self, ano: int):
        self._ano = ano
        self._times = []
        self.juiz = None 

        def add_time(self, time: Time):
            self.__times.append(time)

        def get_ano(self):
            return self.__ano
        
        def __str__(self):

            txt = f"Maratona do ano {self._-ano}\n"
            txt += f"Juiz: {self.juiz}\n"
            txt += "Times:\n"
            for t in self.__times:
                txt += f" - {t}\n"
            return txt

    gabriel = Aluno("Gabriel Conrado", 1, "M")
    diogo = Aluno("Diogo Dantas", 2, "M")
    bianca = Aluno("Bianca Franco", 3, "M")

    time1 = Time("SI the best", [gabriel, diogo, bianca])
    print(time1)