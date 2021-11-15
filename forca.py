print("Import forca ok")
def jogar():
    print("*********************************")
    print("Bem vind@ no jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}", format(chute, index))
        print("jogando")
    print("Fim do jogo")

if(__name__ == "__main__"):
    print("Abrindo jogo")
    jogar()