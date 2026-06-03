algoritmo "cadastro-de-login"

var
senhas: vetor[1..3] de caractere
emails: vetor[1..3] de caractere
senha: caractere
email: caractere
posicao: inteiro
encontrouEmail: logico
encontrouSenha: logico
inicio
  encontrouEmail <- falso
  encontrouSenha <- falso
  senhas[1] <- "senha123"
  senhas[2] <- "senha456"
  senhas[3] <- "senha789"
  emails[1] <- "dielme@exemplo.com"
  emails[2] <- "carlos@exemplo.com"
  emails[3] <- "roberto@exemplo.com"
  escreval("Digite o email: ")
  leia(email)
  escreval("Digite a senha: ")
  leia(senha)
  para posicao de 1 ate 3 faca
    se (email = emails[posicao]) entao
      encontrouEmail <- verdadeiro
      interrompa
    fimse
  fimpara
  para posicao de 1 ate 3 faca
    se (senha = senhas[posicao]) entao
      encontrouEmail <- verdadeiro
      interrompa
    fimse
  fimpara
  se ((encontrouEmail = verdadeiro) E (encontrouSenha = verdadeiro)) entao
    escreval("Email e Senha Corretas: Bem-Vindo!")
  senao
    escreval("Email ou Senha não encontradas")
  fimse
fimalgoritmo
