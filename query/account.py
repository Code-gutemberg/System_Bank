from abc import ABC, abstractmethod


# classe abstrata
class Accounts(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('valor do depósito precisa ser numérico')

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        ...


# Henrança Simples
class ContaCorrente(Accounts):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()


# Henrança Simples
class ContaPoupanca(Accounts):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
