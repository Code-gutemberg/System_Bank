import json

# Criando o dicionario que ficara no formato Json
db = {
    'Pessoa 1': {
        'Nome': 'Alex',
        'Senha': '0000',
        'Idade': '30',
        'Conta': '12345',
        'Agencia': '0001-01',
        'Saldo': 0
    },

    'Pessoa 2': {
        'Nome': 'Delis',
        'Senha': '0000',
        'Idade': '25',
        'Conta': '56789',
        'Agencia': '0002-02',
        'Saldo': 0
    },
}


# Transformando o dicionario em Json
db_json = json.dumps(db, indent=True)


# Criando o arquivo .Json
with open('db.json', 'w+') as file:
    file.write(db_json)

'''
# Lendo o arquivo .Json
with open('db.json', 'r') as file2:
    db_json2 = file2.read()
'''

'''
# Transformando novamente o arquivo json em dicionario para manipular
with open('db.json', 'r') as file3:
    db_json3 = file3.read()
    db_json3 = json.loads(db_json3)


# Iterando o dicionario
for k, v in db_json3.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
'''
