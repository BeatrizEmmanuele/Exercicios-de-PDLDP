public class ex01 {
    // Classe Carro com atributos marca, modelo e ano
    public static class Carro {
        String marca;
        String modelo;
        int ano;

        Carro(String marca, String modelo, int ano) {
            this.marca = marca;
            this.modelo = modelo;
            this.ano = ano;
        }

        void exibirDetalhes() {
            System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
        }
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Ford", "Mustang", 2020);
        Carro carro2 = new Carro("Chevrolet", "Camaro", 2021);
        Carro carro3 = new Carro("Tesla", "Model S", 2022);

        carro1.exibirDetalhes();
        carro2.exibirDetalhes();
        carro3.exibirDetalhes();
    }
}
