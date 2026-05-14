algoritmo "CalculadoraDeMedia"
var
  soma_notas: real
  qtd_notas: inteiro
  nota_digitada: real
  media_turma: real
inicio
  soma_notas <- 0
  qtd_notas <- 0
  escreval("Digite a nota do aluno (ou -1 para calcular a média):")
  leia(nota_digitada)
  enquanto nota_digitada <> -1 faca
    soma_notas <- soma_notas + nota_digitada
    qtd_notas <- qtd_notas + 1
    escreval("Digite a nota do aluno (ou -1 para calcular a média):")
    leia(nota_digitada)
  fimenquanto
  se qtd_notas > 0 entao
    media_turma <- soma_notas / qtd_notas
    escreval("--------------------")
    escreval("RESULTADO FINAL")
    escreval("Total de notas inseridas: ", qtd_notas)
    escreval("A média da turma é: ", media_turma:4:2) // :4:2 formata para 2 
  senao
    escreval("Nenhuma nota foi inserida.")
  fimse
fimalgoritmo