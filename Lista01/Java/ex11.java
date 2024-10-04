// Classe abstrata Funcionario
abstract class Funcionario {
    protected String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }

    // Método abstrato que deve ser implementado pelas subclasses
    public abstract double calcularSalario();
}

// Classe FuncionarioHorista que herda de Funcionario
class FuncionarioHorista extends Funcionario {
    private double valorPorHora;
    private int horasTrabalhadas;

    public FuncionarioHorista(String nome, double valorPorHora, int horasTrabalhadas) {
        super(nome);
        this.valorPorHora = valorPorHora;
        this.horasTrabalhadas = horasTrabalhadas;
    }

    @Override
    public double calcularSalario() {
        return valorPorHora * horasTrabalhadas;
    }
}

// Classe FuncionarioAssalariado que herda de Funcionario
class FuncionarioAssalariado extends Funcionario {
    private double salarioMensal;

    public FuncionarioAssalariado(String nome, double salarioMensal) {
        super(nome);
        this.salarioMensal = salarioMensal;
    }

    @Override
    public double calcularSalario() {
        return salarioMensal;
    }
}

// Classe principal para testar
public class ex11 {
    public static void main(String[] args) {
        Funcionario funcionario1 = new FuncionarioHorista("Ana", 20.0, 160);
        Funcionario funcionario2 = new FuncionarioAssalariado("Carlos", 3000.0);

        System.out.println("Salário de " + funcionario1.nome + ": R$" + funcionario1.calcularSalario()); // R$3200.0
        System.out.println("Salário de " + funcionario2.nome + ": R$" + funcionario2.calcularSalario()); // R$3000.0
    }
}
