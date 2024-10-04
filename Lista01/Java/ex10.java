public class ex10 {
    // Classe Calculadora
    public static class Calculadora {
        // Método para somar dois números
        public int somar(int a, int b) {
            return a + b;
        }

        // Método sobrecarregado para somar três números
        public int somar(int a, int b, int c) {
            return a + b + c;
        }
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        // Somando dois números
        int resultado1 = calc.somar(5, 10);
        System.out.println("Resultado da soma de dois números: " + resultado1); // 15

        // Somando três números
        int resultado2 = calc.somar(5, 10, 15);
        System.out.println("Resultado da soma de três números: " + resultado2); // 30
    }
}
