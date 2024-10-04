// Classe de exceção personalizada
class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(String mensagem) {
        super(mensagem);
    }
}

// Classe ContaBancaria
class ContaBancaria {
    private double saldo;

    public ContaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    public void sacar(double valor) throws SaldoInsuficienteException {
        if (valor > saldo) {
            throw new SaldoInsuficienteException("Saldo insuficiente para realizar o saque.");
        }
        saldo -= valor;
        System.out.println("Saque de R$" + valor + " realizado com sucesso.");
    }

    public double getSaldo() {
        return saldo;
    }
}

// Classe principal para testar
public class ex15 {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria(100.0);

        try {
            conta.sacar(150.0);
        } catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage()); // Saldo insuficiente para realizar o saque.
        }

        System.out.println("Saldo atual: R$" + conta.getSaldo()); // Saldo atual: R$100.0
    }
}
