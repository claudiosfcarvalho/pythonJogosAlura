print("*********************************")
print("Bem vind@ no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou", chute)

if(chute.isnumeric()):
    numero_chute = int(chute)
    acertou = numero_chute == numero_secreto
    maior   = numero_chute > numero_secreto
    menor   = numero_chute < numero_secreto
    if(acertou):
        print("Acertou")
    else:
        if(maior):
            print("Errou! O seu chute foi maior do que o número secreto")
        elif(menor):
            print("Errou! O seu chute foi menor do que o número secreto")
else:
    print("Somente números são aceitos")

print("Fim do Jogo")