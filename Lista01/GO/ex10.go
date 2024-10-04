package main

import "fmt"

// Função para somar dois números
func somarDois(a int, b int) int {
    return a + b
}

// Função para somar três números
func somarTres(a int, b int, c int) int {
    return a + b + c
}

// Função principal para demonstrar a soma
func main() {
    resultado1 := somarDois(5, 10)
    resultado2 := somarTres(5, 10, 15)
    
    fmt.Println("Resultado da soma de dois números:", resultado1)
    fmt.Println("Resultado da soma de três números:", resultado2)
}
