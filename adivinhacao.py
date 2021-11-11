print("*********************************")
print("Bem vind@ no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1
while(tentativa <= total_de_tentativas):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute = input("Digite o seu número: ")

    print("Você digitou", chute)

    if(chute.isnumeric()):
        numero_chute = int(chute)
        acertou = numero_chute == numero_secreto
        maior   = numero_chute > numero_secreto
        menor   = numero_chute < numero_secreto
        if(acertou):
            print("Acertou")
            tentativa = total_de_tentativas
        else:
            if(maior):
                print("Errou! O seu chute foi maior do que o número secreto")
            elif(menor):
                print("Errou! O seu chute foi menor do que o número secreto")
    else:
        print("Somente números são aceitos")

    tentativa = tentativa + 1
print("Fim do Jogo")