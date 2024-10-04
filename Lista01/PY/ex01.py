# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para exibir os detalhes do carro
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

# Instanciando três objetos da classe Carro
carro1 = Carro("Suzuki", "Jimny", 2022)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Fiat", "Pulse", 2021)

# Exibindo os detalhes de cada carro
carro1.exibir_detalhes()
carro2.exibir_detalhes()
carro3.exibir_detalhes()
