# Definindo a classe Professor
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []  # Lista de escolas em que o professor leciona

    # Método para associar uma escola ao professor
    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)  # Adiciona o professor à escola
        else:
            print(f"{self.nome} já leciona na escola {escola.nome}.")

    # Método para exibir as escolas em que o professor leciona
    def exibir_escolas(self):
        print(f"{self.nome} leciona nas seguintes escolas:")
        for escola in self.escolas:
            print(f"- {escola.nome}")

# Definindo a classe Escola
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  # Lista de professores da escola

    # Método para adicionar um professor à escola
    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
        else:
            print(f"{professor.nome} já é professor na escola {self.nome}.")

    # Método para exibir os professores da escola
    def exibir_professores(self):
        print(f"Professores da escola {self.nome}:")
        for professor in self.professores:
            print(f"- {professor.nome}")

# Exemplo de uso com os novos nomes
escola_geo = Escola("GEO")
escola_liceu = Escola("Liceu Paraibano")

professor_ricardo = Professor("Ricardo")
professor_simone = Professor("Simone")

# Associando professores às escolas
professor_ricardo.adicionar_escola(escola_geo)
professor_ricardo.adicionar_escola(escola_liceu)
professor_simone.adicionar_escola(escola_geo)

# Exibindo as escolas em que cada professor leciona
professor_ricardo.exibir_escolas()
professor_simone.exibir_escolas()

# Exibindo os professores de cada escola
escola_geo.exibir_professores()
escola_liceu.exibir_professores()
