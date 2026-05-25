algoritmo "vetores"
var
  numeros: vetor [1..5] de inteiro
  contador: inteiro
inicio
  numeros[1] <- 1
  numeros[2] <- 2
  numeros[3] <- 3
  numeros[4] <- 4
  numeros[5] <- 5
  para contador de 1 ate 5 faca
    escreval("lista[", contador, "] = ", numeros[contador])
  fimpara
fimalgoritmo
