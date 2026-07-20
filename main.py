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
    print()
    print('-' * 40)


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


def solicitar_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print('Este campo precisa ser preenchido.')
            continue
        
        return valor


def solicitar_salario(mensagem):
    while True:
        try:
            valor = float(
                input(mensagem).strip().replace(',', '.')
            )
        except ValueError:
            print('Digite um salário válido.')
            continue

        if valor <= 0:
            print('O salário deve ser maior que zero.')
            continue
        
        return valor


def cadastrar_funcionario():
    print('\n--- Cadastro de funcionário ---')

    if not funcionarios:
        novo_id = 1
    else:
        ids_existentes = [
            funcionario['id']
            for funcionario in funcionarios
        ]
        novo_id = max(ids_existentes) + 1

    nome = solicitar_texto_obrigatorio('Nome: ')
    cpf = solicitar_texto_obrigatorio('CPF: ')
    cargo = solicitar_texto_obrigatorio('Cargo: ')
    setor = solicitar_texto_obrigatorio('Setor: ')
    salario = solicitar_salario('Salário: R$ ')

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


def atualizar_funcionario():
    print('\n--- Atualizar funcionário ---')

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
            print('\n--- Dados atuais ---')
            exibir_funcionario(funcionario)

            print('\n--- Insira os novos dados ---')
            print('Pressione ENTER para manter o valor atual.')

            novo_nome = input(
                f"Novo nome [{funcionario['nome']}]: "
            ).strip()

            novo_cargo = input(
                f"Novo cargo [{funcionario['cargo']}]: "
            ).strip()

            novo_setor = input(
                f"Novo setor [{funcionario['setor']}]: "
            ).strip()

            novo_salario = input(
                f"Novo salário [{funcionario['salario']:.2f}]: "
            ).strip()

            nome_final = novo_nome or funcionario['nome']
            cargo_final = novo_cargo or funcionario['cargo']
            setor_final = novo_setor or funcionario['setor']
            salario_final = funcionario['salario']

            if novo_salario:
                try:
                    salario_convertido = float(
                        novo_salario.replace(',', '.')
                    )
                except ValueError:
                    print('O salário deve ser um número valido.')
                    return
                
                if salario_convertido <= 0:
                    print('O salário deve ser maior que zero.')
                    return
                
                salario_final = salario_convertido
            
            funcionario['nome'] = nome_final
            funcionario['cargo'] = cargo_final
            funcionario['setor'] = setor_final
            funcionario['salario'] = salario_final         

            print('Funcionário atualizado com sucesso.')
            print()
            exibir_funcionario(funcionario)
            return        

    print('Funcionário não encontrado.')


def excluir_funcionario():
    print('\n--- Excluir funcionário ---')

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
            print()
            print(f"--- Deseja excluir o funcionário {funcionario['nome']}? ---")

            confirmacao = input(
                'Pressione ENTER para confirmar ou digite N para cancelar: '
            ).strip().lower()
            
            if confirmacao == 'n':
                print('Exclusão cancelada')
                return
            
            if confirmacao == '':
                funcionarios.remove(funcionario)
                print('\nFuncionario removido com sucesso!')
                return

            print('Opção de confirmação inválida.')
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
        atualizar_funcionario()
    elif opcao == '5':
        excluir_funcionario()
    elif opcao == '6':
        print('Opção Gerar relatórios selecionada.')
    elif opcao == '0':
        print('Opção Sair selecionada.')
        print('\nPrograma encerrado. Até breve!')
        break
    else:
        print('Opção inválida.')