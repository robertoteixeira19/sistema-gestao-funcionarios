funcionarios = []


def exibir_funcionario(funcionario):
    print(f"ID: {funcionario['id']}")
    print(f"NOME: {funcionario['nome']}")
    print(f"CPF: {funcionario['cpf']}")
    print(f"CARGO: {funcionario['cargo']}")
    print(f"SETOR: {funcionario['setor']}")
    print(f"SALÁRIO: R$ {funcionario['salario']:.2f}")
    if funcionario['ativo']:
        print('STATUS: Ativo')
    else:
        print('STATUS: Inativo')


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


def cadastrar_funcionario():
    print('\n--- Cadastro de funcionário ---')

    novo_id = len(funcionarios) + 1

    nome = input('Nome: ').strip()
    cpf = input('CPF: ').strip()
    cargo = input('Cargo: ').strip()
    setor = input('Setor: ').strip()
    salario = float(input('Salário: R$ ').replace(',', '.'))

    funcionario = {
        'id': novo_id,
        'nome': nome,
        'cpf': cpf,
        'cargo': cargo,
        'setor': setor,
        'salario': salario,
        'ativo': True,
    }

    funcionarios.append(funcionario)

    print(f'Funcionário {nome} cadastrado com sucesso!')


def listar_funcionarios():
    print('\n--- Funcionários cadastrados ---')

    if not funcionarios:
        print('Nenhum funcionário cadastrado.')
        return

    for funcionario in funcionarios:
        exibir_funcionario(funcionario)
        print('-' * 40)


def buscar_funcionario():
    print('\n--- Buscar funcionário ---')

    if not funcionarios:
        print('Nenhum funcionário cadastrado.')
        return
    
    try:
        id_busca = int(input('Digite o ID do funcionário: '))
    except ValueError:
        print('O ID deve ser um número inteiro.')
        return
    
    for funcionario in funcionarios:
        if funcionario['id'] == id_busca:
            exibir_funcionario(funcionario)
            return
    print('Funcionário não encontrado.')


while True:
    opcao = exibir_menu()
    if opcao == '1':
        cadastrar_funcionario()
    elif opcao == '2':
        listar_funcionarios()
    elif opcao == '3':
        buscar_funcionario()
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