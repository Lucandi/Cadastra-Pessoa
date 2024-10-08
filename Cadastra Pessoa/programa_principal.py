from Ex115.menu import menu
from Ex115.menu import leia_Inteiro
from time import sleep
from Ex115.docs import *
from Ex115.pessoas_cadastradas import ver_pessoas_cadastradas
from Ex115.cadastrar_pessoa import cadastrar

arq = 'pessoas.txt'

if not existeArquivo(arq):
    criarArquivo(arq)


def main():
    while True:
        menu()
        opcao = leia_Inteiro('\033[32mSua opção: \033[m')
        if opcao == 1:
            ver_pessoas_cadastradas(opcao)
            lerArquivo(arq)
        if opcao == 2:
            cadastrar(opcao, arq)
        if opcao > 3 or opcao <=0 :
            print(f'\033[1;31mErro! Informe um valor válido!\033[m')
            continue  # Volta para o laço
        if opcao == 3:
            print('-' * 40)
            print('          Saindo do Programa...')
            print('-' * 40)
            sleep(1)
            print('Obrigado ☻♥')
            break


main()



