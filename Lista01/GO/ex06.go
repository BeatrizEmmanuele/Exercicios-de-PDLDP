package main

import "fmt"

// Definindo a struct Motor
type Motor struct {
	potencia int
}

// Função associada ao Motor para exibir a potência
func (m Motor) ExibirPotencia() {
	fmt.Printf("Potência do motor: %d HP\n", m.potencia)
}

// Definindo a struct Carro que possui um Motor
type Carro struct {
	marca  string
	modelo string
	motor  Motor
}

// Função para exibir detalhes do carro e do motor
func (c Carro) ExibirDetalhes() {
	fmt.Printf("Carro: %s %s\n", c.marca, c.modelo)
	c.motor.ExibirPotencia()
}

func main() {
	motor := Motor{potencia: 150}
	carro := Carro{marca: "Fiat", modelo: "Pulse", motor: motor}

	carro.ExibirDetalhes()
}
