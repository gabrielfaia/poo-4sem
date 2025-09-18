class Carro:
    marca: str
    motor: bool
    odometro: int
    modelo_: str

    # os dois selfs são valores que serão passados para o Construtor.
    def __init__(self, model, mark, tanq, consu, mot=False, odome=0):
        self.modelo = model
        self.marca = mark
        self.tanque = tanq
        self.consumo = consu
        self.motor = mot
        self.odometro = odome

    def ligar(self):
         self.motor = True
            
    def desligar(self):
        self.motor = False

    def acelerar(self, velocidade: float, tempo: float):
        if self.tanque == 0:
            raise Exception('O tanque esta vazio!')
        if self.motor:
            distancia = velocidade * tempo
            litros = distancia / self.consumo
            if self.tanque - litros > 0:
                self.odometro += distancia
                self.tanque -= litros
            else: 
                self.tanque = 0
        else:
            raise Exception('Ligue o motor do carro antes de acelerar.')

    def __str__(self):
        txt = f"Modelo {self.modelo}\n"
        txt = f"Marca {self.marca}\n"
        txt = f"Motor {self.motor}\n"     
        txt += f"Odometro {self.odometro}"
        return txt