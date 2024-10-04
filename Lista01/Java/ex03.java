public class ex03 {
    // Classe ContaBancaria com encapsulamento
    public static class ContaBancaria {
        private double saldo;
        private String titular;

        public ContaBancaria(String titular) {
            this.titular = titular;
            this.saldo = 0.0;
        }

        public void depositar(double valor) {
            if (valor > 0) {
                saldo += valor;
                System.out.println("Depósito de R$" + valor + " realizado.");
            }
        }

        public void sacar(double valor) {
            if (valor > 0 && valor <= saldo) {
                saldo -= valor;
                System.out.println("Saque de R$" + valor + " realizado.");
            } else {
                System.out.println("Saldo insuficiente ou valor inválido.");
            }
        }

        public double getSaldo() {
            return saldo;
        }
    }

    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("João");
        conta.depositar(1500);
        conta.sacar(500);
        System.out.println("Saldo atual: R$" + conta.getSaldo()); // Saldo atual: R$1000.0
    }
}

