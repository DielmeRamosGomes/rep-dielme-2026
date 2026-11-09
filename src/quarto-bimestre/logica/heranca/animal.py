'''
class Filha(Pai): cria uma herança.
A classe filha herda atributos e métodos da classe pai.
Métodos podem ser sobrescritos (override).
super() acessa a implementação da classe pai.
Python suporta herança múltipla.
Exemplo de relação "é um":
Cachorro é um Animal.
Gato é um Animal.
Aluno é uma Pessoa.
'''

class Animal:
    def __init__(self, nome):
        self.__nome
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def emitir_som(self):
        print("Som genérico")    
            
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().set_nome(nome)
        self.__raca = raca
    
    def get_raca(self):
        return self.__raca
        
    def set_raca(self, raca):
        self.__raca = raca
    
    def emitir_som(self):
        print("Au Au Au")
  
class Voar:
    def voar(self):
        print("Voando")


class Nadar:
    def nadar(self):
        print("Nadando")


class Pato(Animal, Voar, Nadar):
    def __init__(self, nome, raca):
        super().set_nome(nome)
        self.__raca = raca
    
    def get_raca(self):
        return self.__raca
        
    def set_raca(self, raca):
        self.__raca = raca
    
cachorro1 = Cachorro("Rex", "Mastim-Tibetano")
print(f"Nome: {cachorro1.get_nome()}")
print(f"Raça: {cachorro1.get_raca()}")
cachorro1.emitir_som()

print("\n------------------------------------------------")

pato1 = Pato("Patolino", "Pato Pequim")
print(f"Nome: {pato1.get_nome()}")
print(f"Raça: {pato1.get_raca()}")
pato1.voar()
pato1.nadar()
pato1.emitir_som()