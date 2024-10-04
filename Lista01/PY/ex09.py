from abc import ABC, abstractmethod

# Definindo a classe abstrata Imprimivel
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self) -> None:
        pass

# Implementando a classe Relatorio
class Relatorio(Imprimivel):
    def imprimir(self) -> None:
        print("Imprimindo relatório...")

# Implementando a classe Contrato
class Contrato(Imprimivel):
    def imprimir(self) -> None:
        print("Imprimindo contrato...")

# Função para demonstrar a impressão
def imprimir_documento(documento: Imprimivel) -> None:
    documento.imprimir()

# Exemplo de uso
relatorio = Relatorio()
contrato = Contrato()

imprimir_documento(relatorio)
imprimir_documento(contrato)
