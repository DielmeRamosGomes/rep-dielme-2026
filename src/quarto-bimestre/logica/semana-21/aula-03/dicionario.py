pessoa = {
    "id": 1,
    "nome": "Dielme",
    "email": "dielme@exemplo.com"
}

'''
print(f"ID: {pessoa['id']}")
print(f"Nome: {pessoa['nome']}")
print(f"E-mail: {pessoa['email']}")
'''

#print(pessoa.keys())

#print(pessoa.items())

#print(pessoa.get("no", "Nome não encontrado"))
'''
print(pessoa.items())
print(pessoa.pop("email", "E-mail não encontrado"))
print(pessoa.items())
'''
'''
print(pessoa.items())
print(pessoa.setdefault("idade", 33))
print(pessoa.items())
'''
'''
print(pessoa.items())
print(pessoa.popitem())
print(pessoa.items())
'''
'''
print(pessoa.items())
print(pessoa.update({"nome": "Carlos", "idade": 35}))
print(pessoa.items())
'''
'''
pessoa_clone = pessoa.copy()
print(pessoa_clone.items())
'''

print(pessoa.items())
print(pessoa.clear())
print(pessoa.items())
