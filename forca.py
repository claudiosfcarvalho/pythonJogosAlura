import random

print("Import forca ok")
def jogar():
    print("*********************************")
    print("Bem vind@ no jogo de Forca!")
    print("*********************************")

    palavra_secreta = obter_palavra()
    enforcou = False
    acertou = False
    tentativas = 0
    maximo_tentativas = 6
    letras_acertadas = ["_" for letra in palavra_secreta]

    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print(f"Erro {tentativas} de {maximo_tentativas}")

        # há várias formas de obter o acerto
        # acertou = "_" not in letras_acertadas
        acertou = letras_acertadas.count("_") == 0
        enforcou = tentativas == maximo_tentativas

        print(letras_acertadas)

    if(acertou):
        print("Você acertou")
    else:
        print("Você errou")
    print("Fim do jogo")

def obter_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha_arquivo in arquivo:
        palavras.append(linha_arquivo.strip().upper())

    arquivo.close()
    # print("lista de palavras", palavras)
    index = random.randrange(0,len(palavras))
    palavra = palavras[index]
    return palavra

if(__name__ == "__main__"):
    print("Abrindo jogo")
    jogar()