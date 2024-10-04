class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __add__(self, outro):
        """Sobrecarga do operador + para somar os preços de dois produtos"""
        if isinstance(outro, Produto):
            return Produto("Combinação", self.preco + outro.preco)
        return NotImplemented

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

# Exemplo de uso
produto1 = Produto("Produto A", 10.0)
produto2 = Produto("Produto B", 20.0)
produto_comb = produto1 + produto2

print(produto1)         # Saída: Produto A: R$ 10.00
print(produto2)         # Saída: Produto B: R$ 20.00
print(produto_comb)     # Saída: Combinação: R$ 30.00
