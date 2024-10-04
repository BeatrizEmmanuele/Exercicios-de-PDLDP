package main

import (
	"fmt"
	"sync"
)

// Definindo a struct Configuracao (a classe Singleton)
type Configuracao struct {
	Nome string
}

var instancia *Configuracao
var once sync.Once // Usado para garantir que a instância seja criada apenas uma vez

// Função para obter a instância da configuração (Singleton)
func GetInstancia(nome string) *Configuracao {
	once.Do(func() { // Executa apenas uma vez
		instancia = &Configuracao{Nome: nome}
	})
	return instancia
}

func main() {
	// Tentando criar duas instâncias
	config1 := GetInstancia("Configuração 1")
	config2 := GetInstancia("Configuração 2")

	// Exibindo os nomes das instâncias
	fmt.Println(config1.Nome) // Saída: Configuração 1
	fmt.Println(config2.Nome) // Saída: Configuração 1 (mesma instância)

	// Verificando se ambas apontam para a mesma instância
	if config1 == config2 {
		fmt.Println("Ambas as variáveis apontam para a mesma instância.")
	} else {
		fmt.Println("As variáveis apontam para instâncias diferentes.")
	}
}
