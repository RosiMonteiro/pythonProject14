class ContaBancaria:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = 0.0

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def levantar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def verificarSaldo(self):
        print("Saldo da conta de {}: {:.2f}".format(self.__nome, self.__saldo))

def main():
    contas = []

    while True:
        print("\n1 - Criar conta bancária")
        print("2 - Depositar em uma conta bancária")
        print("3 - Levantar em uma conta bancária")
        print("4 - Verificar saldo de uma conta bancária")
        print("5 - Sair")
        opcao = int(input("Digite o número da opção: "))

        if opcao == 1:
            numero = int(input("Digite o número da conta: "))
            nome = input("Digite o nome do titular: ")
            contas.append(ContaBancaria(numero, nome))
        elif opcao == 2:
            conta = int(input("Digite o índice da conta bancária: "))
            valor = float(input("Digite o valor do depósito: "))
            contas[conta].depositar(valor)
        elif opcao == 3:
            conta = int(input("Digite o índice da conta bancária: "))
            valor = float(input("Digite o valor do levantamento: "))
            contas[conta].levantar(valor)
        elif opcao == 4:
            conta = int(input("Digite o índice da conta bancária: "))
            contas[conta].verificarSaldo()
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
