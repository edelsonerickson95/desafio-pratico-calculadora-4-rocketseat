
# Calculadora 4 - Rocketseat

API Flask que calcula a média aritmética de uma lista de números.

## Rota

POST /calculator/4

## Exemplo de body

{
  "numbers": [10, 20, 30]
}

## Resposta

{
  "data": {
    "Calculator": 4,
    "value": 20.0,
    "Success": true
  }
}
Conheça o projeto
Neste desafio, você vai implementar uma nova rota chamada "calculator_4" seguindo o exemplo dado pelo instrutor no
módulo. A rota deve calcular a média entre uma lista de números fornecida em uma requisição POST,
aplicando todas as boas práticas ensinadas.

Instruções
Estrutura, regras e requisitos do projeto

Seu desafio é criar uma nova funcionalidade para a aplicação de calculadora, implementando uma rota que receba uma lista
de números via POST e retorne a média aritmética desses valores. A implementação deve seguir rigorosamente os padrões e
boas práticas demonstrados pelo instrutor no módulo.

Requisitos da implementação:
A criação da nova rota deve ser chamada de "calculator_4" e deve possuir todas as boas práticas conforme ensinado no
módulo. Como por exemplo:

Testes unitários
Arquivos separados por responsabilidade (conforme feito pelo instrutor)
Tratamento de erro em caso de um envio de requisição no formato errado
