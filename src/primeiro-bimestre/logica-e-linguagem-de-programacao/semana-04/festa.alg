algoritmo "Festa"
var
  idade: inteiro
  resposavel: logico
inicio
escreva("Digite uma idade: ")
leia(idade)
escreva("O responsável acompanha?[verdadeiro, falso]")
leia(resposavel)
se ((idade >= 18) ou (resposavel = verdadeiro)) entao
  escreva("A pessoa pode entrar na festa")
senao
  escreva("A pessoa NÂO pode entrar na festa")
fimse
fimalgoritmo
