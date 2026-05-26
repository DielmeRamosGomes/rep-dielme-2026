algoritmo "vetores"
var
  numeros: vetor [1..5] de inteiro
  contador: inteiro
inicio
  para contador de 1 ate 5 faca
    escreval("Digite o item: ", contador)
    leia(numeros[contador])
  fimpara
  para contador de 1 ate 5 faca
    escreva("")
    escreval("numeros[", contador, "] = ", numeros[contador])
  fimpara
fimalgoritmo