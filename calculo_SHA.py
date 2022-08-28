import hashlib

opcoes_menu = {
    1: 'SHA-256',
    2: 'SHA-384',
    3: 'SHA-512',
    4: 'Sair',
}

def print_menu():
    for key in opcoes_menu.keys():
        print(key, '--', opcoes_menu[key] )


if __name__ == '__main__':
    str = input('Qual a string para o hash?\n')
    while(True):
        print_menu()
        opcao = ''

        try:
            opcao = int(input('Digite sua escolha: '))
        except: 
            print('Opção inválida. Favor escolher outra opção.')
        
        match opcao:
            case 1:
                print('O resultado do hash é:')
                print(hashlib.sha256(str.encode()).hexdigest())
            case 2:
                print('O resultado do hash é:')
                print(hashlib.sha384(str.encode()).hexdigest())
            case 3:
                print('O resultado do hash é:')
                print(hashlib.sha512(str.encode()).hexdigest())
            case 4:
                print('Retornando ao menu.')
                exit()
            case _ :
                print('Não foi possível calcular o hash.')





        



