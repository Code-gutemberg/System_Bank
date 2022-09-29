from abc import ABC, abstractmethod
import json


class Accounts(ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('valor do depósito precisa ser numérico')

        self.balance += value
        self.details()

    def details(self):
        print(f'Agência: {self.agency}')
        print(f'Conta: {self.account}')
        print(f'Saldo: {self.balance}')

    @abstractmethod
    def withdraw(self, value):
        ...


class CurrentAccount(Accounts):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, value):
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            for name, balance in db_json.items():
                if name == self:
                    if (balance["balance"] + balance["limit"]) < value:
                        return False
                    return True


class SavingsAccount(Accounts):
    def withdraw(self, value):
        with open('db.json', 'r+') as file:
            db_json = file.read()
            db_json = json.loads(db_json)
            for name, balance in db_json.items():
                if name == self:
                    if balance["balance"] < value:
                        return False
                    return True
