nota = int(input("\nDigite a nota do aluno: ")) 
if nota >= 1 and nota <= 10:
    if nota >= 6:
        print("Parabéns! Você foi aprovado!")
    else:
        print("Infelizmente, você não foi aprovado.")
else:
    print("Nota inválida. Por favor, digite uma nota entre 1 e 10.")