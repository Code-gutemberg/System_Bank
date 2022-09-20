
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

    def details(self, agency, account, balance=0):
        self.agency = agency
        self.account = account
        self.balance = balance
        a = agency
        ac = account
        with open('db.json', 'r') as file:
            db_json = file.read()
            db_json = json.loads(db_json)

            for v in db_json.values():
                if a == v["Agencia"] and ac == v["Conta"]:
                    agency = v["Agencia"]
                    account = v["Conta"]
                    balance = v["Saldo"]
                    return agency, account, balance
            return False
        '''
        print(f'Agência: {self.agency}')
        print(f'Conta: {self.account}')
        print(f'Saldo: {self.balance}')
        '''

    @abstractmethod
    def withdraw(self, value):
        ...


class CurrentAccount(Accounts):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print('Saldo insuficiente')
            return

        self.balance -= value
        self.details()


class SavingsAccount(Accounts):
    def withdraw(self, value):
        if self.balance < value:
            print('Saldo insuficiente')
            return

        self.balance -= value
        self.details()
