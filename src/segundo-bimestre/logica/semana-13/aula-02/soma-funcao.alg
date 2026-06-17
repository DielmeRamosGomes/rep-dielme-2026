algoritmo "Soma"
funcao soma(num1: inteiro, num2: inteiro): inteiro
  var
    resultado: inteiro
  inicio
    resultado <- num1 + num2
    retorne resultado
fimfuncao
var
  num1: inteiro
  num2: inteiro
inicio
  num1 <- 10
  num2 <- 20
  escreval(num1, " + ", num2, " = ", soma(num1, num2))
fimalgoritmo