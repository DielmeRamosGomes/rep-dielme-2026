A = int(input("Digite um numero A: "))
B = int(input("Digite um numero B: "))
C = int(input("Digite um numero C: "))
if (A > B) and (A > C):
    print(f"O {A} é o maior!")
elif (B > A) and (B > C):
    print(f"O {B} é o maior!")
elif (C > A) and (C > B):
    print(f"O {C} é o maior!")
elif (A == B) and (A == C) and (B == C):
    print(f"Os numeros {A}, {B} e {C} são iguais")
else:
    print("Algo deu errado!") 

