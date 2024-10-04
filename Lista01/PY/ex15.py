class SaldoInsuficienteException(Exception):
    """Exceção personalizada para saldo insuficiente."""
    def __init__(self, mensagem="Saldo insuficiente para o saque"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException()
        self.saldo -= valor

# Exemplo de uso
def main():
    conta = ContaBancaria(100.0)
    
    try:
        conta.sacar(150.0)
    except SaldoInsuficienteException as e:
        print(e)

if __name__ == "__main__":
    main()
