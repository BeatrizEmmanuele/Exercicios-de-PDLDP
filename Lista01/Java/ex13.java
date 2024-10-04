public class ex13 {
    // Método estático para calcular o fatorial
    public static long fatorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Número deve ser não negativo.");
        }
        long resultado = 1;
        for (int i = 2; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }

    public static void main(String[] args) {
        int numero = 5;
        long resultado = fatorial(numero);
        System.out.println("Fatorial de " + numero + " é: " + resultado); // Fatorial de 5 é: 120
    }
}

