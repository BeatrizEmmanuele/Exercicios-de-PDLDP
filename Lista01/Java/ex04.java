public class ex04 {
    // Classe base Animal
    public static class Animal {
        void som() {
            System.out.println("O animal faz um som.");
        }
    }

    // Classe Cachorro que herda de Animal
    public static class Cachorro extends Animal {
        @Override
        void som() {
            System.out.println("O cachorro faz: Au Au!");
        }
    }

    // Classe Gato que herda de Animal
    public static class Gato extends Animal {
        @Override
        void som() {
            System.out.println("O gato faz: Miau!");
        }
    }

    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        cachorro.som(); // O cachorro faz: Au Au!
        gato.som();     // O gato faz: Miau!
    }
}

