import json
# Criando a função do Menu de operações:
def menu_de_operacoes():
    print('-' * 10, 'Olá, Bem vindo ao Menu Principal', '-' * 10)
    print('(1) - Gerenciar Estudantes ')
    print('(2) - Gerenciar Professores')
    print('(3) - Gerenciar Disciplinas')
    print('(4) - Gerenciar Matrículas ')
    print('(5) - Gerenciar Turmas ')
    print('(6) - Sair')
# Criando a função do Segundo menu:
def menu_de_operacoes_secundario():
                print('-' * 10, f'{escolha_texto} : Menu de Operações', '-' * 10)
                print('(1) - Incluir')
                print('(2) - Listar')
                print('(3) - Exluir')
                print('(4) - Editar Usuário')
                print('(5) - Voltar ao Menu Principal')
# Criando a funçao de Incluir (Cadastrar) os Estudantes:
def incluir_estudantes(salvar):
    escolha_texto2 = '(1) - Incluir'
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(salvar)
    codigo = int(input('Digite o código do Estudante: '))
    nome_estudantes = input('Digite o nome do Aluno: ')
    cpf = int(input('Por favor digite o CPF: '))
    #Criando um dicionário para armazenar as informações e separá-las
    dados_estudantes = {
    'codigo_estudante' : codigo,
    'nome_estudante' : nome_estudantes,
    'cpf_estudante' : cpf
    }
    listas_cadastros.append(dados_estudantes)
    print('Pronto, você está Incluído na Lista!.')
    sleep(2)
    salvar_arquivo(listas_cadastros, salvar)
# Criando a função de mostrar as listas dos Estudantes, que foram cadastrados:
def lista_dos_estudantes(salvar):
    listas_cadastros = ler_arquivo(salvar)
    escolha_texto2 = '(2) - Listar'
    print(f'Você escolheu a opção: {escolha_texto2}')
    if len (listas_cadastros) == 0:
       print('Não há Estudantes Cadastrados!.')
    else:
        for lista in listas_cadastros:
          print('Os estudantes cadastrados são:\n{}'.format(listas_cadastros))
          sleep(2)
          break
# Criando a função de excluir os Estudantes através do código.
def excluir_estudantes(salvar):
    escolha_texto2 = '(3) - Excluir'
    print(f'Você escolheu a opção: {escolha_texto2}')
    codigo_estudante = int(input('Qual o código do aluno que deseja remover? '))
    estudante_excluir = None
    for dados_estudantes in codigo_estudante:
      if dados_estudantes['codigo_estudante'] == codigo_estudante:
         estudante_excluir = dados_estudantes
         print('Removendo só um instante....')
         sleep(2)
         print('Removido com sucesso!.')
         break
      if estudante_excluir == None:
         print('Não entendi esse código, de uma olhadinha nos alunos cadastrados.')
         sleep(2)
         print(listas_cadastros)
         break
    listas_cadastros = ler_arquivo(arquivo_estudante)
    listas_cadastros.remove(estudante_excluir)
    salvar_arquivo(listas_cadastros, salvar)
    
# Criando a função de editar um Estudante através do seu código.
def editar_estudantes(salvar):
    escolha_texto2 = ('(4) - Editar Usuário')
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(salvar)
    if len(listas_cadastros) == 0:
            print('Nenhum estudantes está cadastrado.')
            sleep(2)
    else:
        codigo_estudante = int(input('Qual o código do aluno que deseja editar ?'))
        estudante_editar = None
        for editor_estudante in listas_cadastros:
            if editor_estudante['codigo_estudante'] == codigo_estudante:
                estudante_editar = editor_estudante
            if estudante_editar == None:
                print('Não achei nenhum usuário com esse código.')
                sleep(2)
                break
            else:
                estudante_editar['codigo_estudante'] = int(input('Digite um novo Código: '))
                estudante_editar['nome_estudante'] = int(input('Digite um novo Nome: '))
                estudante_editar['cpf_estudante'] = int(input('Digite um novo CPF: '))
                salvar_arquivo(listas_cadastros, salvar)
                print('Edição concluída com sucesso!')
                sleep(2)
def menu_de_operacoes_estudante(escolha, salvar):
    if escolha2 >= 1 and escolha <= 6:
        if escolha2 == 1:
            incluir_estudantes(salvar)
        elif escolha2 == 2:
            lista_dos_estudantes(salvar)
        elif escolha2 == 3:
            excluir_estudantes(salvar)
        elif escolha2 == 4:
            editar_estudantes(salvar)
        elif escolha2 == 5:
            print('Você escolheu a opção: Voltar ao Menu Principal')
            print('Voltando...')
            sleep(2)
            return False
    else:
        print('Você digitou uma opção inválida!.')
        sleep(2)
    return True
        


#Criando um arquivo para salvar JSON.
def salvar_arquivo(listas_cadastros, salvar):
    with open(salvar, 'w') as open_file:
        json.dump(listas_cadastros, open_file)

#Para ler a lista em JSON.
def ler_arquivo(salvar):
    try:
        with open(salvar, 'r') as open_file:
            listas_cadastros = json.load(open_file)
        return listas_cadastros
    except:
        return []
# Vou importar o sleep para o programa ficar um pouco mais dinâmico!
from time import sleep
#Lista para cada estudante adicionado!
arquivo_estudante = 'estudantes.json'
arquivo_professor = 'professor.json'
while True:
    menu_de_operacoes()
    # O Usuário irá selecionar a opção desejada, e consequentemente, irá para tela do menu de operações. #
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print('Você inseriu uma letra ou caractere, digite novamente:')
        sleep(2)
        continue
    if escolha >= 1 and escolha <= 5:
        if escolha == 1:
            print('Carregando...')
            sleep(2)

            escolha_texto = '(1) - Gerenciar Estudantes'
            while True:
                menu_de_operacoes_secundario()
                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue
                if not menu_de_operacoes_estudante(escolha2, arquivo_estudante):
                    break
        elif escolha == 2:
            escolha_texto = '(2) - Gerenciar Professores'
            while True:
                menu_de_operacoes_secundario()
                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue
                if not menu_de_operacoes_estudante(escolha2, arquivo_professor):
                    break
        elif escolha == 3:
            escolha_texto = '(3) - Gerenciar Disciplinas'
            menu_de_operacoes_estudante(escolha, arquivo_professor)
        elif escolha == 4:
            escolha_texto = '(4) - Gerenciar Matrículas'
            menu_de_operacoes_estudante(escolha, arquivo_professor)
        elif escolha == 5:
            escolha_texto = '(5) - Gerenciar Turmas'
            menu_de_operacoes_estudante(escolha, arquivo_professor)

    # Opções se o usuário escrever algo inválido ou resolver sair #
    elif escolha == 6:
        print('Você escolheu a opção: (6) - Sair ')
        print('Saindo...')
        sleep(2)
        break
    else:
        print('Você escolheu uma opção inválida!.')
        sleep(2)
