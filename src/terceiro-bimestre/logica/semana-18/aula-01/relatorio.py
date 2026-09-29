def processar_fechamento_caixa(vendas_do_dia):
    total_acumulado = 0.0
    taxa_imposto = 0.10
    
    for valor_venda in vendas_do_dia:
        imposto = valor_venda * taxa_imposto
        # ERRO LÓGICO OCULTO ABAIXO
        total_acumulado += valor_venda + imposto
        
    return total_acumulado

# O Teste Unitário (Sintoma da falha)
vendas_teste = [100.0, 200.0, 50.0]
# O gabarito esperado é 385.0 (110 + 220 + 55)
resultado = processar_fechamento_caixa(vendas_teste)
print(f"Resultado obtido: {resultado}")
