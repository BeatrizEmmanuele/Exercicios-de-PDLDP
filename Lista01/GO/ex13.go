package main

import (
    "fmt"
)

// Função para calcular o fatorial
func fatorial(n int) int {
    if n < 0 {
        panic("O fatorial não está definido para números negativos.")
    }
    resultado := 1
    for i := 2; i <= n; i++ {
        resultado *= i
    }
    return resultado
}

// Função principal para demonstrar o cálculo do fatorial
func main() {
    fmt.Println("Fatorial de 5:", fatorial(5))  // Saída: 120
    fmt.Println("Fatorial de 0:", fatorial(0))  // Saída: 1
}
