import random

def obter_palavra():
    palavra = "banana"
    with open("palavras.txt", "r") as arquivo:
        palavras = []

        for linha_arquivo in arquivo:
            palavras.append(linha_arquivo.strip().upper())

        # print("lista de palavras", palavras)
        index = random.randrange(0, len(palavras))
        palavra = palavras[index]
    return palavra