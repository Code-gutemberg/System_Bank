import json


class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}

    def insert_client(self, client):
        self.clients = client

    def insert_account(self, account):
        self.accounts = account

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

    def to_dict(self, info1, info2):
        # Se for um objeto, transforma num dict
        if hasattr(info1, '__dict__'):
            info1 = info1.__dict__
        if hasattr(info2, '__dict__'):
            info2 = info2.__dict__
        # unindo os 2 dicionarios em 1 só
        self.info3 = dict(info1, **info2)
        return self.info3

    def write_account(self, dict):
        self.db_json = dict

        # adicionando o cliente no arquivo .Json
        with open('db2.json', 'a+') as file:
            file.write(self.db_json)
