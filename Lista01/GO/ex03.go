package main

import "fmt"

// Definindo a struct ContaBancaria
type ContaBancaria struct {
	titular string
	saldo   float64 // saldo encapsulado
}

// Função para depositar na conta (método)
func (c *ContaBancaria) Depositar(valor float64) {
	c.saldo += valor
	fmt.Printf("Depósito de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
}

// Função para sacar da conta (método)
func (c *ContaBancaria) Sacar(valor float64) {
	if valor > c.saldo {
		fmt.Println("Saldo insuficiente!")
	} else {
		c.saldo -= valor
		fmt.Printf("Saque de R$ %.2f realizado. Saldo atual: R$ %.2f\n", valor, c.saldo)
	}
}

// Função para exibir saldo (getter)
func (c *ContaBancaria) ExibirSaldo() {
	fmt.Printf("Saldo atual: R$ %.2f\n", c.saldo)
}

func main() {
	conta := ContaBancaria{titular: "Beatriz", saldo: 0}
	conta.Depositar(100.0)
	conta.Sacar(30.0)
	conta.ExibirSaldo()
	conta.Sacar(80.0)
}
