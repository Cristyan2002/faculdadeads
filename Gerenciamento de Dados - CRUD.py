# Vou importar o sleep para o programa ficar um pouco mais dinâmico!
from time import sleep
#Lista para cada estudante adicionado!
estudantes = []
while True:
    # Desenvolvimento do Menu Principal #
    print('-' * 10, 'Olá, Bem vindo ao Menu Principal', '-' * 10)
    print('(1) - Gerenciar Estudantes ')
    print('(2) - Gerenciar Professores')
    print('(3) - Gerenciar Disciplinas')
    print('(4) - Gerenciar Matrículas ')
    print('(5) - Gerenciar Turmas ')
    print('(6) - Sair')

    # O Usuário irá selecionar a opção desejada, e consequentemente, irá para tela do menu de operações. #
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print('Você inseriu uma letra ou caractere, digite novamente:')
        sleep(2)
        continue
    # Caminhos para ao qual o usuário escolher #
    if escolha >= 1 and escolha <= 5:
        if escolha == 1:
            print('Carregando...')
            sleep(2)

            escolha_texto = '(1) - Gerenciar Estudantes'
            while True:
                # A Opção do usuário irá aparecer aqui no menu de operações #

                print('-' * 10, f'{escolha_texto} : Menu de Operações', '-' * 10)
                print('(1) - Incluir')
                print('(2) - Listar')
                print('(3) - Atualizar')
                print('(4) - Exluir')
                print('(5) - Voltar ao Menu Principal')
                # O Usuário escolherá uma opção #

                try:
                    escolha2 = int(input('Escolha uma opção: '))
                except ValueError:
                    print('Você inseriu uma letra ou caractere, digite novamente:.')
                    sleep(2)
                    continue

                if escolha2 >= 1 and escolha <= 5:
                    if escolha2 == 1:
                        escolha_texto2 = '(1) - Incluir'
                        print(f'Você escolheu a opção: {escolha_texto2}')
                        codigo = int(input('Digite o código do Estudante: '))
                        nome_estudantes = input('Digite o nome do Aluno: ')
                        cpf = int(input('Por favor digite o CPF: '))
                        #Criando um dicionário para armazenar as informações e separá-las
                        dados_estudantes = {
                            'codigo_estudante' : codigo,
                            'nome_estudante' : nome_estudantes,
                            'cpf_estudante' : cpf
                        }
                        estudantes.append(dados_estudantes)
                        print('Pronto, você está Incluído na Lista!.')
                        sleep(2)
                    elif escolha2 == 2:
                        escolha_texto2 = '(2) - Listar'
                        print(f'Você escolheu a opção: {escolha_texto2}')
                        if len (estudantes) == 0:
                            print('Não há Estudantes Cadastrados!.')
                        else:
                            for lista in estudantes:
                                print('Os estudantes cadastrados são:\n{}'.format(estudantes))
                                sleep(2)
                                break

                    elif escolha2 == 3:
                        escolha_texto2 = '(3) - Atualizar'
                        print('Desculpe, esta função está em desenvolvimento...!')
                        sleep(2)
                    elif escolha2 == 4:
                        escolha_texto2 = '(4) - Excluir'
                        codigo_estudante = int(input('Qual o código do aluno que deseja remover? '))
                        estudante_excluir = None
                        for dados_estudantes in estudantes:
                            if dados_estudantes['codigo_estudante'] == codigo_estudante:
                                estudante_excluir = dados_estudantes
                                print('Removendo só um instante....')
                                sleep(2)
                                print('Removido com sucesso!.')
                                break
                            if estudante_excluir == None:
                                print('Não entendi esse código, de uma olhadinha nos alunos cadastrados.')
                                sleep(2)
                                print(estudantes)
                        estudantes.remove(estudante_excluir)
                    
                    elif escolha2 == 5:
                        print('Você escolheu a opção: Voltar ao Menu Principal')
                        print('Voltando...')
                        sleep(2)
                        break
                    else:
                        print('Você digitou uma opção inválida!.')
                        sleep(2)
                        continue
        elif escolha == 2:
            escolha_texto = '(2) - Gerenciar Professores'
            print('Desculpe, esta função está em desenvolvimento...!')
            sleep(2)
        elif escolha == 3:
            escolha_texto = '(3) - Gerenciar Disciplinas'
            print('Desculpe, esta função está em desenvolvimento...!')
            sleep(2)
        elif escolha == 4:
            escolha_texto = '(4) - Gerenciar Matrículas'
            print('Desculpe, esta função está em desenvolvimento...!')
            sleep(2)
        elif escolha == 5:
            escolha_texto = '(5) - Gerenciar Turmas'
            print('Desculpe, esta função está em desenvolvimento...!')
            sleep(2)

    # Opções se o usuário escrever algo inválido ou resolver sair #
    elif escolha == 6:
        print('Você escolheu a opção: (6) - Sair ')
        print('Saindo...')
        sleep(2)
        break
    else:
        print('Você escolheu uma opção inválida!.')
        sleep(2)
