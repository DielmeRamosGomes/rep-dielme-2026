algoritmo "somaValores"
var
  numeros: vetor[1..10] de inteiro
  posicao: inteiro
  soma: inteiro
inicio
  soma <- 0
  para posicao de 1 ate 5 faca
    escreval("Digite o valor do item: ", posicao)
    leia(numeros[posicao])
    soma <- soma + numeros[posicao]
  fimpara
  escreval("Soma = ", soma)
fimalgoritmo