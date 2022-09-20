from query.bank import Bank
from time import sleep
import app.interface as interface
import app.treatment as treatment
import os

bank = Bank()


while True:
    interface.title('BANCO DIGITAL - GUTEMBANK')
    ag = input('Agencia: ')
    acc = input('Conta: ')
    pas = input('Senha: ')
    print('Checando banco de dados...')
    sleep(2)
    if bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] != 'root_':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        interface.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'Conta: {acc}')
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
    elif bank.auth(ag, acc, pas) and bank.auth(ag, acc, pas)[1] == 'root_':
        name = bank.auth(ag, acc, pas)[1]
        print('[SUCESS] - Usuário autenticado')
        interface.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            print(f'Usuário: {name}')
            print(f'Agencia: {ag}')
            print(f'Conta: {acc}')
            interface.title('BANCO DIGITAL - GUTEMBANK')
            interface.subtitle_adm()
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
