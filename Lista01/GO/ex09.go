package main

import "fmt"

// Definindo a interface Imprimivel
type Imprimivel interface {
    Imprimir()
}

// Implementando a interface em Relatorio
type Relatorio struct{}

func (r Relatorio) Imprimir() {
    fmt.Println("Imprimindo relatório...")
}

// Implementando a interface em Contrato
type Contrato struct{}

func (c Contrato) Imprimir() {
    fmt.Println("Imprimindo contrato...")
}

// Função principal para demonstrar a impressão
func main() {
    var relatorio Imprimivel = Relatorio{}
    var contrato Imprimivel = Contrato{}

    relatorio.Imprimir()
    contrato.Imprimir()
}
