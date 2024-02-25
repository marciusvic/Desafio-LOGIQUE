# Projeto Desafio LOGIQUE

## DESAFIO 1 - ENTREVISTA E DEFESA DO PROJETO
Feito por [Márcio Victor de Andrade Rocha](https://github.com/marciusvic).

## Descrição do Projeto
O Projeto é um sistema de gerenciamento de ponto eletrônico, onde o usuário admin pode realizar o cadastro de funcionários e empresas, e o usuário comum pode realizar o login, registrar o ponto de entrada e saída, e visualizar o relatório de ponto.

### Arquitetura
O projeto segue a arquitetura Model-View-Template (MVT) do framework Django, proporcionando uma organização eficiente e modular do código. Isso facilita o desenvolvimento, manutenção e escalabilidade do sistema.

## Funcionalidades Principais
- Gerenciamento de Funcionários e Empresas
- Registro de Ponto
- Relatório de Ponto

## Tecnologias Utilizadas
- Linguagem: Python
- Framework Backend: Django
- Banco de Dados: SQLITE3

## Como rodar o projeto
1. Clone o repositório
2. Instale o Python
3. Ative o ambiente virtual com o comando `.\venv\Scripts\activate` (WINDOWS)
4. Instale os pacotes necessários com o comando `pip install -r requirements.txt` (WINDOWS)
3. Rode o servidor com o comando `python manage.py runserver`

## Como utilizar o sistema
# Como Usuário comum
1. Acesse a página de login `http://localhost:8000/`
2. Faça o login com o CPF `12345678901` e senha `senha123`
3. Registre o ponto de entrada e saída

# Como Usuário Admin
