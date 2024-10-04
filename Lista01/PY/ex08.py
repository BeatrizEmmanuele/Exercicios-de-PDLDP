# Definindo a classe Empregado
class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    # Método para exibir detalhes do empregado
    def exibir_detalhes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R$ {self.salario:.2f}")

# Definindo a classe Empresa
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []  # Lista de empregados na empresa

    # Método para adicionar um empregado à empresa
    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    # Método para exibir todos os empregados da empresa
    def exibir_empregados(self):
        print(f"Empregados da empresa {self.nome}:")
        for empregado in self.empregados:
            empregado.exibir_detalhes()

# Exemplo de uso com os empregados e empresa
empresa_ti = Empresa("Tech Solutions")

# Criando os empregados
empregado_beatriz = Empregado("Beatriz", "Desenvolvedora FrontEnd", 8500)
empregado_sofia = Empregado("Sofia", "Analista de TI", 7500)
empregado_vinicius = Empregado("Vinícius", "Gerente de TI", 12000)

# Adicionando empregados à empresa
empresa_ti.adicionar_empregado(empregado_beatriz)
empresa_ti.adicionar_empregado(empregado_sofia)
empresa_ti.adicionar_empregado(empregado_vinicius)

# Exibindo os empregados da empresa
empresa_ti.exibir_empregados()
