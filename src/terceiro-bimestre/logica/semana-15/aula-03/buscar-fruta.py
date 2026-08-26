frutas = ["maçã", "banana", "pera", "abacate", "uva"]
fruta = input("digite o nome da fruta: ").lower()
for i in frutas:
    if i == fruta:
        print(f"A fruta {fruta} está na lista")
        break
else:
    print(f"A fruta {fruta} não está na lista")



