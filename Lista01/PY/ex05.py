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
        print(f"{self.nome} faz: Au Au Au!")

# Classe derivada Gato
class Gato(Animal):
    def som(self):
        print(f"{self.nome} faz: Miauuu!")

# Classe derivada Vaca (para adicionar mais um exemplo)
class Vaca(Animal):
    def som(self):
        print(f"{self.nome} faz: Muuuu!")

# Função que recebe uma lista de objetos Animal e chama o método som
def emitir_sons(animais):
    for animal in animais:
        animal.som()

# Exemplo de uso
cachorro = Cachorro("Pretinho")
gato = Gato("Olívio")
vaca = Vaca("Joa")

# Criando uma lista de objetos de diferentes classes
lista_animais = [cachorro, gato, vaca]

# Chamando a função que emite os sons de cada animal
emitir_sons(lista_animais)
