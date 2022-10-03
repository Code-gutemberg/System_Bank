class Person:
    def __init__(self, name, cpf, password):
        self.name = name
        self.cpf = cpf
        self.password = password


class Client(Person):
    def __init__(self, name, cpf, password):
        super().__init__(name, cpf, password)
        self.account = None
        self._name = name

    def insert_account(self, account):
        self.account = account

    def name(self):
        self.name = self._name
