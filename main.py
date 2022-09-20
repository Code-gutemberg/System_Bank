from query.bank import Bank
from time import sleep
import app.interface as interface
import app.treatment as treatment
import os
bank = Bank()

while True:
    interface.title('BANCO DIGITAL - GUTEMBANK')
    agency = input('Agencia: ')
    account = input('Conta: ')
    password = input('Senha: ')
    print('Checando banco de dados...')
    sleep(2)
    if bank.auth(agency, account, password):
        name = bank.auth(agency, account, password)[1]
        print('[SUCESS] - Usuário autenticado Logado')
        interface.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {agency}')
            print(f'Conta: {account}')
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
    else:
        print('Usuario não existe')
        sleep(2)
        os.system('cls')
        continue
    break
'''

# Instanciando as contas aos clientes
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

# Inserindo o cliente1 e a conta1 no banco
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

'''
