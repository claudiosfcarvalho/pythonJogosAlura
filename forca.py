print("Import forca ok")
def jogar():
    print("*********************************")
    print("Bem vind@ no jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou = False
    tentativas = 0
    maximo_tentativas = 6
    letras_acertadas = []
    pos = 0

    while(pos < len(palavra_secreta)):
        letras_acertadas.append("_")
        pos = pos + 1

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

        acertou = letras_acertadas.count("_") == 0
        enforcou = tentativas == maximo_tentativas

        print(letras_acertadas)

    if(acertou):
        print("Você acertou")
    else:
        print("Você errou")
    print("Fim do jogo")

if(__name__ == "__main__"):
    print("Abrindo jogo")
    jogar()