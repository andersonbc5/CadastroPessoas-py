def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('\033[31mMENU PRINCIPAL \033[m')
    c=1
    for item in lista:
        print(f'\033[31m{c}\033[m - \033[32m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[31mSua Opção:\033[m ')
    return opc

