class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


# Herança simples
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
        self._nome = nome

    def inserir_conta(self, conta):
        self.conta = conta

    def nome(self):
        print(self._nome)
