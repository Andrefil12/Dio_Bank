from src.operacao.transacao import Transacao

class Saque(Transacao):

    def registrar(self, conta, valor):
        conta._saldo -= valor
