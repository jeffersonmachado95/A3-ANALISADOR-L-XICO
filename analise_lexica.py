import re
from typing import List
from collections import defaultdict, Counter
from colorama import Fore, Style, init
import PySimpleGUI as sg

# Inicializa o colorama para o terminal (caso queira também exibir no console)
init(autoreset=True)

class Token:
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}')"

class AnaliseLexica:
    KEYWORDS = r'\b(se|senao|enquanto|para|retornar|numero|frase|inicio|fim)\b'
    IDENTIFIER = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    NUMBER = r'\b\d+(\.\d+)?\b'
    OPERATOR = r'[+\-*/=<>!]+'
    SYMBOL = r'[{}();,]'
    STRING = r'"[^"\n]*"'

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
        for match in AnaliseLexica.pattern.finditer(code):
            for tipo in ['SYMBOL', 'STRING', 'KEYWORDS', 'IDENTIFIER', 'NUMBER', 'OPERATOR']:
                if match.group(tipo):
                    valor = match.group(tipo)
                    tokens.append(Token(tipo, valor))
                    break
        return tokens

def gerar_resumo(tokens: List[Token]) -> str:
    resumo = []

    if any(t.tipo == 'KEYWORDS' and t.valor == 'inicio' for t in tokens):
        resumo.append("- O código possui um ponto de início, indicando o começo da execução.")
    if any(t.tipo == 'KEYWORDS' and t.valor == 'retornar' for t in tokens):
        resumo.append("- Há um comando de retorno de valor, indicando fim ou saída de função.")
    if any(t.tipo == 'KEYWORDS' and t.valor in ['se', 'senao'] for t in tokens):
        resumo.append("- O código usa estruturas condicionais (if/else).")
    if any(t.tipo == 'KEYWORDS' and t.valor in ['enquanto', 'para'] for t in tokens):
        resumo.append("- Laços de repetição identificados (while/for).")
    if any(t.tipo == 'NUMBER' for t in tokens):
        resumo.append("- Manipulação de números está presente.")
    if any(t.tipo == 'STRING' for t in tokens):
        resumo.append("- O código utiliza textos (strings).")
    if any(t.tipo == 'OPERATOR' for t in tokens):
        resumo.append("- Operações aritméticas ou lógicas estão presentes.")
    if any(t.tipo == 'KEYWORDS' and t.valor in ['numero', 'frase'] for t in tokens):
        resumo.append("- Declarações de variáveis detectadas.")

    return "\n".join(resumo) if resumo else "Nenhuma estrutura significativa identificada."

def exibir_tokens_em_janela(tokens: List[Token]):
    # Contar as ocorrências por tipo e valor
    contagem_por_tipo = defaultdict(list)
    for token in tokens:
        contagem_por_tipo[token.tipo].append(token.valor)

    # Construir o texto formatado
    saida_tokens = ""
    for tipo in sorted(contagem_por_tipo.keys()):
        valores = contagem_por_tipo[tipo]
        total = len(valores)
        contagem_valores = Counter(valores)
        saida_tokens += f"[{tipo}] ({total} ocorrência{'s' if total != 1 else ''})\n"
        for valor, count in sorted(contagem_valores.items()):
            saida_tokens += f"  - {valor} ({count}x)\n"
        saida_tokens += "\n"

    # Gerar o resumo técnico
    resumo = gerar_resumo(tokens)

    # Criar a janela com PySimpleGUI
    layout = [
        [sg.Text("Resultado da Análise Léxica", font=("Arial", 14))],
        [sg.Multiline(saida_tokens, size=(80, 20), disabled=True, font=("Courier New", 10))],
        [sg.Text("Resumo do Código:", font=("Arial", 12, 'bold'))],
        [sg.Multiline(resumo, size=(80, 6), disabled=True, font=("Courier New", 10))],
        [sg.Button("Fechar")]
    ]
    window = sg.Window("Visualização de Tokens e Resumo", layout)

    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            break
    window.close()

# Execução direta para testes
if __name__ == "__main__":
    with open('code.txt', 'r', encoding='utf-8') as file:
        codigo = file.read()

    tokens = AnaliseLexica.de_token(codigo)
    exibir_tokens_em_janela(tokens)