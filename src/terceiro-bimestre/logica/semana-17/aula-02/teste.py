carros = []

while True:
    
    carros.append(input("\nDigite o nome do carro: "))
    
    
    print("\n--- Lista Atualizada ---")
    for i, carro in enumerate(carros, 1):
        print(f"{i}º - {carro}")
        

    if input("\nQuer continuar? (s/n): ").lower() != 's':
        break

print("\nFim do programa!")