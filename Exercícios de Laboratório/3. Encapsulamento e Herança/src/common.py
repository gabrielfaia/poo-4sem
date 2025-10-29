class Pessoa:
    # Atributos Privados (não acessados fora da classe, apenas como anotação)
    __nome : str
    __RG : str
    __CPF : str
    
    # Construtor da classe (inicializa os atributos da Pessoa)
    def __init__(self, nome, RG, CPF):
        self.__nome = nome
        self.__RG = RG
        self.__CPF = CPF

    def __str__(self):
        info = (f'Nome: {self.__nome}\n'
               f'RG: {self.__RG}\n'
               f'CPF: {self.__CPF}\n')
        return info
    
    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}')"
    
class Eleitor(Pessoa):
    __titulo : int
    secao : int
    zona : int

    # Construtor da classe, aproveitando o construtor da classe Pessoa (super)
    # super() = Pessoa é a classe mãe, enquanto Eleitor a filha
    def __init__(self, nome, RG, CPF, titulo, secao, zona):
        super().__init__(nome, RG, CPF)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona

    def __str__(self):
        info = super().__str__()
        info += (f'Titulo: {self.__titulo}\n'
                 f'Seção: {self.secao}\n'
                 f'Zona: {self.zona}\n')
        return info

    def __repr__(self):
        return f"Eleitor({super().__repr__()}, titulo='{self.__titulo}', secao='{self.secao}', zona='{self.zona}')"

    def get_titulo(self):
        return self.__titulo
    
class Candidato(Pessoa):

    def __init__(self, nome, RG, CPF, numero):
        super().__init__(nome, RG, CPF)
        self._numero = numero

    def __str__(self):
        info = super().__str__()
        info += f'Número: {self.__numero}\n'
        return info
    
    def __repr__(self):
        return f"Candidato({super().__repr__()}, numero='{self.__numero}')"

    def get_numero(self):
        return self.__numero
    
    