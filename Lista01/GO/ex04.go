package main

import "fmt"

// Definindo a interface Animal (substituindo herança)
type Animal interface {
	Som() string
}

// Definindo a struct Cachorro
type Cachorro struct {
	nome string
}

// Implementando o método Som para Cachorro
func (c Cachorro) Som() string {
	return "Au Au!"
}

// Definindo a struct Gato
type Gato struct {
	nome string
}

// Implementando o método Som para Gato
func (g Gato) Som() string {
	return "Miau!"
}

func main() {
	cachorro := Cachorro{nome: "Rex"}
	gato := Gato{nome: "Felix"}

	fmt.Printf("%s faz: %s\n", cachorro.nome, cachorro.Som())
	fmt.Printf("%s faz: %s\n", gato.nome, gato.Som())
}
