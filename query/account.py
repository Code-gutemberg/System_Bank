from abc import ABC, abstractmethod


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
