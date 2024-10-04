class Calculadora:
    def somar(self, *args):
        return sum(args)

# Exemplo de uso
calc = Calculadora()

resultado1 = calc.somar(5, 10)
resultado2 = calc.somar(5, 10, 15)

print("Resultado da soma de dois números:", resultado1)
print("Resultado da soma de três números:", resultado2)
