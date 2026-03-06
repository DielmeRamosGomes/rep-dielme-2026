desconto = 0
desconto_venda = 0
frete = 15
subtotal = 0
valor_venda = float(input("Digite o valor da venda: "))
if valor_venda >= 100 and valor_venda < 500:
    desconto = 0.05
    desconto_venda = valor_venda * desconto
    subtotal = valor_venda
    if valor_venda <= 200:    
        valor_venda = valor_venda - desconto_venda
        valor_venda = valor_venda + frete
    else:
        valor_venda = valor_venda - desconto_venda
        frete = 0
if valor_venda >= 500:
    desconto = 0.10
    frete = 0
    desconto_venda = valor_venda * desconto
    subtotal = valor_venda
    valor_venda = valor_venda - desconto_venda

print(f"\nSubtotal: R${subtotal:.2f}")  
print(f"\nValor do desconto: R${desconto_venda:.2f}")
print(f"\nValor do frete: R${frete:.2f}")
print(f"\nValor da venda com desconto: R${valor_venda:.2f}")