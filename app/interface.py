def title(msg):
    print('=' * 50)
    print(msg.center(50))
    print('=' * 50)


def subtitle():
    menu = dict()
    menu[1] = 'Sacar Valor \t[ - ]'
    menu[2] = 'Depositar Valor \t[ + ]'
    menu[3] = 'Consultar Saldo\t[...]'
    menu[4] = 'Sair do Sistema \t[ ! ]'
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def subtitle_adm():
    menu = dict()
    menu[1] = 'Adicionar Cliente \t[ + ]'
    menu[2] = 'Remover Cliente \t[ - ]'
    menu[3] = 'Consultar Cliente \t[...]'
    menu[4] = 'Sair do Sistema \t[ ! ]'
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def error_code():
    print('[ERROR] - Digite um número válido.')


def Real(price, coin='R$'):     # Formata para Real BR.
    return f'{coin} {price:.2f}'.replace(".", ",")
