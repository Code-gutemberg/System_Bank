import json
import app.interface as face


class Accounts():
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    def details(self, dict):
        for name, details in dict.items():
            if self == 'root':
                face.title('Usuário protegido pelo administrador!')
                input()
                return True
            elif name == self:
                print('=' * 50)
                print(f'Nome: {details["name"]}')
                print(f'CPF: {details["cpf"]}')
                print(f'Agencia: {details["agency"]}')
                print(f'Conta: {details["account"]}')
                print(f'Saldo: R$ {details["balance"]}')
                print('=' * 50)
                input()
                return True
        return False


class CurrentAccount(Accounts):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, value):
        # Recebe nome e valor
        # retorna Falso se o saque for maior que a soma do saldo e limite
        # retorna True se saldo suficiente
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            for name, balance in db_json.items():
                if name == self:
                    if (balance["balance"] + balance["limit"]) < value:
                        return False
                    return True

    def update(self, dict, value):
        # Recebe nome, db dict e valor
        # Retorna o dict atualizado com o desconto do valor
        for name, balance in dict.items():
            if name == self:
                balance["balance"] -= value
                return dict

    def deposit(self, dict, value):
        # Recebe nome, db dict e valor
        # Retorna o dict atualizado com o desconto do valor
        for name, balance in dict.items():
            if name == self:
                balance["balance"] += value
                return dict


class SavingsAccount(Accounts):
    def withdraw(self, value):
        # Recebe nome e valor
        # retorna Falso se saldo insuficiente
        # retorna True se saldo suficiente
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            for name, balance in db_json.items():
                if name == self:
                    if balance["balance"] < value:
                        return False
                    return True

    def update(self, dict, value):
        # Recebe nome, db dict e valor
        # Retorna o dict atualizado com o desconto do valor
        for name, balance in dict.items():
            if name == self:
                balance["balance"] -= value
                return dict

    def deposit(self, dict, value):
        # Recebe nome, db dict e valor
        # Retorna o dict atualizado com o desconto do valor
        for name, balance in dict.items():
            if name == self:
                balance["balance"] += value
                return dict
