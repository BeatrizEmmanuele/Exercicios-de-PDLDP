class Retangulo:

    def __init__(self,comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcularArea(self):
        return self.comprimento * self.largura
    
    def calcularPerimetro(self):
        return 2* (self.largura + self.largura)
    
    ret = Retangulo(200,300)
    ret.calcularArea()
    ret.calcularPerimetro()

    print("Área do Retângulo: ", calcularArea)
    print("Perímetro do Retângulo: ", calcularPerimetro)
        