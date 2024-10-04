def main():

    vetorA = []
    vetorB = []
    vetorC = []

    for i in range(10):
        vetorA.append(int(input("Digite o elemento %d do vetor A: " %i)))
        vetorB.append(int(input("Digite o elemento %d do vetor B: " %i)))

    for i in range(10):
        vetorC.append(vetorA[i] + vetorB[i])

    print("Vetor C")
    for i in range(10):
        print(vetorA[i])
        print(vetorB[i])
        print(vetorC[i])


if __name__ == "__main__":
    main()