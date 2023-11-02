class ContaBancaria:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.saldo = 0
        self.status = False
        self.limite = 10

    def depositar(self, valor):
        if self.status == True:
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
            else:
                print("O valor do depósito deve ser maior que zero.")
        else:
            print("Não é possível realizar depósitos em uma conta inativa.")

    def sacar(self, valor):
        if self.status == True:
            if valor > 0:
                if self.saldo + self.limite >= valor:
                    self.saldo -= valor
                    print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("O valor do saque deve ser maior que zero.")
        else:
            print("Não é possível realizar saques em uma conta inativa.")

    def ativar_conta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada com sucesso.")

    def verificar_saldo(self):
        if self.status == True:
            print(f"Saldo atual da conta de {self.nome}: R${self.saldo}")
        else:
            print("A conta está inativa. Não é possível verificar o saldo.")

# Exemplo de uso da classe ContaBancaria
conta1 = ContaBancaria(123456, "João", "Corrente")
conta1.verificar_saldo()
conta1.depositar(500)

conta1.ativar_conta()
conta1.depositar(800)
conta1.sacar(1000)
conta1.verificar_saldo()
