from pessoa import Pessoa
from control import Control

if __name__=="__main__":
    control = Control()
    pessoa1 = Pessoa("Dielme Ramos", "123-456-789-34")
    pessoa2 = Pessoa("Carlos Augusto", "123-456-789-35")
    #pessoa.setNome("Carlos")
    #pessoa.getNome()
    #pessoa.imprime_pessoa()
    control.add_pessoa(pessoa1)
    control.add_pessoa(pessoa2)
    control.lista_pessoas()
