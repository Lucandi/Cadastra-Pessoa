from Cadastra Pessoa.pessoas_cadastradas import ver_pessoas_cadastradas
from Cadastra Pessoa.cadastrar_pessoa import cadastrar
from Cadastra Pessoa.docs import *
def menu():
    print('-' * 40)
    print('             MENU PRINCIPAL')
    print('-' * 40)
    print('''\033[1;33m 1 - \033[34mVer pessoas cadastradas
 \033[1;33m2 -\033[m \033[1;34mCadastrar novas pessoas
 \033[1;33m3 - \033[m\033[1;34mSair do programa\033[m''')
    print('-' * 40)


def leia_Inteiro(msg):
    while True:

        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro! Informe um valor inteiro de 1 até 3 válido!\033[m')
            continue  # Volta para o laço
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu por não informar os dados.\033[m')
            return 0
        else:
            return num





