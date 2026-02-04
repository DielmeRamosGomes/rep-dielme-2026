def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2 

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def menu():
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do programa\n")
   
def execucao(opcao, num1, num2):
    if opcao == 1:
        print(f"{num1} + {num2} = {soma(num1, num2)}\n")
    elif opcao == 2:
        print(f"{num1} - {num2} = {subtracao(num1, num2)}\n")
    elif opcao == 3:
       print(f"{num1} x {num2} = {multiplicacao(num1, num2)}\n")
    elif opcao == 4:
        try:
            print(f"{num1} / {num2} = {divisao(num1, num2)}\n")
        except ZeroDivisionError:
          print("Erro: denominador não pode ser zero!")  
    elif opcao == 5:
        print("Saindo do programa")
    else:
        print("A opção só poder der no intervalo de [1, 4]")
 
def main():
    while True:
        num1 = int(input("\nDigite um número: "))
        num2 = int(input("Digite outro número: "))
        menu()
        opcao = int(input("\nDigite a opção escolhida: "))
        execucao(opcao, num1, num2)
        continua = input("Deseja continuar executando? [s,n]: ").lower()
        if continua == 'n':
            break    
 
main()
    
