class Matematica:
    
    @staticmethod
    def fatorial(n: int) -> int:
        """Calcula o fatorial de um número n."""
        if n < 0:
            raise ValueError("O fatorial não está definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso
def main():
    print("Fatorial de 5:", Matematica.fatorial(5))  # Saída: 120
    print("Fatorial de 0:", Matematica.fatorial(0))  # Saída: 1

if __name__ == "__main__":
    main()
