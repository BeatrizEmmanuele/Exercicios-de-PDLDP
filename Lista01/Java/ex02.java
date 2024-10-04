public class ex02 {
    // Classe Carro com métodos acelerar e frear
    public static class Carro {
        String marca;
        String modelo;
        int ano;
        int velocidade;

        Carro(String marca, String modelo, int ano) {
            this.marca = marca;
            this.modelo = modelo;
            this.ano = ano;
            this.velocidade = 0;
        }

        void acelerar(int incremento) {
            velocidade += incremento;
        }

        void frear(int decremento) {
            velocidade -= decremento;
            if (velocidade < 0) {
                velocidade = 0;
            }
        }

        void exibirVelocidade() {
            System.out.println("Velocidade atual: " + velocidade + " km/h");
        }
    }

    public static void main(String[] args) {
        Carro carro = new Carro("Honda", "Civic", 2021);
        carro.acelerar(50);
        carro.exibirVelocidade(); // Velocidade atual: 50 km/h
        carro.frear(20);
        carro.exibirVelocidade(); // Velocidade atual: 30 km/h
    }
}

