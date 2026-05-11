algoritmo "soma"
var
  num1: inteiro
  num2: inteiro
  resultado: inteiro
  sentinela: inteiro
inicio
  sentinela <- 0
  enquanto sentinela <> -99 faca
    escreva(" Digite o numero1: ")
    leia(num1)
    escreva(" Digite o numero2: ")
    leia(num2)
    resultado <- num1 + num2
    escreva(num1, " + ", num2, " = ", resultado)
    escreva(" Digite -99 para sair")
    leia(sentinela)
  fimenquanto
  escreval("Saiu do laço!")
fimalgoritmo