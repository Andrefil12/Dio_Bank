from src.conta.conta import Conta
from src.extrato.historico import Historico
from src.operacao.deposito import Deposito
from src.operacao.saque import Saque
from src.pessoa.cliente import Cliente


class ContaCorrente(Conta):

    def __init__(self, saldo, numero, agencia, cliente, historico, limite = 1000, saques = 3):
        self._limite = limite
        self._saques = saques
        super().__init__(saldo, numero, agencia, cliente, historico)


    def saldo(self):
        return self._saldo + self._limite


    def nova_conta(self, cliente, numero):
        cliente.adicionar_conta(self)

    def sacar(self, valor):
        if(valor > 0 and valor < self._saques):
            deposito = Deposito()
            deposito.registrar(self, valor)

    def depositar(self, valor):
        if(valor > 0):
            Saque().registrar(self, valor)


if __name__ == "__main__":
    conta = ContaCorrente(1000,
                          1,
                          "0001",
                          Cliente("000.162.213-90", "José Ferreira da Silva","23/10/1976", "Rua José Rufino, n° 25", []),
                          Historico())
    conta.sacar(200)
    conta.depositar(200)