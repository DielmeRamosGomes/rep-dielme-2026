algoritmo "busca-linear"
var 
  numeros: vetor[1..5] de inteiro
  posicao: inteiro
  aux: inteiro
  codigo: inteiro
  encontrou: logico
inicio
  encontrou <- falso
  numeros[1] <- 30
  numeros[2] <- 40
  numeros[3] <- 10
  numeros[4] <- 5
  numeros[5] <- 7
  escreval("Digite o código do produto: ")
  leia(codigo)
  para posicao de 1 ate 5 faca
    se (codigo = numeros[posicao]) entao
       encontrou <- verdadeiro
       aux <- posicao
       interrompa
    fimse
  fimpara
  se (encontrou = verdadeiro) entao
    escreval("Encontrou o código na posicao: ", aux)
  senao
    escreval("Não encontrou o código")
  fimse
fimalgoritmo