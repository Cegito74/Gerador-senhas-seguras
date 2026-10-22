# Gerador-senhas-seguras
Aplicação desenvolvida em Python para geração de senhas seguras e aleatórias, com apoio de Inteligência Artificial Generativa, como mini-projeto do curso de Engenharia de Software da AKCIT/UFG.


## 1. Descrição do projeto

Mini-projeto desenvolvido em Python, com apoio de Inteligência Artificial Generativa, como atividade do curso de Engenharia de Software da AKCIT/UFG.

O objetivo é gerar senhas aleatórias e seguras, permitindo configurar o tamanho e a utilização de letras maiúsculas, minúsculas, números e caracteres especiais.

## 2. Tecnologias utilizadas

- Python 3
- Biblioteca `secrets`
- Biblioteca `string`
- Biblioteca `unittest`
- Git e GitHub
- GitHub Codespaces
- Inteligência Artificial Generativa (ChatGPT)

## 3. Funcionalidades

- Geração de senhas aleatórias.
- Configuração do tamanho da senha.
- Inclusão opcional de letras maiúsculas, números e símbolos.
- Validação do tamanho mínimo de oito caracteres.
- Garantia de utilização dos grupos de caracteres selecionados.
- Demonstração automática da geração de senhas.

## 4. Como executar

Abra o projeto em um ambiente com Python 3 instalado.

No terminal, execute:

`python3 gerador_senhas.py`

O programa apresentará exemplos de senhas geradas com diferentes tamanhos e configurações.

## 5. Como executar os testes

No terminal, execute:

`python3 -m unittest -v test_gerador.py`

O arquivo de testes verifica o tamanho das senhas, os caracteres permitidos e a rejeição de tamanhos inferiores ao mínimo.

## 6. Utilização da Inteligência Artificial Generativa

A IA generativa foi utilizada como ferramenta de apoio para:

- Elaborar a estrutura inicial do código.
- Implementar a lógica de geração de senhas.
- Corrigir problemas encontrados durante a execução.
- Criar testes automatizados.
- Organizar e documentar o projeto.

As sugestões foram revisadas e verificadas por meio da execução do programa e de testes automatizados.

## 7. Desafios encontrados

Durante o desenvolvimento, um dos desafios foi o erro relacionado à função `input()`, que não era suportada pelo ambiente de execução inicialmente utilizado.

A solução foi adaptar o programa para executar exemplos automaticamente.

Outro desafio foi sincronizar os arquivos do GitHub com o Codespaces, resolvido utilizando o comando `git pull origin main`.

## 8. Considerações finais

O projeto permitiu aplicar conceitos de programação, testes, documentação e controle de versões.

A experiência demonstrou como a IA generativa pode contribuir para o desenvolvimento de software, desde que suas sugestões sejam revisadas, testadas e validadas.

A responsabilidade pela qualidade e segurança do software continua sendo do desenvolvedor.
