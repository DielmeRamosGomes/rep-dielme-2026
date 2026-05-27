algoritmo "codigoProdutos"
var
  codProdutos: vetor[1..10] de inteiro
  posicao: inteiro
  i: inteiro
  codigo: inteiro
  encontrado: logico
inicio
  encontrado <- falso
  escreval("Digite o código do produto ou (-1 para sair): ")
  leia(codigo)
  para posicao de 1 ate 10 faca
    codProdutos[posicao] <- posicao * 10
  fimpara
  enquanto codigo <> -1 faca
    para i de 1 ate 10 faca
      se (codProdutos[i] = codigo) entao
        posicao <- i
        encontrado <- verdadeiro
        interrompa
      fimse
    fimpara
    se (encontrado = verdadeiro) entao
      escreval("Encontrou o código na posição: ", posicao)
    senao
      escreval("Não encontrou o código!")
    fimse 
    escreval("Digite o código do produto ou (-1 para sair): ")
    leia(codigo)
  fimenquanto
  escreval("Fecha o algoritmo")
fimalgoritmo
