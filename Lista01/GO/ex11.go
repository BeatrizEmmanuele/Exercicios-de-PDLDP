package main

import "fmt"

// Definindo a interface Funcionario (equivalente a uma classe abstrata)
type Funcionario interface {
	CalcularSalario() float64
}

// Definindo a struct FuncionarioHorista
type FuncionarioHorista struct {
	nome          string
	horasTrabalhadas int
	valorPorHora   float64
}

// Implementando o método CalcularSalario para FuncionarioHorista
func (f FuncionarioHorista) CalcularSalario() float64 {
	return float64(f.horasTrabalhadas) * f.valorPorHora
}

// Definindo a struct FuncionarioAssalariado
type FuncionarioAssalariado struct {
	nome     string
	salarioFixo float64
}

// Implementando o método CalcularSalario para FuncionarioAssalariado
func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.salarioFixo
}

// Função para exibir salários
func ExibirSalario(f Funcionario) {
	fmt.Printf("Salário: R$ %.2f\n", f.CalcularSalario())
}

func main() {
	// Criando um FuncionarioHorista
	horista := FuncionarioHorista{
		nome:            "Carlos",
		horasTrabalhadas: 160,
		valorPorHora:    50.0,
	}

	// Criando um FuncionarioAssalariado
	assalariado := FuncionarioAssalariado{
		nome:        "Ana",
		salarioFixo: 7000.0,
	}

	// Exibindo os salários
	fmt.Printf("Funcionario: %s\n", horista.nome)
	ExibirSalario(horista)

	fmt.Printf("Funcionario: %s\n", assalariado.nome)
	ExibirSalario(assalariado)
}
