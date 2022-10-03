from query.bank import Bank
from query.client import Client, Person
from query.account import Accounts, CurrentAccount as current
from query.account import SavingsAccount as savings
from random import randint
from time import sleep
import app.interface as face
import app.treatment as treat
import os
import json

bank = Bank()

while True:
    face.title('BANCO DIGITAL - GUTEMBANK')
    ag = input('Agencia: ')
    acc = input('Conta: ')
    pas = input('Senha: ')
    try:
        if acc[-1] == '1':
            type_acc = 'Conta Poupança'
        elif acc[-1] == '0':
            type_acc = 'Conta Corrente'
        elif acc == ' ':
            type_acc = 'Super Usuário'
    except Exception:
        acc = ''
    print('Checando banco de dados...')
    sleep(1)
    # Cliente
    if bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] != 'root':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        face.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'{type_acc}: {acc}')
            face.title('BANCO DIGITAL - GUTEMBANK')
            face.subtitle()
            menu_1 = treat.read_int('Digite o código correspondente: ')
            if menu_1 == 1:
                os.system('cls')
                print(f'Usuário: {name}')
                print(f'Agencia: {ag}')
                print(f'{type_acc}: {acc}')
                face.title('SACAR VALOR [-]')
                withdraw = treat.read_coin('Digite o valor do saque: R$ ')
                if type_acc == 'Conta Poupança':
                    savings.withdraw(name, withdraw)
                    if savings.withdraw(name, withdraw) is False:
                        face.title('SALDO INSUFICIENTE')
                        sleep(2)
                        os.system('cls')
                        continue
                    elif savings.withdraw(name, withdraw):
                        face.title(f'VALOR DO SAQUE: R$ {withdraw}')
                        copy_db = bank.copy_db()
                        update_db = savings.update(name, copy_db, withdraw)
                        json_file = json.dumps(update_db, indent=4)
                        bank.write_account(json_file)
                        sleep(2)
                        os.system('cls')
                        continue
                elif type_acc == 'Conta Corrente':
                    current.withdraw(name, withdraw)
                    if current.withdraw(name, withdraw) is False:
                        face.title('SALDO INSUFICIENTE')
                        sleep(2)
                        os.system('cls')
                        continue
                    elif current.withdraw(name, withdraw):
                        face.title(f'VALOR DO SAQUE: R$ {withdraw}')
                        copy_db = bank.copy_db()
                        update_db = current.update(name, copy_db, withdraw)
                        json_file = json.dumps(update_db, indent=4)
                        bank.write_account(json_file)
                        sleep(2)
                        os.system('cls')
                        continue
            elif menu_1 == 2:
                os.system('cls')
                print(f'Usuário: {name}')
                print(f'Agencia: {ag}')
                print(f'{type_acc}: {acc}')
                face.title('DEPOSITAR VALOR [+]')
                deposit = treat.read_coin('Digite o valor do depósito: R$ ')
                if type_acc == 'Conta Poupança':
                    copy_db = bank.copy_db()
                    update_db = savings.deposit(name, copy_db, deposit)
                    json_file = json.dumps(update_db, indent=4)
                    bank.write_account(json_file)
                    face.title(f'VALOR DO DEPÓSITO: R$ {deposit}')
                    sleep(2)
                    os.system('cls')
                    continue
                elif type_acc == 'Conta Corrente':
                    copy_db = bank.copy_db()
                    update_db = current.deposit(name, copy_db, deposit)
                    json_file = json.dumps(update_db, indent=4)
                    bank.write_account(json_file)
                    face.title(f'VALOR DO DEPÓSITO: R$ {deposit}')
                    sleep(2)
                    os.system('cls')
                    continue
            elif menu_1 == 3:
                os.system('cls')
                print(f'Usuário: {name}')
                print(f'Agencia: {ag}')
                print(f'{type_acc}: {acc}')
                face.title('CONSULTAR SALDO [...]')
                copy_db = bank.copy_db()
                Accounts.details(name, copy_db)
                os.system('cls')
                continue
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
    # Administrador
    elif bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] == 'root':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        face.title('INICIANDO SISTEMA')
        sleep(1)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'{type_acc}: {acc}')
            face.title('BANCO DIGITAL - GUTEMBANK')
            face.subtitle_adm()
            menu_1 = treat.read_int('Digite o código correspondente: ')
            if menu_1 == 1:
                while True:
                    os.system('cls')
                    print(f'Usuário: {name}')
                    print(f'Agencia: {ag}')
                    print(f'{type_acc}: {acc}')
                    face.title('ADICIONAR CLIENTE [+]')
                    client_name = treat.read_name('Nome: ')
                    client_cpf = treat.read_cpf('CPF: ')
                    client_pass = input('Senha: ')
                    # instanciar o cliente
                    new_client = Client(client_name, client_cpf, client_pass)
                    print('[1] Conta Poupança')
                    print('[2] Conta Corrente')
                    menu_2 = treat.read_int('Digite o código correspondente: ')
                    if menu_2 == 1:
                        # Gera número aleatório da conta
                        new_number = str(randint(0, 100))
                        # instancia a conta
                        new_acc = savings('0236', '0236'+new_number+'-1', 0)
                        # instancia a conta para o cliente
                        new_client.insert_account(new_acc)
                        # instancia o cliente e a conta ao banco
                        bank.insert_client(new_client)
                        bank.insert_account(new_acc)
                        info = Person(client_name, client_cpf, client_pass)
                        saving_acc = bank.accounts
                        copy_db = bank.copy_db()
                        full_profile = bank.to_dict(info, saving_acc)
                        join_dicts = {**copy_db, **full_profile}
                        json_file = json.dumps(join_dicts, indent=4)
                        bank.write_account(json_file)
                        os.system('cls')
                        break
                    elif menu_2 == 2:
                        # Gera número aleatório da conta
                        new_number = str(randint(0, 100))
                        # instancia a conta
                        new_acc = current('0236', '0236'+new_number+'-0', 0)
                        # instancia a conta para o cliente
                        new_client.insert_account(new_acc)
                        # instancia o cliente e a conta ao banco
                        bank.insert_client(new_client)
                        bank.insert_account(new_acc)
                        info = Person(client_name, client_cpf, client_pass)
                        current_acc = bank.accounts
                        copy_db = bank.copy_db()
                        full_profile = bank.to_dict(info, current_acc)
                        join_dicts = {**copy_db, **full_profile}
                        json_file = json.dumps(join_dicts, indent=4)
                        bank.write_account(json_file)
                        os.system('cls')
                        break
                    else:
                        face.error_code()
                        sleep(1)
                        os.system('cls')
                        continue
            elif menu_1 == 2:
                os.system('cls')
                print(f'Usuário: {name}')
                print(f'Agencia: {ag}')
                print(f'{type_acc}: {acc}')
                face.title('REMOVER CLIENTE [-]')
                entry = input('Digite o nome do cliente: ')
                copy_db = bank.copy_db()
                update_db = bank.remove_account(copy_db, entry)
                json_file = json.dumps(update_db, indent=4)
                bank.write_account(json_file)
                sleep(2)
                os.system('cls')
                continue
            elif menu_1 == 3:
                os.system('cls')
                print(f'Usuário: {name}')
                print(f'Agencia: {ag}')
                print(f'{type_acc}: {acc}')
                face.title('CONSULTAR CLIENTE [...]')
                entry = input('Digite o nome do cliente: ')
                copy_db = bank.copy_db()
                if Accounts.details(entry, copy_db) is False:
                    face.title('USUÁRIO INEXISTENTE')
                    sleep(2)
                    os.system('cls')
                    continue
                os.system('cls')
                continue
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
        print('Usuario não existe ou senha incorreta')
        sleep(2)
        os.system('cls')
        continue
    break
