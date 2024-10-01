# class Bank:
#
#     def __init__(self):
#         self.extrato_conta = {}
#         self.quantidade_saque = 3
#         self.saldo = 0
#         self.agencia = "0001"
#         self.conta = 0
#
#
#     def deposito(self, deposito):
#         if(deposito > 0):
#             self.saldo += deposito
#             self.extrato_conta.setdefault("Deposito", deposito)
#             return "Deposito realizado com sucesso"
#
#         else:
#             "O valor informado não pode ser depositado!"
#
#     def saque(self, saque):
#         if(saque <= 500 and self.quantidade_saque < 3):
#             self.saldo -= saque
#             self.quantidade_saque += 1
#             self.extrato_conta.setdefault("Saque", saque)
#             return "Saque realizado com sucesso!"
#         else:
#             "Está operação não pode ser realizada"
#
#
#     def extrato(self):
#         for chave, valor in self.extrato_conta.items():
#             print(f"A transação realizada foi: {chave} no valor de R$: {valor} seu saldo é de: {self.saldo}")
#
#     def novo_usuario(self, *args):
#         arg = args[0]
#         novo_usuario_banco = {arg[2]: [value for value in arg if value != arg[2]]}
#         self.conta_bancaria(novo_usuario_banco.keys())
#
#
#     def conta_bancaria(self, relacionamento):
#         nova_conta = [self.conta, self.agencia, relacionamento]
#         self.conta += 1
#
#
# # if __name__ == '__main__':
# #
# #     nome_usuario = input("Digite seu nome: ")
# #     data_nascimento = input("Qual sua data de nascimento: ")
# #     cpf_usuario = input("Qual seu cpf: ")
# #     logradouro = input("Qual seu endereço: ")
# #     bairro = input("Qual seu bairro: ")
# #     cidade_estado = input("Qual sua cidade: ")
# #
# #     bank = Bank()
# #     dados_usuario = [nome_usuario, data_nascimento, cpf_usuario, logradouro, bairro, cidade_estado]
# #     bank.novo_usuario(dados_usuario)
# #     print(bank.deposito(200))
# #     print(bank.saque(350))
# #     print(bank.extrato())