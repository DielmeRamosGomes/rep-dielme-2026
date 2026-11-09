'''
Encapsulamento é o princípio da POO que consiste em proteger os 
dados internos de um objeto, controlando como eles são acessados
e modificados.
A ideia é:
Esconder detalhes internos da implementação.
Evitar alterações indevidas nos atributos.
Permitir validações ao alterar valores.
'''

class Pessoa:
    def __init__(self, nome, email):
        #self.__nome = nome
        #self.__email = email
        self.set_nome(nome)
        self.set_email(email)
        
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_email(self, email):
        self.__email = email

pessoa1 = Pessoa("Paulo", "paulo@hotmail.com")    
#print(f"Nome: {pessoa1.__nome}") nome não acessível porque está privado com __ 

print(f"Nome: {pessoa1.get_nome()}")
pessoa1.set_nome("Carlos")
print(f"Nome alterado: {pessoa1.get_nome()}")
