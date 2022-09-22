import json
from query.bank import Bank
from query.client import Client, Person
from query.account import CurrentAccount as current
from query.account import SavingsAccount as savings
from random import randint
from time import sleep
import app.interface as face
import app.treatment as treat
import os

bank = Bank()


while True:
    face.title('BANCO DIGITAL - GUTEMBANK')
    ag = input('Agencia: ')
    acc = input('Conta: ')
    pas = input('Senha: ')
    print('Checando banco de dados...')
    sleep(1)
    if bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] != 'root_':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        face.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'Conta: {acc}')
            face.title('BANCO DIGITAL - GUTEMBANK')
            face.subtitle()
            menu_1 = treat.read_int('Digite o código correspondente: ')
            if menu_1 == 1:
                ...
            elif menu_1 == 2:
                ...
            elif menu_1 == 3:
                ...
            elif menu_1 == 4:
                face.title('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                sleep(2)
                os.system('cls')
                break
            else:
                face.error_code()
                sleep(2)
                os.system('cls')
                continue
    elif bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] == 'root_':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        face.title('INICIANDO SISTEMA')
        sleep(1)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'Conta: {acc}')
            face.title('BANCO DIGITAL - GUTEMBANK')
            face.subtitle_adm()
            menu_1 = treat.read_int('Digite o código correspondente: ')
            if menu_1 == 1:
                while True:
                    os.system('cls')
                    face.title('ADICIONAR CLIENTE [+]')
                    client_name = input('Nome: ')
                    client_age = int(input('Idade: '))
                    # instanciar o cliente
                    new_client = Client(client_name, client_age)
                    print('[1] Conta Poupança')
                    print('[2] Conta Corrente')
                    menu_2 = treat.read_int('Digite o código correspondente: ')
                    if menu_2 == 1:
                        new_number = str(randint(0, 100))
                        # instanciar a conta
                        new_acc = savings('0236', '0236'+new_number+'-1', 0)
                        # instanciar a conta para o cliente
                        new_client.insert_account(new_acc)
                        # instanciar o cliente e a conta ao banco
                        bank.insert_client(new_client)
                        bank.insert_account(new_acc)
                        info = Person(client_name, client_age)
                        acc = bank.accounts
                        a = json.dumps(bank.to_dict(info, acc), indent=4)
                        print(a)
                        bank.write_account(a)
                        input()
                        os.system('cls')
                        break
                    elif menu_2 == 2:
                        new_number = str(randint(0, 100))
                        # instanciar a conta
                        new_acc = current('0236', '0236'+new_number+'-0', 0)
                        # instanciar a conta para o cliente
                        new_client.insert_account(new_acc)
                        # instanciar o cliente e a conta ao banco
                        bank.insert_client(new_client)
                        bank.insert_account(new_acc)
                    else:
                        face.error_code()
                        sleep(1)
                        os.system('cls')
                        continue
            elif menu_1 == 2:
                os.system('cls')
                face.title('REMOVER CLIENTE [-]')
            elif menu_1 == 3:
                os.system('cls')
                face.title('CONSULTAR CLIENTE [...]')
            elif menu_1 == 4:
                face.title('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                sleep(1)
                os.system('cls')
                break
            else:
                face.error_code()
                sleep(1)
                os.system('cls')
                continue
    else:
        print('Usuario não existe')
        sleep(1)
        os.system('cls')
        continue
    break
'''

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


'''
