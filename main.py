from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


# Instanciando o banco
banco = Banco()

# Instanciando os clientes
cliente1 = Cliente('Alex', 30)
cliente2 = Cliente('Delis', 25)
cliente3 = Cliente('Fabricio', 45)

# Instanciando as contas
conta1 = ContaCorrente('12345', '0001-01', 0)
conta2 = ContaPoupanca('56789', '0002-02', 0)
conta3 = ContaCorrente('09888', '03102-02', 0)

# Instanciando as contas aos clientes
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

# Inserindo o cliente1 e a conta1 no banco
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

print('=' * 20)
# Verificando se o cliente/conta/agencia existe dentro do banco
if banco.autenticar(cliente1):
    cliente1.nome()
    cliente1.conta.depositar(40)
else:
    print('cliente não autenticado')
print('=' * 20)
# Verificando se o cliente/conta/agencia existe dentro do banco
if banco.autenticar(cliente2):
    cliente2.nome()
    cliente2.conta.depositar(40)
else:
    print('cliente não autenticado')
print('=' * 20)
