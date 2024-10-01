from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @abstractmethod
    def saldo(self):
        pass

    @abstractmethod
    def nova_conta(self, cliente, numero):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

