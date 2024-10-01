from src.conta.conta_corrente import ContaCorrente
from src.pessoa.pessoafisica import PessoaFisica


class Cliente(PessoaFisica):

    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        self._endereco = endereco
        self._contas = contas
        self.saque = True
        self.deposito = False
        super().__init__(cpf, nome, data_nascimento)

    def realizar_transacao(self, conta, transacao):
        if(self.saque):
            conta.sacar(200)
        else:
            conta.depositar(200)

    def adicionar_conta(self, conta):
        self._contas = conta


if __name__ == "__main__":
    cliente = Cliente("000.162.213-90", "José Ferreira da Silva","23/10/1976", "Rua José Rufino, n° 25", [])
