import json


class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}

    def insert_client(self, client):
        self.clients = client
        '''db_json = ''
        self.db_json = db_json

        # Transformando o dicionario em Json
        db_json = json.dumps(client, indent=True)

        # adicionando o cliente no arquivo .Json
        with open('db2.json', 'a+') as file:
            file.write(db_json)'''

    def insert_account(self, account):
        self.accounts = account
        '''db_json = ''
        self.db_json = db_json

        # Transformando o dicionario em Json
        db_json = json.dumps(account, indent=True)

        # adicionando o cliente no arquivo .Json
        with open('db2.json', 'a+') as file:
            file.write(db_json)'''

    def auth(self, agency='', account='', password='', name=''):
        self.agency = agency
        self.account = account
        self.password = password
        self._name = name
        a = agency
        ac = account
        p = password
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)

            for v in db_json.values():
                if a == v["Agencia"] and ac == v["Conta"] and p == v["Senha"]:
                    name = v["Nome"]
                    return True, name
            return False

    def para_dict(self, obj):
        # Se for um objeto, transforma num dict
        if hasattr(obj, '__dict__'):
            obj = obj.__dict__
        
        return obj
