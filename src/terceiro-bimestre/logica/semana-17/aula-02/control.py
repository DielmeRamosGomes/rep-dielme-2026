from pessoa import Pessoa

class Control():
    def __init__(self):
        self.__lista = []

    def add_pessoa(self, pessoa):
        self.__lista.append(pessoa)
        
    def lista_pessoas(self):
        for pessoa in self.__lista:
            pessoa.imprime_pessoa()
            print("------------------------------------------")

