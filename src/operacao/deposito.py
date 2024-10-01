from src.operacao.transacao import Transacao

class Deposito(Transacao):

    def registrar(self, conta, valor):
        conta._saldo += valor
