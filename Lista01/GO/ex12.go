package main

import "fmt"

// Definindo a estrutura Produto
type Produto struct {
    Nome  string
    Preco float64
}

// Função para somar o preço de dois produtos
func somarProdutos(p1, p2 Produto) Produto {
    return Produto{
        Nome:  "Combinação",
        Preco: p1.Preco + p2.Preco,
    }
}

// Função principal para demonstrar a soma
func main() {
    produto1 := Produto{"Produto A", 10.0}
    produto2 := Produto{"Produto B", 20.0}
    produtoComb := somarProdutos(produto1, produto2)

    fmt.Printf("%s: R$ %.2f\n", produto1.Nome, produto1.Preco)
    fmt.Printf("%s: R$ %.2f\n", produto2.Nome, produto2.Preco)
    fmt.Printf("%s: R$ %.2f\n", produtoComb.Nome, produtoComb.Preco)
}
