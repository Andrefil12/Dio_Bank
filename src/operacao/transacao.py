from abc import ABC, abstractmethod


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta, valor):
        pass