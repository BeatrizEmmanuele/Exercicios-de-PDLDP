package main

import "fmt"

// Definindo a struct Empregado
type Empregado struct {
	nome   string
	cargo  string
	salario float64
}

// Definindo a struct Empresa que agrega Empregados
type Empresa struct {
	nome      string
	empregados []Empregado
}

// Método para adicionar um empregado à empresa
func (e *Empresa) AdicionarEmpregado(empregado Empregado) {
	e.empregados = append(e.empregados, empregado)
}

// Método para exibir detalhes da empresa e seus empregados
func (e Empresa) ExibirEmpregados() {
	fmt.Printf("Empresa: %s\n", e.nome)
	for _, emp := range e.empregados {
		fmt.Printf("Empregado: %s, Cargo: %s, Salário: R$ %.2f\n", emp.nome, emp.cargo, emp.salario)
	}
}

func main() {
	// Criando a empresa
	empresa := Empresa{nome: "Tech Solutions"}

	// Criando empregados
	emp1 := Empregado{nome: "Beatriz", cargo: "Desenvolvedora", salario: 7000.0}
	emp2 := Empregado{nome: "Sofia", cargo: "Analista de Sistemas", salario: 6000.0}
	emp3 := Empregado{nome: "Vinicius", cargo: "Engenheiro de Software", salario: 8000.0}

	// Adicionando empregados à empresa
	empresa.AdicionarEmpregado(emp1)
	empresa.AdicionarEmpregado(emp2)
	empresa.AdicionarEmpregado(emp3)

	// Exibindo detalhes da empresa e empregados
	empresa.ExibirEmpregados()
}
