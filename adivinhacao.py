print("*********************************")
print("Bem vind@ no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou", chute)

if(chute.isnumeric()):
    numero_chute = int(chute)
    if(numero_secreto == numero_chute):
        print("Acertou")
    else:
        print("Errou")
else:
    print("Somente números são aceitos")

print("Fim do Jogo")