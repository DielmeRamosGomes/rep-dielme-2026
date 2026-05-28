algoritmo "SomaProdutosDigitados"
var
  produtos: vetor[1..5] de inteiro
  posicao: inteiro
  soma: inteiro
inicio
  soma <- 0
  para posicao de 1 ate 5 faca
    escreval("Digite o produto: ", posicao)
    leia(produtos[posicao])
  para posicao de 1 ate 5 faca
    soma <- soma + produtos[posicao]
  fimpara
  escreval("Soma dos produtos é = ", soma)
fimalgoritmo