import re
from typing import List
from colorama import Fore, Style, init
from collections import defaultdict

# Inicializa o colorama para funcionar no terminal
init(autoreset=True)

class Token:
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}')"

class AnaliseLexica:
    # Definindo os padrões para os tokens
    KEYWORDS = r'\b(se|senao|enquanto|para|retornar|numero|frase|inicio|fim)\b'
    IDENTIFIER = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    NUMBER = r'\b\d+(\.\d+)?\b'
    OPERATOR = r'[+\-*/=<>!]+'  # Operadores como +, -, *, /, =, <, >, etc.
    SYMBOL = r'[{}();,]'  # Símbolos como {, }, ;, (, )
    STRING = r'"[^"\n]*"'  # Strings entre aspas

    pattern = re.compile(
        f'(?P<KEYWORDS>{KEYWORDS})|'
        f'(?P<IDENTIFIER>{IDENTIFIER})|'
        f'(?P<NUMBER>{NUMBER})|'
        f'(?P<OPERATOR>{OPERATOR})|'
        f'(?P<SYMBOL>{SYMBOL})|'
        f'(?P<STRING>{STRING})'
    )

    @staticmethod
    def de_token(code: str) -> List[Token]:
        tokens = []
        grouped_tokens = defaultdict(list)  # Agrupar tokens por tipo
        unique_tokens = defaultdict(set)  # Usar set para garantir valores únicos

        print("\n" + "-"*50)  # Linha de separação visual
        print(f"{'Token':<15} {'Valor':<20} {'Descrição':<40}")  # Cabeçalho da tabela
        print("-"*50)

        # Análise dos tokens
        for match in AnaliseLexica.pattern.finditer(code):
            for tipo in ['SYMBOL', 'STRING', 'KEYWORDS', 'IDENTIFIER', 'NUMBER', 'OPERATOR']:
                if match.group(tipo):
                    valor = match.group(tipo)
                    tokens.append(Token(tipo, valor))
                    unique_tokens[tipo].add(valor)  # Adicionar valor ao set para garantir unicidade

        # Exibir os tokens agrupados por tipo sem repetições
        for tipo in ['KEYWORDS', 'IDENTIFIER', 'NUMBER', 'OPERATOR', 'SYMBOL', 'STRING']:
            if tipo in unique_tokens:
                print(f"\n{tipo}:")
                for valor in unique_tokens[tipo]:
                    token = Token(tipo, valor)
                    # Determinar a cor e descrição do token
                    if tipo == 'KEYWORDS':
                        cor = Fore.GREEN
                        descricao = "Palavra reservada que tem um significado especial na linguagem de programação."
                    elif tipo == 'IDENTIFIER':
                        cor = Fore.CYAN
                        descricao = "Nome dado a variáveis, funções ou outros elementos definidos pelo programador."
                    elif tipo == 'NUMBER':
                        cor = Fore.YELLOW
                        descricao = "Valor literal numérico que pode ser inteiro ou decimal."
                    elif tipo == 'OPERATOR':
                        cor = Fore.MAGENTA
                        descricao = "Símbolos utilizados para realizar operações matemáticas ou lógicas."
                    elif tipo == 'SYMBOL':
                        cor = Fore.RED
                        descricao = "Símbolos usados para estruturar o código, como parênteses e ponto e vírgula."
                    elif tipo == 'STRING':
                        cor = Fore.BLUE
                        descricao = "Sequência de caracteres representada entre aspas."
                    
                    # Exibir o token com a formatação
                    print(f"{cor}{token.tipo:<15} {token.valor:<20} {descricao}")
                print("-" * 50)

        return tokens
