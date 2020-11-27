from random import sample
import time
import os
import re

while True:
    print('*-*'*21)
    print('                  Gerador de Senhas')
    print()
    print('Escolha como será a senha:')
    print('1 - Somente letras minúsculas - Fraco')
    print('2 - Somente letras maiúsculas - Fraco')
    print('3 - Letras maiúsculas e minúsculas  - Forte')
    print('4 - Letras maiúsculas, minúsculas e símbolos  - Recomendado')
    print('5 - SAIR')
    print('*-*'*21)
    print()
    opcao = ''
    try:
        opcao = int(input(''))
    except ValueError:
        while type(opcao) == str:
            opcao = input('Informe um valor inteiro (1 - 5): ')
            if re.match('^\d+$', opcao):
                opcao = int(opcao)
            elif re.match('^\d+\.\d+$', opcao):
                if opcao == float(opcao):
                    while opcao != int:
                        opcao = input('Informe um valor inteiro (1 - 5): ')

    while opcao < 1 or opcao > 5:
        try:
            opcao = int(input('Informe um valor inteiro (1 - 5): '))

        except ValueError:
            while type(opcao) == str:
                opcao = input('Informe um valor inteiro (1 - 5): ')
                if re.match('^\d+$', opcao):
                    opcao = int(opcao)
                elif re.match('^\d+\.\d+$', opcao):
                    if opcao == float(opcao):
                        while opcao != int:
                            opcao = input('Informe um valor inteiro (1 - 5): ')

    if opcao == 5:
        break
    tamanho_da_senha = ''
    try:
        tamanho_da_senha = int(input('Tamanho da senha: (5 - 10):'))
    except ValueError:
        while type(tamanho_da_senha) == str:
            tamanho_da_senha = input('Tamanho da senha: (5 - 10):')
            if re.match('^\d+$', tamanho_da_senha):
                tamanho_da_senha = int(tamanho_da_senha)
            elif re.match('^\d+\.\d+$', tamanho_da_senha):
                if tamanho_da_senha == float(tamanho_da_senha):
                    while tamanho_da_senha != int:
                        tamanho_da_senha = input('Tamanho da senha: (5 - 10):')

    while tamanho_da_senha < 1 or tamanho_da_senha > 10:
        try:
            tamanho_da_senha = int(input('Tamanho da senha: (5 - 10):'))
        except ValueError:
            while type(tamanho_da_senha) == str:
                tamanho_da_senha = input('Tamanho da senha: (5 - 10):')
                if re.match('^\d+$', tamanho_da_senha):
                    tamanho_da_senha = int(tamanho_da_senha)
                elif re.match('^\d+\.\d+$', tamanho_da_senha):
                    if tamanho_da_senha == float(tamanho_da_senha):
                        while tamanho_da_senha != int:
                            tamanho_da_senha = input(
                                'Tamanho da senha: (5 - 10):')
    if opcao == 1:
        minusculas = 'abcdefghijklmnopqrstuvxyz'
        senha_m = "".join(sample(minusculas, tamanho_da_senha))
        os.system('clear') or None
        print()
        print('<>'*10)
        print(f'\nSenha: {senha_m}')
        print('<>'*10)

    if opcao == 2:
        minusculas = 'abcdefghijklmnopqrstuvxyz'
        maiusculas = minusculas.upper() + minusculas
        senha_mu = "".join(sample(maiusculas, tamanho_da_senha))
        os.system('clear') or None
        print()
        print('<>'*10)
        print(f'\nSenha: {senha_mu}')
        print('<>'*10)

    if opcao == 3:
        minusculas = 'abcdefghijklmnopqrstuvxyz'
        maiusculas = minusculas.upper() + minusculas
        numeros = '0123456789' + maiusculas
        senha_nu = "".join(sample(numeros, tamanho_da_senha))
        os.system('clear') or None
        print()
        print('<>'*10)
        print(f'\nSenha: {senha_nu}')
        print('<>'*10)

    if opcao == 4:
        minusculas = 'abcdefghijklmnopqrstuvxyz'
        maiusculas = minusculas.upper() + minusculas
        numeros = '0123456789' + maiusculas
        simbolos = '@#$&*' + numeros
        senha_sm = "".join(sample(simbolos, tamanho_da_senha))
        os.system('clear') or None
        print()
        print('<>'*10)
        print(f'\nSenha: {senha_sm}')
        print('<>'*10)
