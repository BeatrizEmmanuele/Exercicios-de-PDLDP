from abc import ABC, abstractmethod

# Definindo a classe abstrata Funcionario
class Funcionario(ABC):
    
    @abstractmethod
    def calcular_salario(self) -> float:
        """Método abstrato para calcular o salário"""
        pass

# Implementando a classe FuncionarioHorista
class FuncionarioHorista(Funcionario):
    def __init__(self, horas_trabalhadas: float, valor_hora: float):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    
    def calcular_salario(self) -> float:
        """Calcula o salário com base nas horas trabalhadas e no valor da hora"""
        return self.horas_trabalhadas * self.valor_hora

# Implementando a classe FuncionarioAssalariado
class FuncionarioAssalariado(Funcionario):
    def __init__(self, salario_mensal: float):
        self.salario_mensal = salario_mensal
    
    def calcular_salario(self) -> float:
        """Retorna o salário mensal fixo"""
        return self.salario_mensal

# Exemplo de uso
def main():
    # Criando um funcionário horista
    funcionario_horista = FuncionarioHorista(horas_trabalhadas=160, valor_hora=20)
    print(f"Salário do funcionário horista: R$ {funcionario_horista.calcular_salario():.2f}")
    
    # Criando um funcionário assalariado
    funcionario_assalariado = FuncionarioAssalariado(salario_mensal=5000)
    print(f"Salário do funcionário assalariado: R$ {funcionario_assalariado.calcular_salario():.2f}")

if __name__ == "__main__":
    main()
