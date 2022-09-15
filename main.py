from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


"""
# Criar um sistema bancario que tem clientes, contas, e um banco. A ideia
# é que o cliente tenha uma conta (poupança/corrente) e que  possa
# sacar/depositar
# Conta corrente tem um limite extra; Banco tem clientes e contas

# Dicas:

# Criar classe cliente que herda da classe Pessoa (herança)  =  OK
    # Pessoa tem nome e idade ( com getters)                 =  OK
    # cliente tem conta (agregação da classe CC e CP)        =  OK
# Criar Classes CP e CC que herdam de Conta                   = OK
    # CC deve ter limite extra                                = OK
    # Contas tem agencia, numero e saldo                      = OK
    # conta tem que ter metodo de deposito                    = OK
    # conta (super Classe) deve ter metodo sacar abstrato     = OK
# Criar classe banco para AGREGAR classes clientes e contas (agregação)
# Banco sera responsavel autenticar o cliente e as contas da seguinte maneira:
    # Banco tem contas e clientes (agregação)
    # Checar se a agencia é daquele banco
    # Checar se o cliente é daquele banco
    # Checar se a conta é daquele banco
# Só será possivel sacar se passar na autenticacao do banco
"""

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
