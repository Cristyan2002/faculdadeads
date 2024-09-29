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
                print('(3) - Excluir')
                print('(4) - Editar Usuário')
                print('(5) - Voltar ao Menu Principal')
# Criando a funçao de Incluir os Cadastros:
def incluir_cadastros(salvar):
    escolha_texto2 = '(1) - Incluir'
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(salvar)
    codigo = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    cpf = int(input('Por favor digite o CPF: '))
    #Criando um dicionário para armazenar as informações e separá-las
    dados_cadastros = {
    'Codigo' : codigo,
    'Nome' : nome,
    'CPF' : cpf
    }
    listas_cadastros.append(dados_cadastros)
    print('Pronto, você está Incluído na Lista!.')
    sleep(2)
    salvar_arquivo(listas_cadastros, salvar)
# Criando a função de mostrar as listas dos cadastros, que foram cadastrados:
def lista_dos_cadastrados(salvar):
    listas_cadastros = ler_arquivo(salvar)
    escolha_texto2 = '(2) - Listar'
    print(f'Você escolheu a opção: {escolha_texto2}')
    if len(listas_cadastros) == 0:
       print('Não ninguém cadastrados!.')
       sleep(2)
    else:
        for lista in listas_cadastros:
          print('Os cadastrados são:\n{}'.format(listas_cadastros))
          sleep(2)
          break
# Criando a função de excluir os Cadastros através do código.
def excluir_cadastros(salvar, arquivo_estudante):
    escolha_texto2 = '(3) - Excluir'
    listas_cadastros = ler_arquivo(arquivo_estudante)
    print(f'Você escolheu a opção: {escolha_texto2}')
    if len(listas_cadastros) == 0:
        print('Nâo há nenhum código cadastrado!.')
        sleep(2)
    else: 
        codigo = int(input('Qual o código que deseja remover? '))

        cadastros_excluir = None
        for dados_cadastros in listas_cadastros:
            if dados_cadastros['Codigo'] == codigo:
                cadastros_excluir = dados_cadastros
                break
        if cadastros_excluir is not None:
            listas_cadastros.remove(cadastros_excluir)
            salvar_arquivo(listas_cadastros, arquivo_estudante)
            print('Código removido com sucesso!')
            sleep(2)
        else:
            print('Código não encontrado!.')
            sleep(2)
         
    
# Criando a função de editar um Estudante através do seu código.
def editar_cadastros(arquivo_estudante, salvar):
    escolha_texto2 = ('(4) - Editar Usuário')
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(arquivo_estudante)
    
    if len(listas_cadastros) == 0:
        print('Não há nenhum código cadastrado.')
        sleep(2)
        return
    codigo_editor = int(input('Qual o código que deseja editar ?'))
    for editor_cadastros in listas_cadastros:
        if editor_cadastros ['Codigo'] == codigo_editor:
            editor_cadastros['Codigo'] = int(input('Digite um novo Código: '))
            editor_cadastros['Nome'] = input('Digite um novo Nome: ')
            editor_cadastros['CPF'] = input('Digite um novo CPF: ')
            salvar_arquivo(listas_cadastros, salvar)
            print('Edição concluída com sucesso!')
            sleep(2)
            return
        
    print('Código não encontrado.')
    sleep(2)
def incluir_cadastro2(salvar):
    escolha_texto2 = '(1) - Incluir'
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(salvar)
    codigo = int(input('Digite seu código: '))
    nome = input('Digite seu nome: ')
    #Criando um dicionário para armazenar as informações e separá-las
    dados_cadastros = {
    'Codigo' : codigo,
    'Nome' : nome,
    }
    listas_cadastros.append(dados_cadastros)
    print('Pronto, você está Incluído na Lista!.')
    sleep(2)
    salvar_arquivo(listas_cadastros, salvar)
def editar_cadastros2(arquivo_estudante, salvar):
    escolha_texto2 = ('(4) - Editar Usuário')
    print(f'Você escolheu a opção: {escolha_texto2}')
    listas_cadastros = ler_arquivo(arquivo_estudante)
    
    if len(listas_cadastros) == 0:
        print('Não há nenhum código cadastrado.')
        sleep(2)
        return
    codigo_editor = int(input('Qual o código que deseja editar ?'))
    for editor_cadastros in listas_cadastros:
        if editor_cadastros ['Codigo'] == codigo_editor:
            editor_cadastros['Codigo'] = int(input('Digite um novo Código: '))
            editor_cadastros['Nome'] = input('Digite um novo Nome: ')
            salvar_arquivo(listas_cadastros, salvar)
            print('Edição concluída com sucesso!')
            sleep(2)
            return
    print('Código não encontrado.')
    sleep(2)
    
    
    
def menu_de_operacoes_terciario(escolha, salvar, pessoa):
    if escolha2 >= 1 and escolha <= 6:
        if escolha2 == 1:
            if pessoa:
                incluir_cadastros(salvar)
            else:
                incluir_cadastro2(salvar)
        elif escolha2 == 2:
            lista_dos_cadastrados(salvar)
        elif escolha2 == 3:
            excluir_cadastros(arquivo_estudante, salvar)
        elif escolha2 == 4:
            if pessoa:
                editar_cadastros(arquivo_estudante, salvar)
            else:
                editar_cadastros2(arquivo_estudante, salvar)
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
arquivo_disciplina = 'disciplina.json'
arquivo_matriculas = 'matriculas.json'
arquivo_turmas = 'turmas.json'
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
                pessoa = True
                if not menu_de_operacoes_terciario(escolha2, arquivo_estudante, pessoa):
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
                    
                pessoa = True
                if not menu_de_operacoes_terciario(escolha2, arquivo_professor, pessoa):
                    break
        elif escolha == 3:
            escolha_texto = '(3) - Gerenciar Disciplinas'
            while True:
                menu_de_operacoes_secundario()
                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue
                pessoa = False
                if not menu_de_operacoes_terciario(escolha2, arquivo_disciplina, pessoa):
                    break
        elif escolha == 4:
            escolha_texto = '(4) - Gerenciar Matrículas'
            while True:
                menu_de_operacoes_secundario()
                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue
                pessoa = False
                if not menu_de_operacoes_terciario(escolha2, arquivo_matriculas, pessoa):
                    break
        elif escolha == 5:
            escolha_texto = '(5) - Gerenciar Turmas'
            while True:
                menu_de_operacoes_secundario()
                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue
                pessoa = False
                if not menu_de_operacoes_terciario(escolha2, arquivo_turmas, pessoa):
                    break

    # Opções se o usuário escrever algo inválido ou resolver sair #
    elif escolha == 6:
        print('Você escolheu a opção: (6) - Sair ')
        print('Saindo...')
        sleep(2)
        break
    else:
        print('Você escolheu uma opção inválida!.')
        sleep(2)
