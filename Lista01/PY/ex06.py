# Definindo a classe Motor
class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    # Método para exibir os detalhes do motor
    def exibir_detalhes_motor(self):
        print(f"Motor: {self.cilindrada} cilindradas, {self.potencia} HP")

# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composição: Carro contém um objeto Motor

    # Método para exibir os detalhes do carro e do motor
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}")
        self.motor.exibir_detalhes_motor()  # Chamando método da classe Motor

# Exemplo de uso com Fiat Pulse
motor_pulse = Motor(1000, 130)  # Criando um objeto Motor (1.0 turbo, 130 HP)
carro_pulse = Carro("Fiat", "Pulse", motor_pulse)  # Associando o motor ao carro

# Exibindo os detalhes do carro e do motor
carro_pulse.exibir_detalhes()
