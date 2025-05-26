from interface import  *
from arquivo import *

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['\033[1mVer pessoas cadastradas\033[0m', '\033[1mCadastrar Pessoas\033[0m', '\033[1mSair do Sistema\033[0m'])
    if resposta == 1:
        # Opçao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema....')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
