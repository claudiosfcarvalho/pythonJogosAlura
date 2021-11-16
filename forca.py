import arquivo
import mensagens

nome_arquivo = "palavras.txt"
def mensagem_enforcou(palavra_secreta):
    mensagens.imprimir_mensagem_perdeu()

def jogar():
    mensagens.imprimir_mensagem_abertura("Forca")

    palavra_secreta = arquivo.obter_palavra(nome_arquivo)

    enforcou = False
    acertou = False
    tentativas = 0
    maximo_tentativas = 7

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_letra()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            print(f"Erro {tentativas} de {maximo_tentativas}")
            mensagens.imprimir_forca(tentativas)

        # há várias formas de obter o acerto
        # acertou = "_" not in letras_acertadas
        acertou = letras_acertadas.count("_") == 0
        enforcou = tentativas == maximo_tentativas

        print(letras_acertadas)

    if(acertou):
        mensagens.imprimir_mensagem_ganhou()
    else:
        mensagem_enforcou(palavra_secreta)


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    # return letras_acertadas

def pede_letra():
    chute = input("Qual letra? ")
    return chute.strip().upper()

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__ == "__main__"):
    print("Abrindo jogo")
    jogar()