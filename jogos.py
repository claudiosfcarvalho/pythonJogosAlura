import adivinhacao
import forca

sair = False

while(not sair):
    print("\n*********************************")
    print("***** Escolha o seu Jogo ********!")
    print("*********************************\n")
    print("(1) Forca \n(2) Adivinhação \n(9) Sair")
    jogo = int(input("Qual jogo? "))
    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 9):
        sair = True
