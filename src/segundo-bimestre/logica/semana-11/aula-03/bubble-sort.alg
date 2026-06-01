algoritmo "bubble sort"
var
  numeros: vetor[1..4] de inteiro
  i: inteiro
  j: inteiro
  auxiliar: inteiro
inicio
  numeros[1] <- 40
  numeros[2] <- 20
  numeros[3] <- 50
  numeros[4] <- 10
  para i de 1 ate 4 faca
    para j de 1 ate 4 faca
      se (numeros[j] > numeros[j+1]) entao
        auxiliar <- numeros[j]
        numeros[j] <- numeros[j+1]
        numeros[j+1] <- auxiliar
      fimse
    fimpara
  fimpara
  para i de 1 ate 4 faca
    escreval("numeros[", i, "] = ", numeros[i])
  fimpara
fimalgoritmo