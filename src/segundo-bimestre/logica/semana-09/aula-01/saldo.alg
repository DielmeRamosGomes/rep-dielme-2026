// Desafio: Imagine que um cliente tem R$ 100 em uma conta de
// jogos e quer fazer saques consecutivos de R$ 20 até zerar
// a conta. Escreva um programa que mostre o saldo atualizado 
// a cada retirada e, no final, exiba a mensagem "Saldo 
// esgotado!".

algoritmo "DiminuindoSaldo"
var
  saldo: real
  contador: real
inicio
  saldo <- 100
  para contador de saldo ate 1 passo -20 faca
    saldo <- contador
    escreval("Saldo = ", saldo)
  fimpara
fimalgoritmo

