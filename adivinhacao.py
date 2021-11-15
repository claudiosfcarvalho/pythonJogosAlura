import random

print("*********************************")
print("Bem vind@ no jogo de Adivinhação!")
print("*********************************")

#numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

for tentativa in range(1,total_de_tentativas + 1):
    print("\nTentativa {} de {}".format(tentativa, total_de_tentativas))
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
            print("Acertou\n")
            break
        else:
            if(maior):
                print("Errou! O seu chute foi maior do que o número secreto\n")
            elif(menor):
                print("Errou! O seu chute foi menor do que o número secreto\n")
if (not acertou):
    print("O número secreto é", numero_secreto)
print("Fim do Jogo")