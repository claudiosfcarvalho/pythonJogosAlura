print("Import forca ok")
def jogar():
    print("*********************************")
    print("Bem vind@ no jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = []
    pos = 0

    while(pos < len(palavra_secreta)):
        letras_acertadas.append("_")
        pos = pos + 1

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        if(letras_acertadas.count("_") == 0):
            acertou = True
        print(letras_acertadas)
    print("Fim do jogo")

if(__name__ == "__main__"):
    print("Abrindo jogo")
    jogar()