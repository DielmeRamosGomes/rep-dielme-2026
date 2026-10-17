class Pessoa():
    def __init__(self, nome, idade, email, senha):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__senha = senha
        
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getEmail(self):
        return self.__email
    
    def getPessoa(self):
        print(f"Nome: {self.getNome()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Email: {self.getEmail()}")
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, email, senha, cargo):
        super().__init__(nome, idade, email, senha)
        self.__cargo = cargo  

    def getCargo(self):
        return self.__cargo

    def getFuncionario(self):
        self.getPessoa()
        print(f"Cargo: {self.getCargo()}")

pessoa1 = Pessoa("Carlos", 20, "carlos@exemplo.com", "1234")
     
pessoa2 = Funcionario("Dielme", 32, "dielmeuba@hotmail.com", "12345", "Professor")

pessoa1.getPessoa()
print("----------------------------------------------------------")
pessoa2.getFuncionario()
