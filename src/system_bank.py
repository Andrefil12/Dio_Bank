class Bank:

    limite_saque = 500
    extrato_conta = {}
    quantidade_saque = 0
    saldo = 1000


    def deposito(self, deposito):
        if(deposito > 0):
            self.saldo += deposito
            self.extrato_conta.setdefault("DP", deposito)
            return "Deposito realizado com sucesso"

        else:
            "O valor informado não pode ser depositado!"

    def saque(self, saque):
        if(saque <= 500 and self.quantidade_saque < 3):
            self.saldo -= saque
            self.quantidade_saque += 1
            self.extrato_conta.setdefault("SQ", saque)
            return "Saque realizado com sucesso!"
        else:
            "Está operação não pode ser realizada"


    def extrato(self):
        for chave, valor in self.extrato_conta.items():
            print(f"A transação realizada foi: {chave} no valor de R$: {valor}")


if __name__ == '__main__':
    bank = Bank()
    print(bank.deposito(200))
    print(bank.saque(350))
    print(bank.extrato())