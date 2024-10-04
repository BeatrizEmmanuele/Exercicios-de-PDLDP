import java.util.ArrayList;
import java.util.List;

public class ex05 {
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

    // Método que recebe uma lista de objetos Animal
    public static void emitirSons(List<Animal> animais) {
        for (Animal animal : animais) {
            animal.som();
        }
    }

    public static void main(String[] args) {
        List<Animal> animais = new ArrayList<>();
        animais.add(new Cachorro());
        animais.add(new Gato());

        emitirSons(animais);
    }
}

