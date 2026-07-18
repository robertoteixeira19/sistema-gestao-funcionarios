def exibir_menu():
    print('\n--- Sistema de Gestão de Funcionários ---')
    print('1 - Cadastrar funcionário')
    print('2 - Listar funcionários')
    print('3 - Buscar funcionário')
    print('4 - Atualizar funcionário')
    print('5 - Excluir funcionário')
    print('6 - Gerar relatórios')
    print('0 - Sair')
    opcao = input('Digite a opção desejada: ').strip()
    return opcao


while True:
    opcao = exibir_menu()
    if opcao == '1':
        print('Opção Cadastrar funcionário selecionada.')
    elif opcao == '2':
        print('Opção Listar funcionários selecionada.')
    elif opcao == '3':
        print('Opção Buscar funcionário selecionada.')
    elif opcao == '4':
        print('Opção Atualizar funcionário selecionada.')
    elif opcao == '5':
        print('Opção Excluir funcionário selecionada.')
    elif opcao == '6':
        print('Opção Gerar relatórios selecionada.')
    elif opcao == '0':
        print('Opção Sair selecionada.')
        print('\nPrograma encerrado. Até breve!')
        break
    else:
        print('Opção inválida.')