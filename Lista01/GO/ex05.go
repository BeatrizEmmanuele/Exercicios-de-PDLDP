package main

import "fmt"

// Definindo a interface Animal
type Animal interface {
	Som() string
}

// Função que recebe uma lista de animais e chama o método Som
func EmitirSons(animais []Animal) {
	for _, animal := range animais {
		fmt.Println(animal.Som())
	}
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

	animais := []Animal{cachorro, gato}
	EmitirSons(animais)
}
