# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # Atributo para armazenar a velocidade do carro
    
    # Método para exibir os detalhes do carro
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")
    
    # Método para acelerar o carro
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")
    
    # Método para frear o carro
    def frear(self, decremento):
        if self.velocidade - decremento < 0:
            self.velocidade = 0
        else:
            self.velocidade -= decremento
        print(f"O carro freou. Velocidade atual: {self.velocidade} km/h")
    
    # Método para exibir a velocidade atual
    def exibir_velocidade(self):
        print(f"A velocidade atual é: {self.velocidade} km/h")

# Instanciando um objeto da classe Carro
meu_carro = Carro("Fiat", "Pulse", 2021)

# Exibindo os detalhes do carro
meu_carro.exibir_detalhes()

# Acelerando e exibindo a velocidade
meu_carro.acelerar(30)
meu_carro.acelerar(20)

# Freando e exibindo a velocidade
meu_carro.frear(15)
meu_carro.frear(50)

# Exibindo a velocidade final
meu_carro.exibir_velocidade()
