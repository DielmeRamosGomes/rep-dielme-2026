algoritmo "verdadeiro-falso"
var
valores: vetor[1..15] de logico
posicao: inteiro
eh_verdade: logico
inicio
  eh_verdade <- verdadeiro
  para posicao de 1 ate 15 faca
    se (eh_verdade = verdadeiro) entao
      valores[posicao] <- eh_verdade
      eh_verdade <- falso
    senao
      valores[posicao] <- eh_verdade
      eh_verdade <- verdadeiro
    fimse
  fimpara
  para posicao de 1 ate 15 faca
    escreval("valores[", posicao, "] = ", valores[posicao])
  fimpara
fimalgoritmo