# Sistema de Gestão de Funcionários

## Descrição

Projeto desenvolvido em Python para praticar organização de código, gerenciamento de funcionários, persistência de dados e geração de relatórios.

## Funcionalidades

- Cadastrar funcionários;
- Listar funcionários;
- Buscar funcionário pelo ID;
- Atualizar dados de um funcionário;
- Excluir funcionários;
- Ativar e inativar funcionários;
- Gerar relatórios de funcionários;
- Calcular a folha salarial e a média salarial;
- Salvar e carregar os dados em um arquivo JSON.

## Tecnologias utilizadas

- Python;
- JSON;
- Git;
- GitHub;
- Visual Studio Code.

## Como executar o projeto

1. Tenha o Python 3 instalado no computador.
2. Clone o repositório:

```bash
git clone https://github.com/robertoteixeira19/sistema-gestao-funcionarios.git
```

## Estrutura dos dados

Cada funcionário é armazenado em um dicionário com as seguintes informações:

* ID;
* Nome;
* CPF;
* Cargo;
* Setor;
* Salário;
* Status ativo ou inativo.

Os funcionários são armazenados em uma lista e salvos no arquivo `funcionarios.json`.

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

* Criação e organização de funções;
* Listas e dicionários;
* Estruturas de repetição e condições;
* Validação de dados com `try` e `except`;
* Leitura e gravação de arquivos JSON;
* Organização e reutilização de código;
* Controle de versão com Git e GitHub;
* Desenvolvimento das operações de cadastro, consulta, atualização e exclusão.

## Próximas melhorias

* Dividir o código em diferentes arquivos e módulos;
* Criar testes automatizados;
* Melhorar a validação do CPF;
* Adicionar busca por nome;
* Criar relatórios por setor;
* Desenvolver uma interface gráfica;
* Substituir o arquivo JSON por um banco de dados.
