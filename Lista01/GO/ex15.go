package main

import (
    "fmt"
)

// Definindo o tipo de erro personalizado
type SaldoInsuficienteError struct {
    Mensagem string
}

func (e *SaldoInsuficienteError) Error() string {
    return e.Mensagem
}

// Definindo a struct ContaBancaria
type ContaBancaria struct {
    Saldo float64
}

// Método para sacar valor da conta
func (c *ContaBancaria) Sacar(valor float64) error {
    if valor > c.Saldo {
        return &SaldoInsuficienteError{"Saldo insuficiente para o saque"}
    }
    c.Saldo -= valor
    return nil
}

// Função principal para demonstrar o uso
func main() {
    conta := &ContaBancaria{Saldo: 100.0}

    err := conta.Sacar(150.0)
    if err != nil {
        fmt.Println(err)
    }
}
