'''
Uma progressão aritmética (P.A.) é uma sequência de números 
onde cada termo, a partir do segundo, é igual ao anterior 
somado a um valor fixo chamado razão
Você descobre a razão ao subtrair um termo pelo número que vem
antes dele (r = a_n - a_n-1)).
formula geral da P.A.:
a_n = a_1 + (n - 1) * r
a_n = n-ésimo termo da P.A.
a_1 = primeiro termo da P.A.
n = posição do termo na P.A.
r = razão da P.A.
soma dos n primeiros termos da P.A.:
S_n = (a_1 + a_n) * n / 2
'''
pa = [2, 5, 8, 11, 14]

razao = pa[1] - pa[0] 
print(f'Razão da P.A: {razao}')
n = 5
a_n = pa[0] + (n-1) * razao
print(f'O {n}º termo da P.A é: {a_n}')

soma = ((pa[0] + a_n) * n) / 2
print(f'A soma dos {n} primeiros termos da P.A é: {soma}')