from analise_lexica import AnaliseLexica

def main():
    with open('code.txt', 'r', encoding='utf-8') as file:
        code = file.read()

    print("Código fonte lido:")
    print(code)
    print("\nTokens encontrados:\n")

    tokens = AnaliseLexica.de_token(code)

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
