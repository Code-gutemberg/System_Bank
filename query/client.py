class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None
        self._name = name

    def insert_account(self, account):
        self.account = account

    def name(self):
        self.name = self._name
