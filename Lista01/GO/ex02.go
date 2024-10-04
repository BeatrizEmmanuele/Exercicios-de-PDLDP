package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
    Marca     string
    Modelo    string
    Ano       int
    Velocidade int
}

// Método para acelerar o carro
func (c *Carro) Acelerar(incremento int) {
    c.Velocidade += incremento
    fmt.Printf("O carro acelerou. Velocidade atual: %d km/h\n", c.Velocidade)
}

// Método para frear o carro
func (c *Carro) Frear(decremento int) {
    c.Velocidade -= decremento
    if c.Velocidade < 0 {
        c.Velocidade = 0
    }
    fmt.Printf("O carro freou. Velocidade atual: %d km/h\n", c.Velocidade)
}

// Método para exibir a velocidade atual
func (c Carro) ExibirVelocidade() {
    fmt.Printf("A velocidade atual é: %d km/h\n", c.Velocidade)
}

func main() {
    carro := Carro{Marca: "Fiat", Modelo: "Pulse", Ano: 2022, Velocidade: 0}

    carro.Acelerar(30)
    carro.ExibirVelocidade()

    carro.Frear(15)
    carro.ExibirVelocidade()

    carro.Frear(20)
    carro.ExibirVelocidade()
}
