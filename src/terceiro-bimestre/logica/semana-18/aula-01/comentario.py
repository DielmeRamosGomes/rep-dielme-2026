def soma(numero1, numero2):
    """
    Calcula a soma de dois números
    Args:
        numero1 (float): numero um
        numero2 (float): numero dois
    Returns:
        float: soma dos números
    """
    return numero1 + numero2

#Arranje (Preparar)
numero1 = 20
numero2 = 20
resultado_esperado = 50

# 2. Act (Agir)
resultado_obtido = soma(numero1, numero2)

# 3. Assert (Validar)
assert resultado_obtido == resultado_esperado, "Erro na soma"
print("Soma com resultado esperado")


