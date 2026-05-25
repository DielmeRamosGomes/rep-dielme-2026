algoritmo "comparação-de-listas"

var
  numeros: vetor [1..5] de inteiro
  i: inteiro
  j: inteiro
inicio
  numeros[1] <- 10
  numeros[2] <- 20
  numeros[3] <- 30
  numeros[4] <- 30
  numeros[5] <- 20 
  para i de 1 ate 5 faca
    para j de i+1 ate 5 faca
      se (numeros[i] = numeros[j]) entao
        escreval("numero[", i, "]", " = numero[", j, "] = ", numeros[j]) 
      fimse
    fimpara
  fimpara  
fimalgoritmo



