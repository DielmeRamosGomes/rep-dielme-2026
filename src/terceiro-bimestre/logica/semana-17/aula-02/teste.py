carros = []
continuar = "s"

while continuar.lower() == "s":
    nome_carro = input("Digite o nome do carro: ")
    carros.append(nome_carro)
    
    print("\n--- LISTA DE CARROS ATUALIZADA ---")
    for i, carro in enumerate(carros, start=1):
        print(f"{i} - {carro}")
    print("---------------------------------\n")
    
    continuar = input("Deseja adicionar mais um carro? (S/N): ")

print("Programa encerrado.")