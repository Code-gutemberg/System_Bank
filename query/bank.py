import json


class Bank:
    def __init__(self):
        ...

    def insert_client(self, client):
        self.client.append(client)

    def insert_account(self, account):
        self.accounts.append(account)

    def auth(self, agency='', account='', password='', name=''):
        self.agency = agency
        self.account = account
        self.password = password
        self.name = name
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
