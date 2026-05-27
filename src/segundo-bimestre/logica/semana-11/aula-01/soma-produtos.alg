algoritmo "SomaProdutos"
var
  produtos: vetor[1..5] de inteiro
  posicao: inteiro
  soma: inteiro
inicio
  soma <- 0
  produtos[1] <- 10
  produtos[2] <- 20
  produtos[3] <- 30
  produtos[4] <- 40
  produtos[5] <- 50
  para posicao de 1 ate 5 faca
    soma <- soma + produtos[posicao]
  fimpara
  escreval("Soma dos produtos é = ", soma)
fimalgoritmo