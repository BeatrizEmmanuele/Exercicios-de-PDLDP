# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # Atributo protegido

    # Método para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")

    # Método para sacar dinheiro
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    # Método para exibir o saldo atual
    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")

# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria("Beatriz", 1000)

# Exibindo o saldo inicial
conta.exibir_saldo()

# Realizando depósitos
conta.depositar(float(input("Digite o valor a ser depositado:" )))

# Realizando saques
conta.sacar(float(input("Digite o valor a sacar:")))

# Exibindo o saldo final
conta.exibir_saldo()
