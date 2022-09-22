import json

# Criando o dicionario que ficara no formato Json
db = {
    "Cliente_01": {
        "Nome": "Alex Gutemberg",
        "Senha": "0000",
        "Idade": "30",
        "Conta": "02361-0",
        "Agencia": "0236",
        "Saldo": 0
    },
    "Cliente_02": {
        "Nome": "Delis de Almeida",
        "Senha": "0000",
        "Idade": "25",
        "Conta": "02361-1",
        "Agencia": "0236",
        "Saldo": 0
    },
    "Administrador": {
        "Nome": "root_",
        "Senha": "0000",
        "Conta": "0000-99",
        "Agencia": "0099"
    }
}


# Transformando o dicionario em Json
db_json = json.dumps(db, indent=True)

'''
# Criando o arquivo .Json
with open('db.json', 'w+') as file:
    file.write(db_json)

# Lendo o arquivo .Json
with open('db.json', 'r') as file2:
    db_json2 = file2.read()


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
