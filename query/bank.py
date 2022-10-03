import json
from query.account import Accounts as acc
import app.interface as face


class Bank():
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
        self.name = name
        a = agency
        ac = account
        p = password
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            for v in db_json.values():
                if a == v["agency"]:
                    if ac == v["account"]:
                        if p == v["password"]:
                            name = v["name"]
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
        self.info4 = {}
        # coloca os dicionarios unidos dentro do dicionario nome do cliente
        self.info4[info1["name"]] = self.info3
        # Retorna um dicionario
        return self.info4

    def copy_db(self):
        # Lendo e Copiando os dados do db.json
        # retorna dicionario
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            self.copy = db_json.copy()
            return self.copy

    def write_account(self, entry):
        self.db_json = entry
        # adicionando o cliente no arquivo .Json
        with open('db.json', 'w') as file2:
            file2.write(self.db_json)

    def remove_account(self, dict, entry):
        for name in dict:
            if entry == 'root':
                face.title('Usuário protegido pelo administrador!')
                return dict
            elif entry == name:
                acc.details(name, self.copy_db())
                while True:
                    menu = input('Deseja excluir [S/N]: ')[0]
                    if menu in 'Ss':
                        face.title('EXCLUIDO COM SUCESSO!')
                        del dict[name]
                        return dict
                    if menu in 'Nn':
                        face.title('EXCLUSÃO CANCELADA!')
                        break
                    else:
                        print('Digite Sim ou Não.')
                return dict
        face.title('USUÁRIO INEXISTENTE!')
        return dict
