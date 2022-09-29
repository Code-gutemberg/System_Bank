class Person:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password


class Client(Person):
    def __init__(self, name, age, password):
        super().__init__(name, age, password)
        self.account = None
        self._name = name

    def insert_account(self, account):
        self.account = account

    def name(self):
        self.name = self._name
