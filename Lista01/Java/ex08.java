import java.util.ArrayList;
import java.util.List;

public class ex08 {
    // Classe Empregado
    public static class Empregado {
        private String nome;
        private String cargo;
        private double salario;

        public Empregado(String nome, String cargo, double salario) {
            this.nome = nome;
            this.cargo = cargo;
            this.salario = salario;
        }

        public String getNome() {
            return nome;
        }

        public String getCargo() {
            return cargo;
        }

        public double getSalario() {
            return salario;
        }
    }

    // Classe Empresa
    public static class Empresa {
        private String nome;
        private List<Empregado> empregados;

        public Empresa(String nome) {
            this.nome = nome;
            this.empregados = new ArrayList<>();
        }

        public void adicionarEmpregado(Empregado empregado) {
            empregados.add(empregado);
        }

        public void listarEmpregados() {
            System.out.println("Empregados da empresa " + nome + ":");
            for (Empregado empregado : empregados) {
                System.out.println(empregado.getNome() + ", Cargo: " + empregado.getCargo() + ", Salário: R$" + empregado.getSalario());
            }
        }
    }

    public static void main(String[] args) {
        Empresa empresa = new Empresa("Tech Solutions");
        
        Empregado empregado1 = new Empregado("Ana", "Desenvolvedora", 5000);
        Empregado empregado2 = new Empregado("Carlos", "Gerente", 7000);
        
        empresa.adicionarEmpregado(empregado1);
        empresa.adicionarEmpregado(empregado2);
        
        empresa.listarEmpregados();
    }
}
