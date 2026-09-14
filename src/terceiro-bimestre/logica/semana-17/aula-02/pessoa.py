class Pessoa():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
        
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def getCpf(self):
        return self.__cpf
        
    def imprime_pessoa(self):
        print(f"Nome: {self.getNome()}")
        print(f"Cpf: {self.getCpf()}")
