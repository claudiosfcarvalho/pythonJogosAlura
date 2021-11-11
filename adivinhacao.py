print("*********************************")
print("Bem vind@ no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for tentativa in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute)
    validacao_ok = True
    numero_chute = 0

    if (not chute.isnumeric()):
        print("Apenas números entre 1 e 100 são aceitos")
        validacao_ok = False
    else:
        numero_chute = int(chute)
        if (numero_chute < 1 or numero_chute > 100):
            print("Apenas números entre 1 e 100 são aceitos")
            validacao_ok = False

    if (validacao_ok):
        acertou = numero_chute == numero_secreto
        maior   = numero_chute > numero_secreto
        menor   = numero_chute < numero_secreto

        if(acertou):
            print("Acertou")
            break
        else:
            if(maior):
                print("Errou! O seu chute foi maior do que o número secreto")
            elif(menor):
                print("Errou! O seu chute foi menor do que o número secreto")

print("Fim do Jogo")