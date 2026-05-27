algoritmo "codigoProdutos"
var
  codProdutos: vetor[1..10] de inteiro
  posicao: inteiro
  codigo: inteiro
inicio
  codigo <- 1
  para posicao de 1 ate 10 faca
    codProdutos[posicao] <- posicao * 10
  fimpara
  enquanto codigo <> -1 faca
    escreval("Digite o código do produto ou (-1 para sair): ")
    leia(codigo)
    para posicao de 1 ate 10 faca
      se (codProdutos[posicao] = codigo) entao
        escreval("Encontrou o código na posição; ", posicao)
      senao
        escreval("Não encontrou o código")
      fimse
    fimpara
  fimenquanto
fimalgoritmo