// Interface Imprimível
interface Imprimivel {
    void imprimir();
}

// Classe Relatório que implementa a interface Imprimível
class Relatório implements Imprimivel {
    private String conteudo;

    public Relatório(String conteudo) {
        this.conteudo = conteudo;
    }

    @Override
    public void imprimir() {
        System.out.println("Imprimindo Relatório: " + conteudo);
    }
}

// Classe Contrato que implementa a interface Imprimível
class Contrato implements Imprimivel {
    private String detalhes;

    public Contrato(String detalhes) {
        this.detalhes = detalhes;
    }

    @Override
    public void imprimir() {
        System.out.println("Imprimindo Contrato: " + detalhes);
    }
}

// Classe principal
public class ex09 {
    public static void main(String[] args) {
        Imprimivel relatorio = new Relatório("Relatório de Vendas");
        Imprimivel contrato = new Contrato("Contrato de Prestação de Serviços");

        relatorio.imprimir(); // Imprimindo Relatório: Relatório de Vendas
        contrato.imprimir();  // Imprimindo Contrato: Contrato de Prestação de Serviços
    }
}
