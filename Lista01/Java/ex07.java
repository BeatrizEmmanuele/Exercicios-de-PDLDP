import java.util.ArrayList;
import java.util.List;

public class ex07 {
    // Classe Professor
    public static class Professor {
        private String nome;

        public Professor(String nome) {
            this.nome = nome;
        }

        public String getNome() {
            return nome;
        }
    }

    // Classe Escola
    public static class Escola {
        private String nome;
        private List<Professor> professores;

        public Escola(String nome) {
            this.nome = nome;
            this.professores = new ArrayList<>();
        }

        public void adicionarProfessor(Professor professor) {
            professores.add(professor);
        }

        public void listarProfessores() {
            System.out.println("Professores da escola " + nome + ":");
            for (Professor professor : professores) {
                System.out.println(professor.getNome());
            }
        }
    }

    public static void main(String[] args) {
        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        Professor professor1 = new Professor("Maria");
        Professor professor2 = new Professor("João");
        
        escola1.adicionarProfessor(professor1);
        escola1.adicionarProfessor(professor2);
        
        escola2.adicionarProfessor(professor1); // Maria leciona em ambas as escolas

        escola1.listarProfessores();
        escola2.listarProfessores();
    }
}
