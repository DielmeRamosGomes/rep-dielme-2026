class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade
        
    def imprime_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Idade: {self.get_idade()}")

pessoa1 = Pessoa("João", 25)
pessoa1.imprime_dados()

pessoa1.set_nome("Maria")
pessoa1.set_idade(30)
pessoa1.imprime_dados()