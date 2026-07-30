primeiro = int(input("Digite um numero1: "))
segundo = int(input("Digite um numero2: "))
terceiro = int(input("Digite um numero3: "))
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
    
print(f"O maior é {maior}")