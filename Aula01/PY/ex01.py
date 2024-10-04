def somaDeVetor(x,y): 
    vetor = [0] * 8
    soma = vetor[x] + vetor[y]
    return soma


def main():

    vetor = [0] * 8

    for i in range(8):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))

    
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    
    print("A soma dos valores nas posições X e Y é {}." .format(somaDeVetor))

if __name__ == "__main__":
    main()