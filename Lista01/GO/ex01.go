package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
    Marca  string
    Modelo string
    Ano    int
}

// Função para exibir os detalhes do carro
func (c Carro) ExibirDetalhes() {
    fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func main() {
    // Instanciando três carros
    carro1 := Carro{"Fiat", "Pulse", 2022}
    carro2 := Carro{"Chevrolet", "Onix", 2021}
    carro3 := Carro{"Volkswagen", "Polo", 2020}

    // Exibindo os detalhes de cada carro
    carro1.ExibirDetalhes()
    carro2.ExibirDetalhes()
    carro3.ExibirDetalhes()
}
