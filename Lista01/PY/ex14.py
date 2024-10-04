class Configuracao:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            # Inicialize qualquer configuração aqui, se necessário
        return cls._instancia

    def __init__(self, valor=None):
        if not hasattr(self, '_inicializado'):
            # Inicialize a configuração aqui, se necessário
            self.valor = valor
            self._inicializado = True

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

# Exemplo de uso
def main():
    config1 = Configuracao("Configuração 1")
    print("Valor de config1:", config1.get_valor())  # Saída: Configuração 1

    config2 = Configuracao("Configuração 2")
    print("Valor de config2:", config2.get_valor())  # Saída: Configuração 1 (não mudou, pois é a mesma instância)

    # Verificar se config1 e config2 são a mesma instância
    print("config1 é a mesma instância que config2?", config1 is config2)  # Saída: True

if __name__ == "__main__":
    main()
