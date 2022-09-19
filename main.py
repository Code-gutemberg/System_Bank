from query.bank import Bank
from query.client import Cliente
from query.account import ContaCorrente, ContaPoupanca
from time import sleep
import app.interface as interface
import app.treatment as treatment
import os

bank = Bank()

while True:
    interface.title('BANCO DIGITAL - GUTEMBANK')
    interface.subtitle()
    menu = treatment.read_int('Digite o código correspondente: ')
    if menu == 1:
        ...
    elif menu == 2:
        ...
    elif menu == 3:
        ...
    elif menu == 4:
        interface.title('[!] PROGRAMA ENCERRADO COM SUCESSO!')
        sleep(2)
        os.system('cls')
        break
    else:
        interface.error_code()
        sleep(2)
        os.system('cls')
        continue
'''

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
'''
