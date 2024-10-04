public class ex06 {
    // Classe Motor
    public static class Motor {
        private String tipo;

        public Motor(String tipo) {
            this.tipo = tipo;
        }

        public String getTipo() {
            return tipo;
        }
    }

    // Classe Carro que possui um Motor
    public static class Carro {
        private Motor motor;

        public Carro(Motor motor) {
            this.motor = motor;
        }

        public void exibirTipoMotor() {
            System.out.println("O carro tem um motor do tipo: " + motor.getTipo());
        }
    }

    public static void main(String[] args) {
        Motor motorV8 = new Motor("V8");
        Carro carro = new Carro(motorV8);
        carro.exibirTipoMotor(); // O carro tem um motor do tipo: V8
    }
}

