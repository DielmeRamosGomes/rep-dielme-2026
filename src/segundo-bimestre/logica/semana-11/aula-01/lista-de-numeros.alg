algoritmo "vetores"
var
  numeros: vetor [1..5] de inteiro
  posicao: inteiro
inicio
  numeros[1] <- 10
  numeros[2] <- 20
  numeros[3] <- 30
  numeros[4] <- 40
  numeros[5] <- 50
  para posicao de 1 ate 5 faca
    escreval("numeros[", posicao, "] = ", numeros[posicao])
  fimpara
fimalgoritmo
