import json


ARQUIVO_DADOS = 'funcionarios.json'


def salvar_funcionarios(funcionarios):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(
            funcionarios, 
            arquivo, 
            ensure_ascii=False, 
            indent=4,
        )


def carregar_funcionarios():
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print('O arquivo de dados está vazio ou inválido.')
        return []