from Cadastra Pessoa.docs import *

def cadastrar(opc, nome):
    print('-' * 40)
    print('            CADASTRAR PESSOAS')
    print('-' * 40)
    while True:
        try:
            a = open(nome, 'at')
        except:
            print('Houve um erro na abertura do arquivo.')
        else:
            try:
                nome = str(input('Informe o seu nome: '))
                idade = int(input('Informe a sua idade: '))
                a.write(f'{nome}; {idade}\n')

            except (ValueError, TypeError):
                print('ERRO! Informe um valor válido! ')
            else:
                print(f'{nome} cadastrada(o) com sucesso! ')
                a.close()
                break

