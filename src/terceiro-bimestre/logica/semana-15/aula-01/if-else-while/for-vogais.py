conta_letras = 0
palavra = input("Digite uma palavra: ").lower()
for letra in palavra:
    if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
        conta_letras += 1   
print(f"O número de vogais é = {conta_letras}")