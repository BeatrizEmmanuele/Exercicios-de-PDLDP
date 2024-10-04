package main

import "fmt"

// Definindo a struct Professor
type Professor struct {
	nome string
	escolas []*Escola // Lista de escolas em que o professor leciona
}

// Adiciona uma escola à lista de escolas do professor
func (p *Professor) AdicionarEscola(e *Escola) {
	p.escolas = append(p.escolas, e)
}

// Definindo a struct Escola
type Escola struct {
	nome       string
	professores []*Professor // Lista de professores que lecionam na escola
}

// Adiciona um professor à lista de professores da escola
func (e *Escola) AdicionarProfessor(p *Professor) {
	e.professores = append(e.professores, p)
}

// Função para exibir detalhes da escola e seus professores
func (e Escola) ExibirProfessores() {
	fmt.Printf("Escola: %s\n", e.nome)
	for _, professor := range e.professores {
		fmt.Printf("Professor: %s\n", professor.nome)
	}
}

// Função para exibir detalhes do professor e suas escolas
func (p Professor) ExibirEscolas() {
	fmt.Printf("Professor: %s\n", p.nome)
	for _, escola := range p.escolas {
		fmt.Printf("Escola: %s\n", escola.nome)
	}
}

func main() {
	// Criando as escolas
	escolaA := Escola{nome: "GEO"}
	escolaB := Escola{nome: "Liceu Paraibano"}

	// Criando os professores
	professor1 := Professor{nome: "Ricardo"}
	professor2 := Professor{nome: "Simone"}

	// Associando professores a escolas
	escolaA.AdicionarProfessor(&professor1)
	escolaA.AdicionarProfessor(&professor2)
	escolaB.AdicionarProfessor(&professor1)

	// Associando escolas a professores
	professor1.AdicionarEscola(&escolaA)
	professor1.AdicionarEscola(&escolaB)
	professor2.AdicionarEscola(&escolaA)

	// Exibindo os professores de cada escola
	escolaA.ExibirProfessores()
	escolaB.ExibirProfessores()

	// Exibindo as escolas de cada professor
	professor1.ExibirEscolas()
	professor2.ExibirEscolas()
}
