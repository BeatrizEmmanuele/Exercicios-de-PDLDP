# Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    # Método genérico de som (a ser sobrescrito nas subclasses)
    def som(self):
        pass

# Classe derivada Cachorro
class Cachorro(Animal):
    def som(self):
        print(f"{self.nome} faz: Au Au Au Au!")

# Classe derivada Gato
class Gato(Animal):
    def som(self):
        print(f"{self.nome} faz: Miauuuuuuuu!")

# Exemplo de uso das classes
cachorro = Cachorro("Pretinho")
gato = Gato("Olívio")

# Chamando o método som para cada objeto
cachorro.som()  # Saída: Rex faz: Au Au!
gato.som()      # Saída: Mingau faz: Miau!
