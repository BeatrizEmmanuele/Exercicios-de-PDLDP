import random

def gerarCartela():
    nums = set()
    cartela = []
    for i in range(5):
        nums = random.randint(0,99)
        while numero in nums:
            numero = random.randint(0,99)
        nums.add(numero)
        cartela.append(numero)
    return cartela

def main():
    cartela = gerarCartela()
    print("Cartela de Bingo:")
    for linha in cartela:
        print(linha)

if __name__ == "__main__":
    main()