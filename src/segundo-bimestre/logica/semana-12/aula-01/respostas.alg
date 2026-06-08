/*Escreva um programa que defina um número secreto (por exemplo,
42). O programa deve pedir para o usuário tentar adivinhar o 
número. Enquanto o usuário errar, o programa deve dizer se o 
palpite foi "Muito alto" ou "Muito baixo" e pedir um novo 
palpite. Quando o usuário acertar, o programa exibe uma 
mensagem de parabéns e encerra.
*/

algoritmo "Acertar o numero secreto"
var
  numSecreto: inteiro
  palpite: inteiro
inicio
  numSecreto <- 56
  escreval("Digite o número secreto: ")
  leia(palpite)
  enquanto numSecreto <> palpite faca
    se (palpite > numSecreto) entao
      escreval("Muito alto - tente novamente")
    senao
      escreval("Muito baixo - tente novamente")
    fimse
  escreval("Digite o número secreto: ")
  leia(palpite)
  fimenquanto
  escreval("Parabéns você acertou o numero")
fimalgoritmo

/*Desenvolva um programa que peça ao usuário para digitar um 
número inteiro. O programa deve utilizar um laço para para 
calcular e exibir a tabuada desse número de 1 a 10.*/

algoritmo "Acertar o numero secreto"
var
  numero: inteiro
  i: inteiro
  resultado: inteiro
inicio
  escreval("Digite o numero da tabuada: ")
  leia(numero)
  para i de 1 ate 10 faca
    resultado <- i * numero
    escreval(numero, " X ", i, " = ", resultado)
  fimpara
fimalgoritmo

/*Escreva um programa que simule o funcionamento de um 
cronômetro digital que conta de 00:00 até 01:20. 
Use dois laços para aninhados: o externo para controlar os 
minutos (de 0 a 1) e o interno para controlar os segundos 
(de 0 a 20). Exiba o tempo no formato "Minutos:Segundos".*/

algoritmo "Cronometro"
var
  minutos: inteiro
  segundos: inteiro
inicio
    para minutos de 0 ate 1 faca
      para segundos de 0 ate 20 faca
        escreval(minutos, ":", segundos)
      fimpara
    fimpara
fimalgoritmo
