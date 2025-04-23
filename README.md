# Analisador Léxico - Ferramenta Educacional para Ensino de Programação

Este projeto implementa um analisador léxico em Python que visa ajudar estudantes a aprenderem conceitos fundamentais de linguagens de programação. A ferramenta pode ser utilizada como parte de um compilador de uma linguagem simplificada, similar ao Portugol, permitindo que os alunos compreendam a lógica de programação de maneira didática.

## Objetivo

O principal objetivo deste projeto é fornecer uma ferramenta que possa ler código-fonte em uma linguagem simplificada e identificar tokens (como palavras-chave, identificadores, operadores, números e símbolos) para que os alunos possam compreender a estrutura do código e a importância de cada elemento em uma linguagem de programação.

## Funcionalidades

- **Leitura de código-fonte**: O código-fonte é lido a partir de um arquivo `.txt`.
- **Análise de tokens**: Identificação e classificação de tokens como palavras-chave, identificadores, operadores, números, símbolos e strings.
- **Ignorar espaços em branco e comentários**: Comentários e espaços em branco são ignorados na análise.
- **Saída didática**: A saída é visualmente organizada e didática, com a descrição dos tipos de tokens identificados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para o desenvolvimento do analisador.
- **Regular Expressions (Regex)**: Utilizado para a identificação de tokens.
- **Colorama**: Biblioteca para formatação de saída no terminal com cores.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Para instalar o Python, acesse [python.org](https://www.python.org/).

Você também precisará instalar a biblioteca `colorama` para uma melhor visualização da saída no terminal:

```bash
pip install colorama
