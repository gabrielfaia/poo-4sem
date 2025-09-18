from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

## __str__() = imprime o objeto
## No fim da classe criar um trecho de código:
## 

class ContaInvestimento(ABC):
    def __init__(self, v: float):
        self._saldo = v

    def depositar(self, v: float):
        self._saldo += v

    def sacar(self, v: float):
        if v > self._saldo:
            raise Exception('Saldo insuficiente')
        
    def get_saldo(self):
        return self._saldo 

    def __str__(self):
        txt = f"Saldo: R${self._saldo:.2f}"
        return txt
    
    @abstractmethod
    def atualizar(self):
        pass

class RendaFixa(ContaInvestimento):
    def __init__(self, rendimento: float, prazo_saque: str, valor: float):
        super().__init__()
        self._rendimento = rendimento
        self._prazo_saque = datetime.strptime(prazo_saque, "%d/%m/%Y")
        self.depositar(valor)

    def sacar(self, v: float):
        data_atual = datetime.now
        if data_atual >= self._prazo_saque:
            raise Exception("Saque nao permitido antes do prazo!")
        super().sacar(v)

    def __str__(self):
        txt = super().__str__()
        txt += f"\nRendimento: {self._rendimento:.2f}% Prazo {self._prazo_saque}"
        return txt
    
    def atualizar(self):
        renda = self.get_saldo() * self._rendimento
        super().depositar(renda)

class ContaPoupanca(ContaInvestimento):
    def __init__(self, taxa_mensal: float):
        super().__init__()
        self._taxa_mensal = taxa_mensal
        self._depositos = List[float] = []

    def depositar(self, v: float):
        super().depositar(v)
        self._depositos.append(v)

    def sacar(self, v):
        super().sacar(v)
        
        if len(self._depositos) > 0:
            del self.depositos[0]

        # Utilizar self._depositos.del significa remover o Primeiro Valor
        # Utilizar self._depositos.del significa remover o Último valor
    
    def atualizar(self):
        total = sum(self.depositos)
        rendimento = total * (self._taxa_mensal / 100)
        self._saldo += rendimento

    def __str__(self):
        txt = super().__str__()
        txt += f"\nTaxa: {self.taxa_mensal} │ Depositos: {self._depositos}"
        return txt

class Criptomoeda(ContaInvestimento):
    def __init__(self, cotacao: float, quantidade: float):
        self._cotacao = cotacao
        self._quantidade = 0.0

    def atualizar(self, quantidade: float):
        self._quantidade += quantidade
        self.atualizar()

    def comprar(self, quantidade: float):
        self.quantidade += quantidade
        self.atualizar()

    def vender(self, quantidade: float):
        self.quantidade -= quantidade
        self.atualizar()

    def __str__(self):
        txt = super().__str__()
        txt += f"\nCotacao: R${self._cotacao} │ Quantidade: {self._quantidade}"
        return txt