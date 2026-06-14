algoritmo "Listando uma matriz"
var
numeros: matriz[1..3, 1..3] de inteiro 
linha: inteiro
coluna: inteiro
inicio
  para linha de 1 ate 3 faca
    para coluna de 1 ate 3 faca
      numeros[linha, coluna] <- 0
    fimpara 
  fimpara
  para linha de 1 ate 3 faca
    para coluna de 1 ate 3 faca
      escreva(numeros[linha, coluna], " ")
    fimpara
    escreval("") 
  fimpara
fimalgoritmo